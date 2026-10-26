# -*- coding: utf-8 -*-
"""GuanLan 22d L2 data layer: per-date K-line matrix (raw daily + adj_factor).

复权铁律 (瑶序 2026-08-27 调研, 22d三必答题之一):
  底层存不复权原价 + 复权因子, 应用层(tech_check)动态计算复权价 - 不用黑盒前复权接口.
  daily      -> kline_daily_YYYYMMDD.json  (不复权 OHLC + pre_close)
  adj_factor -> kline_adj_YYYYMMDD.json    (累计复权因子)

停牌铁律: 停牌股当日无 daily 行 -> tech_check 的 inner join 自然剔除.
  实证 (2026-09-06 probe): adj_factor 5556 行 > daily 5548 行, 差值=停牌股(有因子无行情).

pre_close 红利: pre_close != 前收 即除权除息日 (将来反查复权因子的交叉验证工具).

Design: market_snapshot.py 同款哲学 - 按日文件+水位线+幂等+skip对账(r6)+双流reconfigure(r7b).
--backfill: 自动拉 trade_cal 生成交易日清单 (参数硬隔离: 清单派生, 不手打日期).

Usage:
  python kline_snapshot.py 20260904                      # 指定日期
  python kline_snapshot.py --backfill 20260506 20260904  # 交易日历驱动的区间回补
"""
import json, sys, time
from pathlib import Path
from datetime import datetime

sys.stdout.reconfigure(encoding='utf-8', errors='replace')
sys.stderr.reconfigure(encoding='utf-8', errors='replace')

BASE = Path(__file__).parent
DATA_DIR = BASE / "market_data"
STATE_FILE = DATA_DIR / "kline_state.json"

FIELDS_DAILY = 'ts_code,open,high,low,close,pre_close,vol,amount'  # 原价, 不复权
FIELDS_ADJ = 'ts_code,adj_factor'                                  # 累计复权因子
PACING = 0.35  # 秒/调用

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
    from ledger_io import atomic_write_json
    atomic_write_json(STATE_FILE, state)

def pull_one(api, api_name, params, fields):
    """None 重试1次; 再 None 返回 None."""
    for attempt in (1, 2):
        r = api(api_name, params, fields)
        if r is not None:
            return r
        if attempt == 1:
            time.sleep(1.0)
    return None

def snapshot_kline(trade_date, api):
    """Validate both streams before saving; each file replacement is atomic."""
    import math
    from ledger_io import atomic_write_json

    def validate(document, kind, cached=False):
        if not isinstance(document, dict):
            raise ValueError("snapshot must be an object")
        fields, items = document.get("fields"), document.get("items")
        required = ("ts_code", "close", "vol") if kind == "daily" else (
            "ts_code", "adj_factor")
        if (not isinstance(fields, list)
                or any(not isinstance(f, str) for f in fields)
                or len(set(fields)) != len(fields)
                or not set(required).issubset(fields)
                or not isinstance(items, list) or not items):
            raise ValueError("invalid or empty snapshot schema")
        if cached and document.get("_meta", {}).get("trade_date") != trade_date:
            raise ValueError("cached date mismatch")
        codes = set()
        for values in items:
            if not isinstance(values, list) or len(values) != len(fields):
                raise ValueError("invalid snapshot row")
            row = dict(zip(fields, values))
            code = row["ts_code"]
            if not isinstance(code, str) or not code or code in codes:
                raise ValueError("invalid or duplicate symbol")
            codes.add(code)
            numeric = ("close", "vol") if kind == "daily" else ("adj_factor",)
            for key in numeric:
                value = row[key]
                if (isinstance(value, bool) or not isinstance(value, (int, float))
                        or not math.isfinite(value)
                        or (value < 0 if key == "vol" else value <= 0)):
                    raise ValueError("invalid snapshot numeric value")
        return codes

    f_daily = DATA_DIR / f"kline_daily_{trade_date}.json"
    f_adj = DATA_DIR / f"kline_adj_{trade_date}.json"
    try:
        if f_daily.exists() and f_adj.exists():
            rd = json.loads(f_daily.read_text(encoding="utf-8"))
            ra = json.loads(f_adj.read_text(encoding="utf-8"))
            daily_codes = validate(rd, "daily", cached=True)
            adj_codes = validate(ra, "adj", cached=True)
            if not daily_codes.issubset(adj_codes):
                raise ValueError("cached adjustment coverage incomplete")
            return {"status": "skip", "trade_date": trade_date}
        if f_daily.exists() or f_adj.exists():
            raise ValueError("incomplete cached pair; manual verification required")
        rd = pull_one(api, "daily", {"trade_date": trade_date}, FIELDS_DAILY)
        time.sleep(PACING)
        ra = pull_one(api, "adj_factor", {"trade_date": trade_date}, FIELDS_ADJ)
        time.sleep(PACING)
        daily_codes = validate(rd, "daily")
        adj_codes = validate(ra, "adj")
        if not daily_codes.issubset(adj_codes):
            raise ValueError("adjustment coverage incomplete")
        payloads = []
        for kind, document in (("daily", rd), ("adj", ra)):
            payloads.append({
                "_meta": {
                    "fetched_at": datetime.now().isoformat(timespec="seconds"),
                    "trade_date": trade_date, "rows": len(document["items"]),
                    "source": "tushare " + (
                        "daily" if kind == "daily" else "adj_factor"),
                    "units": ({"ohlc": "元(不复权原价)", "pre_close": "元"}
                              if kind == "daily" else {"adj_factor": "倍"}),
                },
                "fields": document["fields"], "items": document["items"],
            })
        DATA_DIR.mkdir(exist_ok=True)
        atomic_write_json(f_daily, payloads[0])
        atomic_write_json(f_adj, payloads[1])
        return {"status": "ok", "trade_date": trade_date,
                "daily_rows": len(rd["items"]), "adj_rows": len(ra["items"])}
    except (ValueError, TypeError, KeyError, AttributeError, OSError):
        return {"status": "fail", "trade_date": trade_date,
                "reason": "snapshot validation or persistence failed; existing files preserved where possible"}

def cal_open_days(api, start, end):
    r = api('trade_cal', {'start_date': start, 'end_date': end}, 'exchange,cal_date,is_open')
    if r is None:
        sys.exit("trade_cal FAIL (None) - 无法派生交易日清单, 中止 (不手打日期)")
    items = r.get('items') or []
    return sorted(it[1] for it in items if it[2] == 1)

def main():
    args = sys.argv[1:]
    api = _get_api()
    if '--backfill' in args:
        i = args.index('--backfill')
        if len(args) < i + 3:
            sys.exit("--backfill needs START END, e.g. --backfill 20260506 20260904")
        start, end = args[i + 1], args[i + 2]
        dates = cal_open_days(api, start, end)
        if not dates:
            sys.exit("trade calendar contains no confirmed open days")
        print(f"calendar: {len(dates)} trading days, {dates[0]}..{dates[-1]}",
              file=sys.stderr, flush=True)
    else:
        dates = [a for a in args if not a.startswith('--')]
        if not dates:
            sys.exit("need dates or --backfill START END")
    state = load_state()
    results = {"ok": 0, "skip": 0, "fail": 0, "fails": []}
    advanced = False
    for d in dates:
        r = snapshot_kline(d, api)
        results[r["status"]] += 1
        if r["status"] == "fail":
            results["fails"].append({"date": d, "reason": r.get("reason")})
        if r["status"] in ("ok", "skip") and d not in state["pulled_dates"]:
            state["pulled_dates"].append(d)  # skip也reconcile (r6, 文件系统为truth)
            advanced = True
    if advanced:
        save_state(state)
    results["watermark_count"] = len(state["pulled_dates"])
    print(json.dumps(results, ensure_ascii=False, indent=1))
    if results["fail"]:
        sys.exit(1)

if __name__ == '__main__':
    main()