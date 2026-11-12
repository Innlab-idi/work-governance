"""Deterministic WORKER-HANDOFF-01 issue-body registry helpers.

GitHub issue-body writes do not provide compare-and-swap. V1 therefore requires
one strictly serialized publisher and fails closed on non-identical readback.
"""
from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Protocol

VALID_STATUSES = frozenset({"NO_OP", "PR_READY", "FAILED"})
MAX_RECENT = 10
EMPTY_CURRENT = "No accepted execution yet."
EMPTY_RECENT = "No accepted executions yet."


class RegistryError(ValueError): pass
class RegistryConflict(RegistryError): pass
class StaleExecution(RegistryError): pass
class PublicationUncertain(RegistryError): pass


class IssueBodyStore(Protocol):
    def read_body(self) -> str: ...
    def write_body(self, body: str) -> None: ...


@dataclass(frozen=True)
class HandoffRecord:
    execution_id: str
    started_at: datetime
    completed_at: datetime
    status: str
    summary: str
    references: tuple[str, ...] = ()

    def __post_init__(self) -> None:
        if not self.execution_id or not self.summary:
            raise RegistryError("execution_id and summary are required")
        _aware(self.started_at, "started_at")
        _aware(self.completed_at, "completed_at")
        if self.completed_at < self.started_at:
            raise RegistryError("completed_at precedes started_at")
        if self.status not in VALID_STATUSES:
            raise RegistryError(f"unsupported status: {self.status}")
        if any(not item for item in self.references):
            raise RegistryError("references cannot contain empty values")


@dataclass(frozen=True)
class RegistrySnapshot:
    revision: int
    parent_revision: int | None
    current: HandoffRecord | None
    recent: tuple[HandoffRecord, ...] = ()

    def __post_init__(self) -> None:
        if self.revision < 0:
            raise RegistryError("revision cannot be negative")
        if self.revision == 0:
            if self.parent_revision is not None or self.current is not None or self.recent:
                raise RegistryError("revision 0 must be the empty bootstrap snapshot")
            return
        if self.parent_revision != self.revision - 1:
            raise RegistryError("parent revision must immediately precede revision")
        if self.current is None or not self.recent or self.recent[0] != self.current:
            raise RegistryError("CURRENT must be RECENT entry 1")
        if len(self.recent) > MAX_RECENT:
            raise RegistryError("recent exceeds retention limit")
        ids = [item.execution_id for item in self.recent]
        if len(ids) != len(set(ids)):
            raise RegistryError("RECENT contains duplicate execution IDs")


def advance(snapshot: RegistrySnapshot, record: HandoffRecord, *, expected_revision: int) -> RegistrySnapshot:
    if snapshot.revision != expected_revision:
        raise RegistryConflict(f"expected revision {expected_revision}, observed {snapshot.revision}")
    if record.execution_id in {item.execution_id for item in snapshot.recent}:
        raise RegistryConflict("execution ID already exists in RECENT")
    if snapshot.current and record.started_at < snapshot.current.completed_at:
        raise StaleExecution("execution started before CURRENT completed")
    return RegistrySnapshot(snapshot.revision + 1, snapshot.revision, record,
                            (record, *snapshot.recent[:MAX_RECENT - 1]))


def publish(store: IssueBodyStore, record: HandoffRecord, *, expected_revision: int) -> RegistrySnapshot:
    """Read/write/read for the sole v1 publisher; this is not atomic."""
    successor = advance(parse(store.read_body()), record, expected_revision=expected_revision)
    store.write_body(render(successor))
    confirmed = parse(store.read_body())
    if confirmed != successor:
        raise PublicationUncertain("issue body readback does not match publication")
    return confirmed


def render(snapshot: RegistrySnapshot) -> str:
    parent = "None" if snapshot.parent_revision is None else str(snapshot.parent_revision)
    lines = ["# WORKER-HANDOFF-01", f"Revision: {snapshot.revision}", f"Parent revision: {parent}", "", "## CURRENT"]
    lines.extend([EMPTY_CURRENT] if snapshot.current is None else _record_lines(snapshot.current))
    lines.extend(["", "## RECENT"])
    if not snapshot.recent:
        lines.append(EMPTY_RECENT)
    for index, record in enumerate(snapshot.recent, 1):
        lines.extend([f"### {index}", *_record_lines(record)])
    return "\n".join(lines) + "\n"


def parse(body: str) -> RegistrySnapshot:
    """Parse the exact persisted format and validate all invariants."""
    lines = body.splitlines()
    if len(lines) < 7 or lines[0] != "# WORKER-HANDOFF-01" or lines[3:5] != ["", "## CURRENT"]:
        raise RegistryError("malformed handoff header")
    revision = _integer(_value(lines[1], "Revision: "), "revision")
    raw_parent = _value(lines[2], "Parent revision: ")
    parent = None if raw_parent == "None" else _integer(raw_parent, "parent revision")
    try: recent_at = lines.index("## RECENT", 5)
    except ValueError as error: raise RegistryError("missing RECENT section") from error
    if recent_at == 5 or lines[recent_at - 1] != "":
        raise RegistryError("CURRENT and RECENT must be separated by one blank line")
    current_lines = lines[5:recent_at - 1]
    current = None if current_lines == [EMPTY_CURRENT] else _record(current_lines)
    recent = _recent(lines[recent_at + 1:])
    return RegistrySnapshot(revision, parent, current, recent)


def _recent(lines: list[str]) -> tuple[HandoffRecord, ...]:
    if lines == [EMPTY_RECENT]: return ()
    records, position = [], 0
    while position < len(lines):
        if lines[position] != f"### {len(records) + 1}":
            raise RegistryError("RECENT entries must be sequentially numbered")
        records.append(_record(lines[position + 1:position + 7]))
        position += 7
    return tuple(records)


def _record(lines: list[str]) -> HandoffRecord:
    if len(lines) != 6: raise RegistryError("record must contain exactly six fields")
    refs = _field(lines[5], "References: ")
    return HandoffRecord(_field(lines[0], "Execution: `", "`"),
        _timestamp(_field(lines[1], "Started UTC: "), "started UTC"),
        _timestamp(_field(lines[2], "Completed UTC: "), "completed UTC"),
        _field(lines[3], "Status: "), _field(lines[4], "Summary: "),
        () if refs == "None" else tuple(refs.split(", ")))


def _field(line: str, prefix: str, suffix: str = "") -> str:
    wanted = f"- {prefix}"
    if not line.startswith(wanted) or (suffix and not line.endswith(suffix)):
        raise RegistryError(f"malformed field: {line}")
    value = line[len(wanted):len(line) - len(suffix) if suffix else None]
    if not value: raise RegistryError(f"empty field: {prefix}")
    return value


def _value(line: str, prefix: str) -> str:
    if not line.startswith(prefix) or line == prefix: raise RegistryError(f"malformed field: {prefix}")
    return line[len(prefix):]


def _integer(value: str, name: str) -> int:
    if not value.isdecimal(): raise RegistryError(f"{name} must be a non-negative integer")
    return int(value)


def _timestamp(value: str, name: str) -> datetime:
    try: parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError as error: raise RegistryError(f"invalid {name}") from error
    _aware(parsed, name)
    if not value.endswith("Z"): raise RegistryError(f"{name} must use a UTC Z timestamp")
    return parsed


def _aware(value: datetime, name: str) -> None:
    if value.tzinfo is None or value.utcoffset() is None: raise RegistryError(f"{name} must include a timezone")


def _record_lines(record: HandoffRecord) -> list[str]:
    refs = ", ".join(record.references) if record.references else "None"
    return [f"- Execution: `{record.execution_id}`", f"- Started UTC: {utc(record.started_at)}",
        f"- Completed UTC: {utc(record.completed_at)}", f"- Status: {record.status}",
        f"- Summary: {record.summary}", f"- References: {refs}"]


def utc(value: datetime) -> str:
    _aware(value, "timestamp")
    return value.astimezone(timezone.utc).isoformat().replace("+00:00", "Z")
