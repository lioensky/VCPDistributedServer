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
    STATE_FILE.write_text(json.dumps(state, ensure_ascii=False, indent=1), encoding='utf-8')

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
    """双文件齐备 -> skip (幂等); 拉取失败保旧不推进."""
    f_daily = DATA_DIR / f"kline_daily_{trade_date}.json"
    f_adj = DATA_DIR / f"kline_adj_{trade_date}.json"
    if f_daily.exists() and f_adj.exists():
        return {"status": "skip", "trade_date": trade_date}
    DATA_DIR.mkdir(exist_ok=True)
    rd = pull_one(api, 'daily', {'trade_date': trade_date}, FIELDS_DAILY)
    time.sleep(PACING)
    ra = pull_one(api, 'adj_factor', {'trade_date': trade_date}, FIELDS_ADJ)
    time.sleep(PACING)
    if rd is None or ra is None:
        return {"status": "fail", "trade_date": trade_date,
                "reason": f"daily={'None' if rd is None else 'ok'}, adj_factor={'None' if ra is None else 'ok'}"}
    d_items = rd.get('items') or []
    a_items = ra.get('items') or []
    if not d_items:
        return {"status": "fail", "trade_date": trade_date, "reason": "daily empty (非交易日?)"}
    f_daily.write_text(json.dumps(
        {"_meta": {"fetched_at": datetime.now().isoformat(timespec='seconds'),
                    "trade_date": trade_date, "rows": len(d_items),
                    "units": {"ohlc": "元(不复权原价)", "pre_close": "元(前收, 除权探测器)"},
                    "source": "tushare daily"},
         "fields": rd.get('fields', []), "items": d_items}, ensure_ascii=False), encoding='utf-8')
    f_adj.write_text(json.dumps(
        {"_meta": {"fetched_at": datetime.now().isoformat(timespec='seconds'),
                    "trade_date": trade_date, "rows": len(a_items),
                    "units": {"adj_factor": "倍(累计复权因子)"},
                    "source": "tushare adj_factor"},
         "fields": ra.get('fields', []), "items": a_items}, ensure_ascii=False), encoding='utf-8')
    return {"status": "ok", "trade_date": trade_date,
            "daily_rows": len(d_items), "adj_rows": len(a_items)}

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
        print(f"calendar: {len(dates)} trading days, {dates[0]}..{dates[-1]}", flush=True)
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

if __name__ == '__main__':
    main()