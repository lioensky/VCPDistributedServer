"""Explicit recovery-before-access guard.

Every participant must use the same root, journal allowlist, and lock file.
This module supplies no production defaults and does not initiate a transaction.
The lock must be reentrant if guarded business code nests ledger helpers.
"""
from contextlib import contextmanager

from ledger_recovery import RecoveryStore


@contextmanager
def recovered_access(root, allowed_names, lock):
    """Hold the caller's lock across recovery and the entire business operation.

    Recovery errors propagate BEFORE yielding, preserving the journal and
    preventing business reads or writes. Exceptions from business code are
    not swallowed and do not imply rollback: writes must use LedgerBatch.
    """
    with lock:
        store = RecoveryStore(root, allowed_names)
        store.recover()
        yield store