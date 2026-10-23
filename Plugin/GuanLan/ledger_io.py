"""Single-file atomic writes, not a multi-file transaction.

Callers must supply the shared ledger lock and recovery protocol.
The destination parent must already exist; no fallback paths are used.
File fsync does not by itself guarantee directory-entry durability on Windows.
"""
import json
import os
import tempfile
from pathlib import Path


def atomic_write_bytes(path, data):
    """Replace one file after fully writing and syncing a unique sibling.

    A failure before os.replace leaves the destination unchanged.
    No claim of cross-file atomicity or protection against uncoordinated writers.
    """
    if not isinstance(data, bytes):
        raise TypeError("ledger payload must be bytes")
    target = Path(path)
    parent = target.parent
    if not parent.is_dir():
        raise FileNotFoundError("ledger destination directory missing")
    if target.is_symlink():
        raise ValueError("symlink ledger destination refused")
    if target.exists() and not target.is_file():
        raise ValueError("ledger destination must be a regular file")

    temporary = None
    fd = None
    try:
        fd, temporary = tempfile.mkstemp(
            prefix="." + target.name + ".", suffix=".tmp", dir=str(parent))
        stream = os.fdopen(fd, "wb")
        fd = None
        with stream:
            stream.write(data)
            stream.flush()
            os.fsync(stream.fileno())
        os.replace(temporary, target)
        temporary = None
    finally:
        if fd is not None:
            os.close(fd)
        if temporary is not None:
            try:
                os.unlink(temporary)
            except FileNotFoundError:
                pass


def atomic_write_json(path, value):
    """Serialize before touching disk; reject NaN/Infinity, preserve UTF-8."""
    payload = json.dumps(
        value, ensure_ascii=False, indent=2, allow_nan=False
    ).encode("utf-8")
    atomic_write_bytes(path, payload)