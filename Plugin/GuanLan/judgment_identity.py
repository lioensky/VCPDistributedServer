"""Shared judgment identity; no IO or automatic historical migration."""
import json
import re
from datetime import datetime, timezone, timedelta

_ID = re.compile(r"[A-Za-z0-9][A-Za-z0-9_.:-]{0,127}")


def explicit_id(row):
    if "judgment_id" not in row:
        return None
    value = row["judgment_id"]
    if not isinstance(value, str) or not _ID.fullmatch(value):
        raise ValueError("invalid judgment_id")
    return value


def scope(row, result=False):
    return (
        str(row.get("symbol") or ""),
        str(row.get("window_end" if result else "time_window_end") or ""),
        str(row.get("model_version") or ""),
    )


def key(row, result=False):
    identity = explicit_id(row)
    return (("id", identity) if identity is not None
            else ("legacy",) + scope(row, result))


def _instant(row):
    stamp = datetime.fromisoformat(row["timestamp"])
    if stamp.tzinfo is None:
        stamp = stamp.replace(tzinfo=timezone(timedelta(hours=8)))
    return stamp


def select_judgments(rows):
    """Explicit independent samples survive; only explicit corrections replace.

    Legacy rows retain the existing latest-timestamp rule. A correction must
    reference an explicit ID already present in this ledger, never free text.
    """
    identified, legacy = {}, {}
    for row in rows:
        identity = explicit_id(row)
        if identity is None:
            if "corrects" in row:
                raise ValueError("correction requires its own judgment_id")
            marker = key(row)
            if (marker not in legacy
                    or str(row.get("timestamp", ""))
                    >= str(legacy[marker].get("timestamp", ""))):
                legacy[marker] = row
            continue
        # Canonical serialization also rejects nonfinite data.
        canonical = json.dumps(row, sort_keys=True, allow_nan=False)
        if identity in identified:
            previous = json.dumps(
                identified[identity], sort_keys=True, allow_nan=False)
            if canonical != previous:
                raise ValueError("conflicting duplicate judgment_id")
        identified[identity] = row

    replaced = {}
    for identity, row in identified.items():
        if "corrects" not in row:
            continue
        parent = row["corrects"]
        if (not isinstance(parent, str) or parent == identity
                or parent not in identified):
            raise ValueError("correction target missing or invalid")
        original = identified[parent]
        if scope(row) != scope(original):
            raise ValueError("correction scope differs")
        if row.get("agent") != original.get("agent"):
            raise ValueError("correction agent differs")
        if _instant(row) < _instant(original):
            raise ValueError("correction timestamp precedes original")
        if parent in replaced and replaced[parent] != identity:
            raise ValueError("branching corrections refused")
        replaced[parent] = identity

    for identity in identified:
        seen, cursor = set(), identity
        while cursor in replaced:
            if cursor in seen:
                raise ValueError("cyclic corrections refused")
            seen.add(cursor)
            cursor = replaced[cursor]

    selected = dict(legacy)
    selected.update({
        key(row): row for identity, row in identified.items()
        if identity not in replaced})
    return selected


def result_index(rows):
    indexed = {}
    for row in rows:
        marker = key(row, result=True)
        if marker in indexed and marker[0] == "id":
            previous = indexed[marker]
            if scope(previous, True) != scope(row, True):
                raise ValueError("result identity scope conflict")
            fields = ("actual_direction", "actual_return", "close_price")
            if any(previous.get(f) != row.get(f) for f in fields):
                raise ValueError("conflicting outcomes for judgment_id")
        if (marker not in indexed
                or str(row.get("timestamp", ""))
                >= str(indexed[marker].get("timestamp", ""))):
            indexed[marker] = row
    return indexed


def matching_result(judgment, indexed):
    marker = key(judgment)
    result = indexed.get(marker)
    if marker[0] == "id":
        if result is not None and scope(judgment) != scope(result, True):
            raise ValueError("judgment/result identity scope mismatch")
        return result
    paper = (
        str(judgment.get("model_version") or "").startswith("paper-")
        or judgment.get("source") == "paper-trade"
        or str(judgment.get("state") or "").startswith("paper_"))
    if result is None and not paper:
        result = indexed.get(("legacy",) + scope(judgment)[:2] + ("",))
    if paper and result is not None and not result.get("model_version"):
        return None
    return result