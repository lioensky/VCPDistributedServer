"""Real booking transaction adapter. No production paths or IO at import.

All real ledger participants must use access() before reading or writing.
A shared external lock serializes operations; a separate journal avoids
confusing paper recovery participants. Not a request deduplication layer.
"""
import json
from contextlib import contextmanager
from contextvars import ContextVar
from pathlib import Path

from ledger_batch import LedgerBatch
from ledger_recovery import RecoveryStore, RecoveryError

class RealRecoveryStore(RecoveryStore):
    JOURNAL = ".real-ledger-recovery.json"

_ACTIVE = ContextVar("real_ledger_batch", default=None)

def current_batch():
    return _ACTIVE.get()

def _target(batch, path):
    target = Path(path)
    if target.parent.resolve() != batch.store.root:
        raise RecoveryError("real ledger outside transaction root")
    batch.store._path(target.name)
    return target.name

@contextmanager
def access(paths, lock):
    """Recover under lock, stage writes, commit only on normal completion.

    Exceptions discard in-memory writes before prepare. Commit exceptions
    retain the distinction supplied by LedgerBatch. Caller must not retry
    booking merely because it did not receive a normal response.
    """
    targets = [Path(p) for p in paths]
    if not targets:
        raise RecoveryError("explicit real ledger paths required")
    root = targets[0].parent.resolve()
    names = {p.name for p in targets}
    if (len(names) != len(targets)
            or any(p.parent.resolve() != root for p in targets)):
        raise RecoveryError("real ledgers require distinct names in one root")
    with lock:
        existing = current_batch()
        if existing is not None:
            if existing.store.root != root or existing.store.allowed != frozenset(names):
                raise RecoveryError("nested real transaction scope differs")
            yield existing
            return
        store = RealRecoveryStore(root, names)
        store.recover()
        batch = LedgerBatch(store)
        token = _ACTIVE.set(batch)
        try:
            yield batch
            batch.commit()
        finally:
            _ACTIVE.reset(token)

def read_json(path, missing):
    """Read staged content; missing is an explicit caller initialization value."""
    batch = current_batch()
    if batch is None:
        raise RecoveryError("real ledger read outside guarded access")
    raw = batch.read_bytes(_target(batch, path))
    return missing if raw is None else json.loads(raw)

def write_json(path, value):
    batch = current_batch()
    if batch is None:
        raise RecoveryError("real ledger write outside guarded access")
    batch.stage_json(_target(batch, path), value)