# -*- coding: utf-8 -*-
"""GuanLan 22d L0: daily market snapshot (22d data foundation).
Single responsibility: fetch + store + watermark. NO filtering - that is L1's job.

Design (瑶序 2026-09-06):
- Raw JSON snapshots (fields+items as-returned) - no pre-transform, evidence chain preserved;
  L1/L2/L3 parse on demand.
- Fail-silent-keep-old: pull failure does NOT advance watermark; never advance on partial data.
- Delisted registry: separate file, full pull each run (delisting is low-frequency; delta
  vs prev count reported). Survivorship-bias guard lives HERE at L0.
- API contract (verified 2026-09-06 live): daily_basic returns {'fields': [...], 'items': [[...]]}
  with adapter already unwrapped (main.py L209-225); rows sorted by ts_code; total_mv in 万元.
- 5548 rows incl. Beijing exchange < single-call cap 6000 -> one call per trade date.

Usage:
  python market_snapshot.py 20260904        # explicit trade date(s)
  python market_snapshot.py                 # default: today (fails honestly on non-trading days)
"""
import json, sys
from pathlib import Path
from datetime import datetime

sys.stdout.reconfigure(encoding='utf-8', errors='replace')  # r7: GBK console mojibake guard (test_harvest_spec.py precedent 2026-09-02)
sys.stderr.reconfigure(encoding='utf-8', errors='replace')  # r7b: sys.exit() messages go to STDERR - the actual mojibake culprit (diagnosis v2 2026-09-06)

BASE = Path(__file__).parent
DATA_DIR = BASE / "market_data"
STATE_FILE = DATA_DIR / "market_state.json"
DELISTED_FILE = DATA_DIR / "delisted_stocks.json"

FIELDS_DAILY = 'ts_code,close,total_mv,circ_mv,pe'   # v2 2026-09-06: circ_mv added (观澜裁定一 - 流通市值为主口径); close=元, total_mv/circ_mv=万元, pe=倍

def _get_api():
    import importlib.util
    spec = importlib.util.spec_from_file_location('gl', BASE / 'main.py')
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m._tushare_api

def load_state():
    if STATE_FILE.exists():
        try:
            return json.loads(STATE_FILE.read_text(encoding='utf-8'))
        except (json.JSONDecodeError, OSError):
            pass
    return {"pulled_dates": []}

def save_state(state):
    DATA_DIR.mkdir(exist_ok=True)
    STATE_FILE.write_text(json.dumps(state, ensure_ascii=False, indent=1), encoding='utf-8')

def snapshot(trade_date, api):
    DATA_DIR.mkdir(exist_ok=True)  # L0 fix 2026-09-06: mkdir previously only in save_state/refresh_delisted which run AFTER snapshot - first-run ordering crash
    out_file = DATA_DIR / f"daily_basic_{trade_date}.json"
    if out_file.exists():
        return {"status": "skip", "reason": "already pulled", "file": out_file.name}
    r = api('daily_basic', {'trade_date': trade_date}, FIELDS_DAILY)
    if r is None:
        return {"status": "fail", "reason": "api returned None (auth/network, see log)", "trade_date": trade_date}
    items = r.get('items') or []
    if not items:
        return {"status": "fail", "reason": "empty items (non-trading day or auth issue)", "trade_date": trade_date}
    payload = {"_meta": {"fetched_at": datetime.now().isoformat(timespec='seconds'),
                          "trade_date": trade_date, "rows": len(items),
                          "units": {"close": "元", "total_mv": "万元", "circ_mv": "万元", "pe": "倍"},  # r7: circ_mv added; note: 16 historical snapshots (pre-20260906) lack this key - fields array is authoritative
                          "source": "tushare daily_basic"},
               "fields": r.get('fields', []),
               "items": items}
    out_file.write_text(json.dumps(payload, ensure_ascii=False), encoding='utf-8')
    return {"status": "ok", "rows": len(items), "file": out_file.name}

def refresh_delisted(api):
    prev = 0
    if DELISTED_FILE.exists():
        try:
            prev = json.loads(DELISTED_FILE.read_text(encoding='utf-8')).get('_meta', {}).get('rows', 0)
        except (json.JSONDecodeError, OSError):
            pass
    r = api('stock_basic', {'list_status': 'D'}, 'ts_code,name,list_date,delist_date')
    if r is None:
        return {"status": "fail", "reason": "api returned None", "prev_rows": prev}
    items = r.get('items') or []
    if not items:
        return {"status": "fail", "reason": "empty items", "prev_rows": prev}
    payload = {"_meta": {"fetched_at": datetime.now().isoformat(timespec='seconds'),
                          "rows": len(items), "source": "tushare stock_basic list_status=D"},
               "fields": r.get('fields', []),
               "items": items}
    DATA_DIR.mkdir(exist_ok=True)
    DELISTED_FILE.write_text(json.dumps(payload, ensure_ascii=False), encoding='utf-8')
    return {"status": "ok", "rows": len(items), "prev_rows": prev, "delta": len(items) - prev}

def main():
    dates = [a for a in sys.argv[1:] if not a.startswith('--')]
    api = _get_api()
    if not dates:
        dates = [datetime.now().strftime('%Y%m%d')]
    state = load_state()
    results = {}
    advanced = False
    for d in dates:
        r = snapshot(d, api)
        results[f"snapshot_{d}"] = r
        if r.get('status') in ('ok', 'skip') and d not in state['pulled_dates']:
            # Nova r6 fix: skip (file exists) also reconciles into watermark - filesystem is truth, watermark catches up
            state['pulled_dates'].append(d)
            advanced = True
    if advanced:
        save_state(state)
    results['delisted'] = refresh_delisted(api)
    results['watermark'] = {"pulled_dates": state['pulled_dates']}
    print(json.dumps(results, ensure_ascii=False, indent=1))

if __name__ == '__main__':
    main()