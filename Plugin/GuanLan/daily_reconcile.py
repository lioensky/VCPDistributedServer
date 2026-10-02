# -*- coding: utf-8 -*-
"""GuanLan v4.3 daily reconciliation (22b R3).
Mechanical integrity checks; standalone-runnable now, AutoScheduler mount planned with 22a.

Checks:
  T1 funding triangle : available_cash + sum(position cost*shares) == total_capital (tol 0.01)
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

def main():
    account = load(BASE / "account.json")
    positions = load(BASE / "positions.json") or {"positions": []}
    trades = load(BASE / "trades.json") or []

    r = {"run_date": str(date.today()), "checks": {}}
    fails = []

    # T1 funding triangle
    if account:
        pos_cost = sum(p.get("cost", 0) * p.get("shares", 0) for p in positions.get("positions", []))
        lhs = account.get("available_cash", 0) + pos_cost
        rhs = account.get("total_capital", 0)
        ok = abs(lhs - rhs) <= TOL
        r["checks"]["T1_triangle"] = {"pass": ok, "cash": account.get("available_cash"),
                                      "position_cost": round(pos_cost, 2),
                                      "total_capital": rhs, "diff": round(rhs - lhs, 2)}
        if not ok:
            fails.append("T1")
    else:
        r["checks"]["T1_triangle"] = {"pass": False, "error": "account.json missing"}
        fails.append("T1")

    # T2 replay sync
    flows = {}
    for t in trades:
        s = t.get("symbol")
        flows[s] = flows.get(s, 0) + (t.get("shares", 0) if t.get("action") == "buy" else -t.get("shares", 0))
    pos_map = {p.get("symbol"): p.get("shares", 0) for p in positions.get("positions", [])}
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

if __name__ == "__main__":
    main()