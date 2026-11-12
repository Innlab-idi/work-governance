from datetime import datetime, timedelta, timezone
import unittest

from handoff.registry import HandoffRecord, RegistryConflict, RegistrySnapshot, StaleExecution, advance, render


UTC = timezone.utc
START = datetime(2026, 11, 12, 10, 0, tzinfo=UTC)


def record(number: int, status: str = "NO_OP") -> HandoffRecord:
    started = START + timedelta(minutes=number * 10)
    return HandoffRecord(
        execution_id=f"worker-{number:03d}",
        started_at=started,
        completed_at=started + timedelta(minutes=1),
        status=status,
        summary=f"execution {number}",
        references=(f"https://example.invalid/runs/{number}",),
    )


class RegistryTests(unittest.TestCase):
    def test_no_op_to_pr_ready_keeps_current_separate_from_recent(self) -> None:
        first = advance(RegistrySnapshot(0, None), record(1), expected_revision=0)
        second = advance(first, record(2, "PR_READY"), expected_revision=1)
        self.assertEqual(second.current.status, "PR_READY")
        self.assertEqual([item.status for item in second.recent], ["PR_READY", "NO_OP"])
        rendered = render(second, parent_revision=1)
        self.assertIn("## CURRENT\n- Execution: `worker-002`", rendered)
        self.assertIn("## RECENT\n### 1\n- Execution: `worker-002`", rendered)

    def test_retains_only_ten_most_recent_executions(self) -> None:
        snapshot = RegistrySnapshot(0, None)
        for number in range(1, 13):
            snapshot = advance(snapshot, record(number), expected_revision=number - 1)
        self.assertEqual(len(snapshot.recent), 10)
        self.assertEqual(snapshot.recent[0].execution_id, "worker-012")
        self.assertEqual(snapshot.recent[-1].execution_id, "worker-003")

    def test_conflicting_expected_revision_stops_without_overwrite(self) -> None:
        snapshot = advance(RegistrySnapshot(0, None), record(1), expected_revision=0)
        with self.assertRaises(RegistryConflict):
            advance(snapshot, record(2), expected_revision=0)
        self.assertEqual(snapshot.current.execution_id, "worker-001")

    def test_stale_execution_stops_without_replacing_current(self) -> None:
        snapshot = advance(RegistrySnapshot(0, None), record(2), expected_revision=0)
        with self.assertRaises(StaleExecution):
            advance(snapshot, record(1), expected_revision=1)
        self.assertEqual(snapshot.current.execution_id, "worker-002")


if __name__ == "__main__":
    unittest.main()
