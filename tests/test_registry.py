from datetime import datetime, timedelta, timezone
import unittest
from handoff.registry import (HandoffRecord, PublicationUncertain, RegistryConflict, RegistryError, RegistrySnapshot, StaleExecution, advance, parse, publish, render)

UTC = timezone.utc
START = datetime(2026, 11, 12, 10, 0, tzinfo=UTC)

def record(number, status="NO_OP"):
    started = START + timedelta(minutes=number * 10)
    return HandoffRecord(f"worker-{number:03d}", started, started + timedelta(minutes=1), status, f"execution {number}", (f"https://example.invalid/runs/{number}",))

class Store:
    def __init__(self, body): self.body = body
    def read_body(self): return self.body
    def write_body(self, body): self.body = body

class OverwritingStore(Store):
    def write_body(self, body): self.body = render(RegistrySnapshot(1, 0, record(99), (record(99),)))

class RegistryTests(unittest.TestCase):
    def test_read_write_cycle_no_op_to_pr_ready(self):
        store = Store(render(RegistrySnapshot(0, None, None)))
        publish(store, record(1), expected_revision=0)
        result = publish(store, record(2, "PR_READY"), expected_revision=1)
        self.assertEqual([x.status for x in result.recent], ["PR_READY", "NO_OP"])
        self.assertEqual(parse(store.body), result)
    def test_retains_ten_and_round_trips(self):
        snapshot = RegistrySnapshot(0, None, None)
        for number in range(1, 13): snapshot = advance(snapshot, record(number), expected_revision=number - 1)
        self.assertEqual((len(snapshot.recent), snapshot.recent[-1].execution_id), (10, "worker-003"))
        self.assertEqual(parse(render(snapshot)), snapshot)
    def test_conflict_stale_and_uncertain_publication_fail_closed(self):
        snapshot = advance(RegistrySnapshot(0, None, None), record(2), expected_revision=0)
        with self.assertRaises(RegistryConflict): advance(snapshot, record(3), expected_revision=0)
        with self.assertRaises(StaleExecution): advance(snapshot, record(1), expected_revision=1)
        with self.assertRaises(PublicationUncertain): publish(OverwritingStore(render(RegistrySnapshot(0, None, None))), record(1), expected_revision=0)
    def test_rejects_naive_duplicate_invalid_and_malformed(self):
        with self.assertRaises(RegistryError): HandoffRecord("x", datetime(2026, 1, 1), datetime(2026, 1, 1), "NO_OP", "x")
        one = record(1)
        with self.assertRaises(RegistryError): RegistrySnapshot(1, 0, one, (one, one))
        with self.assertRaises(RegistryError): RegistrySnapshot(1, 0, one, (record(2),))
        with self.assertRaises(RegistryError): RegistrySnapshot(2, 0, one, (one,))
        with self.assertRaises(RegistryError): parse("# WORKER-HANDOFF-01\nRevision: x\n")
        with self.assertRaises(RegistryError): parse(render(RegistrySnapshot(1, 0, one, (one,))).replace("### 1", "### 2"))
