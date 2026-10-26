# -*- coding: utf-8 -*-
"""GuanLan v4.3 daily reconciliation (22b R3).
Mechanical integrity checks; standalone-runnable now, AutoScheduler mount planned with 22a.

Checks:
  T1 funding triangle : cash + active position cost == capital + realized PnL (tol 0.01).
       Assumes complete trade history, fee-inclusive costs/PnL, and a reconciled
       capital anchor. External cash flows must be reconciled separately.
  T2 replay sync      : per symbol, sum(buy shares) - sum(sell shares) == held shares (or 0)
  T3 staleness        : account.updated older than 10 days -> status WARN + manual-verify note

Honest boundary: external cash flows into the brokerage account (the 580.8-type event) are
NOT detectable from inside the ledger. Going forward they enter via cash_events (R1 schema)
plus the Agent's diary cross-check. Mechanical reconciliation guards internal consistency only.

Exit code: 0 = PASS/WARN, 1 = FAIL (T1 or T2 broken).
Usage: python daily_reconcile.py
Design: 瑶序 2026-09-03 | Evidence: replay audit 瑶序/2026-09-03-08_23_01.txt
"""
import json, sys
from pathlib import Path
from datetime import date, datetime

BASE = Path(__file__).parent
TOL = 0.01
STALE_DAYS = 10

def load(p):
    return json.loads(p.read_text(encoding="utf-8")) if p.exists() else None

def _main_locked():
    account = load(BASE / "account.json")
    positions = load(BASE / "positions.json")
    trades = load(BASE / "trades.json")
    import math

    def number(value, positive=False):
        if (isinstance(value, bool) or not isinstance(value, (int, float))
                or not math.isfinite(value) or (positive and value <= 0)):
            raise ValueError("invalid reconciliation numeric field")
        return value

    if (not isinstance(account, dict)
            or not isinstance(positions, dict)
            or not isinstance(positions.get("positions"), list)
            or not isinstance(trades, list)):
        raise ValueError("missing or invalid reconciliation ledgers")
    number(account.get("available_cash"))
    if number(account.get("total_capital")) < 0:
        raise ValueError("invalid capital anchor")
    for position in positions["positions"]:
        if (not isinstance(position, dict)
                or not isinstance(position.get("symbol"), str)
                or not position["symbol"]
                or position.get("status") not in ("active", "closed")):
            raise ValueError("invalid reconciliation position")
        if position["status"] == "active":
            quantity = position.get("shares")
            if isinstance(quantity, bool) or not isinstance(quantity, int) or quantity <= 0:
                raise ValueError("invalid reconciliation position quantity")
            number(position.get("cost"), positive=True)
    for trade in trades:
        if not isinstance(trade, dict):
            raise ValueError("invalid reconciliation trade row")
        if trade.get("action") not in ("buy", "sell"):
            continue
        quantity = trade.get("shares")
        if (not isinstance(trade.get("symbol"), str) or not trade["symbol"]
                or isinstance(quantity, bool) or not isinstance(quantity, int)
                or quantity <= 0):
            raise ValueError("invalid reconciliation trade identity or quantity")
        if trade["action"] == "sell":
            number(trade.get("pnl"))

    r = {"run_date": str(date.today()), "checks": {}}
    fails = []

    # T1 funding triangle
    if account:
        pos_cost = sum(
            p["cost"] * p["shares"]
            for p in positions.get("positions", [])
            if p.get("status") == "active")
        realized = sum(t["pnl"] for t in trades if t.get("action") == "sell")
        capital = account["total_capital"]
        lhs = account["available_cash"] + pos_cost
        rhs = capital + realized
        ok = abs(lhs - rhs) <= TOL
        r["checks"]["T1_triangle"] = {
            "pass": ok, "cash": account["available_cash"],
            "position_cost": round(pos_cost, 2),
            "total_capital": capital, "realized_pnl": round(realized, 2),
            "expected_book_equity": round(rhs, 2),
            "diff": round(rhs - lhs, 2),
            "scope": "完整交易历史、含费成本和已核对本金；不证明外部资金流完整"}
        if not ok:
            fails.append("T1")
    else:
        r["checks"]["T1_triangle"] = {"pass": False, "error": "account.json missing"}
        fails.append("T1")

    # T2 replay sync
    flows = {}
    for t in trades:
        action = t.get("action")
        if action not in ("buy", "sell"):
            continue
        s = t["symbol"]
        flows[s] = flows.get(s, 0) + (
            t["shares"] if action == "buy" else -t["shares"])
    pos_map = {}
    for p in positions.get("positions", []):
        if p.get("status") == "active":
            s = p["symbol"]
            pos_map[s] = pos_map.get(s, 0) + p["shares"]
    detail, ok_all = {}, True
    for s, net in flows.items():
        held = pos_map.get(s, 0)
        ok = (net == held)
        ok_all &= ok
        detail[s] = {"replay_net": net, "held": held, "pass": ok}
    for s, held in pos_map.items():
        if s not in flows:
            ok_all = False
            detail[s] = {"replay_net": 0, "held": held, "pass": False,
                         "note": "position without any trade history row"}
    r["checks"]["T2_replay_sync"] = {"pass": ok_all, "symbols": detail}
    if not ok_all:
        fails.append("T2")

    # T3 staleness (informational)
    stale = False
    if account and account.get("updated"):
        try:
            upd = datetime.strptime(account["updated"], "%Y-%m-%d").date()
            age = (date.today() - upd).days
            stale = age > STALE_DAYS
            r["checks"]["T3_staleness"] = {"updated": account["updated"], "age_days": age,
                                           "level": "WARN" if stale else "fresh",
                                           "note": ("ledger not written for >%d days; if capital moved "
                                                    "outside trades (cash_events expected), verify manually"
                                                    % STALE_DAYS) if stale else "fresh"}
        except ValueError:
            r["checks"]["T3_staleness"] = {"updated": account.get("updated"), "note": "unparseable date"}
    else:
        r["checks"]["T3_staleness"] = {"note": "no updated field"}

    r["status"] = "FAIL" if fails else ("WARN" if stale else "PASS")
    print(json.dumps(r, ensure_ascii=False, indent=2))
    sys.exit(1 if fails else 0)

def main():
    from filelock import FileLock
    from real_ledger import access
    paths = (
        BASE / "positions.json", BASE / "trades.json", BASE / "account.json")
    lock = FileLock(str(BASE / "guanlan.lock"), timeout=60)
    # Recover before reading; hold the writer's lock across all checks.
    # No account initialization or ledger correction is performed here.
    with access(paths, lock):
        return _main_locked()


if __name__ == "__main__":
    main()