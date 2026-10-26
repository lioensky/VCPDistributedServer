"""Recoverable file-set updates; NOT yet wired into production.

Caller MUST hold the common lock across every method and all ledger access.
No request deduplication or power-loss durability guarantee is provided here.
"""
import base64
import hashlib
import json
import uuid
from pathlib import Path

from ledger_io import atomic_write_bytes, atomic_write_json


class RecoveryError(ValueError):
    pass


class RecoveryStore:
    JOURNAL = ".ledger-recovery.json"

    def __init__(self, root, allowed_names):
        supplied = Path(root)
        if supplied.is_symlink() or not supplied.is_dir():
            raise RecoveryError("invalid ledger root")
        self.root = supplied.resolve()
        self.allowed = frozenset(allowed_names)
        for name in self.allowed:
            self._name(name)
        self.journal = self.root / self.JOURNAL

    def _name(self, name):
        if (not isinstance(name, str) or not name
                or name in (".", "..", self.JOURNAL)
                or any(c in name for c in ("/", "\\", ":"))
                or name.startswith(".")):
            raise RecoveryError("invalid ledger filename")
        return name

    def _path(self, name):
        self._name(name)
        if name not in self.allowed:
            raise RecoveryError("ledger filename not allowed")
        path = self.root / name
        if path.is_symlink() or (path.exists() and not path.is_file()):
            raise RecoveryError("unsafe ledger target")
        return path

    def _read(self, name):
        path = self._path(name)
        try:
            return path.read_bytes()
        except FileNotFoundError:
            return None

    @staticmethod
    def _pack(data):
        if data is None:
            return None
        return {
            "data": base64.b64encode(data).decode("ascii"),
            "sha256": hashlib.sha256(data).hexdigest(),
        }

    @staticmethod
    def _unpack(value):
        if value is None:
            return None
        try:
            if not isinstance(value, dict) or set(value) != {"data", "sha256"}:
                raise ValueError()
            data = base64.b64decode(value["data"], validate=True)
            if hashlib.sha256(data).hexdigest() != value["sha256"]:
                raise ValueError()
            return data
        except (ValueError, TypeError, KeyError):
            raise RecoveryError("invalid journal payload") from None

    def _check_journal_path(self):
        if self.journal.is_symlink() or (
                self.journal.exists() and not self.journal.is_file()):
            raise RecoveryError("unsafe recovery journal")

    def _load(self):
        self._check_journal_path()
        try:
            record = json.loads(self.journal.read_text(encoding="utf-8"))
            if (not isinstance(record, dict) or record.get("version") != 1
                    or record.get("state") not in ("prepared", "committed")
                    or not isinstance(record.get("id"), str)
                    or not isinstance(record.get("files"), dict)
                    or not record["files"]):
                raise ValueError()
            for name, entry in record["files"].items():
                self._path(name)
                if not isinstance(entry, dict) or set(entry) != {"before", "after"}:
                    raise ValueError()
                self._unpack(entry["before"])
                if self._unpack(entry["after"]) is None:
                    raise ValueError()
            return record
        except (ValueError, TypeError, KeyError, OSError):
            raise RecoveryError("recovery journal unreadable or invalid") from None

    def _validate_current(self, record):
        # Preflight ALL files before changing any target.
        for name, entry in record["files"].items():
            current = self._read(name)
            before = self._unpack(entry["before"])
            after = self._unpack(entry["after"])
            if current != before and current != after:
                raise RecoveryError("ledger differs from transaction states")

    def prepare(self, changes):
        self._check_journal_path()
        if self.journal.exists():
            raise RecoveryError("pending journal must be recovered first")
        if not isinstance(changes, dict) or not changes:
            raise RecoveryError("nonempty changes required")
        files = {}
        for name, data in changes.items():
            self._path(name)
            if not isinstance(data, bytes):
                raise RecoveryError("target payload must be bytes")
            files[name] = {
                "before": self._pack(self._read(name)),
                "after": self._pack(data),
            }
        record = {
            "version": 1, "id": uuid.uuid4().hex,
            "state": "prepared", "files": files,
        }
        atomic_write_json(self.journal, record)
        return record["id"]

    def apply_one(self, name):
        record = self._load()
        if record["state"] != "prepared" or name not in record["files"]:
            raise RecoveryError("invalid apply operation")
        self._validate_current(record)
        data = self._unpack(record["files"][name]["after"])
        atomic_write_bytes(self._path(name), data)

    def commit(self):
        record = self._load()
        self._validate_current(record)
        for name, entry in record["files"].items():
            if self._read(name) != self._unpack(entry["after"]):
                raise RecoveryError("cannot commit incomplete transaction")
        record["state"] = "committed"
        atomic_write_json(self.journal, record)

    def recover(self):
        self._check_journal_path()
        if not self.journal.exists():
            return "idle"
        record = self._load()
        self._validate_current(record)
        field = "after" if record["state"] == "committed" else "before"
        for name, entry in record["files"].items():
            expected = self._unpack(entry[field])
            if self._read(name) == expected:
                continue
            path = self._path(name)
            if expected is None:
                path.unlink()
            else:
                atomic_write_bytes(path, expected)
        for name, entry in record["files"].items():
            if self._read(name) != self._unpack(entry[field]):
                raise RecoveryError("recovery verification failed")
        self.journal.unlink()
        return "committed" if field == "after" else "rolled_back"