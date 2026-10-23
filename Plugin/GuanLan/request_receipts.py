"""Booking receipts stored INSIDE the transactional account document.

Callers supply only normalized business arguments, never raw commands,
environment variables or credentials. No IO, pruning or implicit IDs.
"""
import copy
import hashlib
import json
import re

FIELD = "_booking_receipts_v1"

class ReceiptError(ValueError):
    pass

class ReceiptConflict(ReceiptError):
    """A previously committed request ID has different business arguments."""
    pass

def request_key(request_id):
    if request_id is None:
        return None
    if (not isinstance(request_id, str)
            or not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9_.:-]{0,127}", request_id)):
        raise ReceiptError("invalid request_id")
    return request_id

def fingerprint(operation, arguments):
    if not isinstance(operation, str) or not operation:
        raise ReceiptError("operation required")
    if not isinstance(arguments, dict):
        raise ReceiptError("business arguments must be an object")
    try:
        payload = json.dumps(
            {"operation": operation, "arguments": arguments},
            sort_keys=True, ensure_ascii=False, allow_nan=False,
            separators=(",", ":")).encode("utf-8")
    except (ValueError, TypeError, OverflowError):
        raise ReceiptError("business arguments are not valid JSON") from None
    return hashlib.sha256(payload).hexdigest()

def _receipts(account):
    if not isinstance(account, dict):
        raise ReceiptError("account must be an object")
    receipts = account.get(FIELD, {})
    if not isinstance(receipts, dict):
        raise ReceiptError("receipt ledger invalid")
    return receipts

def lookup(account, request_id, digest):
    key = request_key(request_id)
    if key is None:
        return None
    ledger = _receipts(account)
    if key not in ledger:
        return None
    entry = ledger[key]
    if (not isinstance(entry, dict)
            or set(entry) != {"digest", "result"}
            or not isinstance(entry["digest"], str)
            or not re.fullmatch(r"[0-9a-f]{64}", entry["digest"])
            or not isinstance(entry["result"], dict)):
        raise ReceiptError("receipt record invalid")
    try:
        json.dumps(entry["result"], allow_nan=False)
    except (TypeError, ValueError, OverflowError):
        raise ReceiptError("receipt result invalid") from None
    if entry["digest"] != digest:
        raise ReceiptConflict("request_id already used for different booking")
    return copy.deepcopy(entry["result"])

def record(account, request_id, digest, result):
    """Return a copied account; caller MUST stage it with booking changes."""
    key = request_key(request_id)
    if key is None:
        return copy.deepcopy(account)
    if (not isinstance(digest, str)
            or not re.fullmatch(r"[0-9a-f]{64}", digest)):
        raise ReceiptError("invalid booking fingerprint")
    if not isinstance(result, dict):
        raise ReceiptError("receipt result must be an object")
    existing = lookup(account, key, digest)
    if existing is not None:
        if existing != result:
            raise ReceiptError("receipt result cannot be replaced")
        return copy.deepcopy(account)
    try:
        json.dumps(result, allow_nan=False)
    except (TypeError, ValueError, OverflowError):
        raise ReceiptError("receipt result is not valid JSON") from None
    updated = copy.deepcopy(account)
    receipts = copy.deepcopy(_receipts(account))
    receipts[key] = {"digest": digest, "result": copy.deepcopy(result)}
    updated[FIELD] = receipts
    return updated