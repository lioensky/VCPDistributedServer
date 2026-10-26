"""In-memory staging over RecoveryStore; not wired into production.

Caller must hold the shared lock BEFORE recovery and initial business reads,
through staging, commit, and recovery. All readers/writers must participate.
No request deduplication; a committed operation may need receipt reconciliation.
"""
import json

from ledger_recovery import RecoveryError


class CommittedOutcomeError(RecoveryError):
    """Commit was persisted; reconcile ledgers before any operation retry."""


class LedgerBatch:
    def __init__(self, store):
        self.store = store
        self.changes = {}
        self.closed = False

    def _ensure_open(self):
        if self.closed:
            raise RecoveryError("batch is closed")

    def read_bytes(self, name):
        self._ensure_open()
        # Validate names even when a staged value is already present.
        path = self.store._path(name)
        if name in self.changes:
            return self.changes[name]
        try:
            return path.read_bytes()
        except FileNotFoundError:
            return None

    def stage_bytes(self, name, data):
        self._ensure_open()
        self.store._path(name)
        if not isinstance(data, bytes):
            raise RecoveryError("staged content must be bytes")
        self.changes[name] = data

    def stage_json(self, name, value):
        # Serialization must finish before changing the staged state.
        data = json.dumps(
            value, ensure_ascii=False, indent=2, allow_nan=False
        ).encode("utf-8")
        self.stage_bytes(name, data)

    def append_jsonl(self, name, row):
        line = json.dumps(
            row, ensure_ascii=False, allow_nan=False
        ).encode("utf-8") + b"\n"
        existing = self.read_bytes(name)
        data = existing if existing is not None else b""
        # Do not silently append to a damaged existing ledger.
        for old in data.splitlines():
            if old.strip():
                value = json.loads(old.decode("utf-8"))
                if not isinstance(value, dict):
                    raise RecoveryError("JSONL ledger requires object rows")
        if not isinstance(row, dict):
            raise RecoveryError("JSONL row must be an object")
        if data and not data.endswith((b"\n", b"\r")):
            data += b"\n"
        self.stage_bytes(name, data + line)

    def discard(self):
        """Before commit, discard only memory; never delete a recovery journal."""
        self._ensure_open()
        self.changes.clear()
        self.closed = True

    def commit(self):
        self._ensure_open()
        # Prevent reusing a batch after an uncertain commit outcome.
        self.closed = True
        if not self.changes:
            return "empty"
        # prepare refuses a pending journal. Do not recover someone else's
        # journal here: recovery belongs before the business reads.
        self.store.prepare(self.changes)
        try:
            for name in self.changes:
                self.store.apply_one(name)
            self.store.commit()
        except Exception as exc:
            # A recovery failure propagates and retains the journal:
            # callers must block new operations until recovery succeeds.
            outcome = self.store.recover()
            if outcome == "committed":
                raise CommittedOutcomeError(
                    "transaction committed; reconcile receipt before retry"
                ) from exc
            raise
        # The commit marker was persisted. Cleanup failure must not be
        # reported as an ordinary uncommitted business failure.
        try:
            self.store.recover()
        except Exception as exc:
            raise CommittedOutcomeError(
                "transaction committed; recovery cleanup requires attention"
            ) from exc
        return "committed"