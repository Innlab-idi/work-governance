"""Format and validate append-only worker handoff snapshots.

This module deliberately has no GitHub client.  GitHub publication remains a
human-triggered, reviewable operation; the helpers make snapshot construction
and optimistic-concurrency checks deterministic and testable.
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone


VALID_STATUSES = frozenset({"NO_OP", "PR_READY", "FAILED"})
MAX_RECENT = 10


class RegistryConflict(ValueError):
    """The caller did not build from the registry revision it expected."""


class StaleExecution(ValueError):
    """The execution began before the accepted CURRENT entry completed."""


@dataclass(frozen=True)
class HandoffRecord:
    execution_id: str
    started_at: datetime
    completed_at: datetime
    status: str
    summary: str
    references: tuple[str, ...] = ()

    def __post_init__(self) -> None:
        if not self.execution_id:
            raise ValueError("execution_id is required")
        if self.status not in VALID_STATUSES:
            raise ValueError(f"unsupported status: {self.status}")
        if self.completed_at < self.started_at:
            raise ValueError("completed_at precedes started_at")
        if not self.summary:
            raise ValueError("summary is required")


@dataclass(frozen=True)
class RegistrySnapshot:
    revision: int
    current: HandoffRecord | None
    recent: tuple[HandoffRecord, ...] = ()

    def __post_init__(self) -> None:
        if self.revision < 0:
            raise ValueError("revision cannot be negative")
        if len(self.recent) > MAX_RECENT:
            raise ValueError("recent exceeds retention limit")
        if self.current is not None and (not self.recent or self.recent[0] != self.current):
            raise ValueError("CURRENT must be the first RECENT entry")


def advance(
    snapshot: RegistrySnapshot, record: HandoffRecord, *, expected_revision: int
) -> RegistrySnapshot:
    """Create the next snapshot only from the observed revision.

    An adapter must publish this result only after confirming its source still
    has ``expected_revision``.  A mismatch is a stop-and-reconcile condition,
    never a cue to overwrite or retry a stale update.
    """
    if snapshot.revision != expected_revision:
        raise RegistryConflict(
            f"expected revision {expected_revision}, observed {snapshot.revision}"
        )
    if snapshot.current and record.started_at < snapshot.current.completed_at:
        raise StaleExecution(
            "execution started before CURRENT completed; reconcile instead"
        )
    recent = (record, *snapshot.recent[: MAX_RECENT - 1])
    return RegistrySnapshot(snapshot.revision + 1, record, recent)


def render(snapshot: RegistrySnapshot, *, parent_revision: int | None = None) -> str:
    """Render the exact Markdown snapshot posted to the central issue."""
    lines = ["# WORKER-HANDOFF-01", f"Revision: {snapshot.revision}"]
    if parent_revision is not None:
        lines.append(f"Parent revision: {parent_revision}")
    lines.extend(["", "## CURRENT"])
    if snapshot.current is None:
        lines.append("No accepted execution yet.")
    else:
        lines.extend(_record_lines(snapshot.current))
    lines.extend(["", "## RECENT"])
    if not snapshot.recent:
        lines.append("No accepted executions yet.")
    else:
        for index, record in enumerate(snapshot.recent, 1):
            lines.extend([f"### {index}", *_record_lines(record)])
    return "\n".join(lines) + "\n"


def _record_lines(record: HandoffRecord) -> list[str]:
    references = ", ".join(record.references) if record.references else "None"
    return [
        f"- Execution: `{record.execution_id}`",
        f"- Started UTC: {utc(record.started_at)}",
        f"- Completed UTC: {utc(record.completed_at)}",
        f"- Status: {record.status}",
        f"- Summary: {record.summary}",
        f"- References: {references}",
    ]


def utc(value: datetime) -> str:
    """Return a precise UTC timestamp and reject ambiguous datetimes."""
    if value.tzinfo is None:
        raise ValueError("timestamp must include a timezone")
    return value.astimezone(timezone.utc).isoformat().replace("+00:00", "Z")
