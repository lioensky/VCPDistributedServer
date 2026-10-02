# -*- coding: utf-8 -*-
"""GuanLan 22d L1 v2: market-cap filter over L0 snapshots.
PRIMARY口径: circ_mv (流通市值, 观澜裁定一 2026-09-06) - 流动性/操纵/覆盖三风险由实际可交易盘决定;
total_mv kept as REFERENCE column only.
BJ excluded (观澜裁定二: 权限50万资产门槛 vs 账户1.4万, 物理不可达; 以券商实际权限为准, 可捞回).

v2 changes (瑶序 2026-09-06, per 观澜三裁定 + Nova r6):
- circ_mv primary threshold; requires v2 snapshots (5-field, incl. circ_mv)
- BJ exclusion with ruling note in meta
- None counting into meta (Nova r6 finding-1 defensive): none_circ_mv explicitly reported
- output filename encodes threshold: screened_{date}_circ{N}.json (Nova r6: rerun never evaporates old results)
- CLI: --min-mv N or --min-mv=N, value sanity-checked (0 < N <= 100000 亿)

Usage:
  python market_filter.py 20260904 --stats
  python market_filter.py 20260904 --min-mv 80
阈值80亿出处 (溯源规矩 2026-09-03翔立): 数据驱动选定非拍脑 — 9/6全市场分布实测:
P50=60.1亿(半数A股低于此), 敏感度表80亿档唯一命中观澜8/17"5400→2000+"目标(keep 2211
total口径/circ口径1949, 观澜9/6签字维持), 且为观澜实际操作区间远下限(紫金4000亿/云铝300亿),
漏斗下限取保守. 口径切换时蒸发的262只=流通不足总盘达标的堰塞湖型(裁定一防线收益).
"""
import json, sys
from pathlib import Path
from datetime import datetime

sys.stdout.reconfigure(encoding='utf-8', errors='replace')  # r7: GBK console mojibake guard (test_harvest_spec.py precedent 2026-09-02)
sys.stderr.reconfigure(encoding='utf-8', errors='replace')  # r7b: sys.exit() messages go to STDERR - the actual mojibake culprit (diagnosis v2 2026-09-06)

BASE = Path(__file__).parent
DATA_DIR = BASE / "market_data"

BJ_RULE = {"exclude": True,
           "note": "观澜裁定二 2026-09-06: 北交所权限门槛50万资产量级 vs 账户总资产1.4万, 物理不可达; 若券商权限升级可从delisted标记捞回, 规则成本为零"}

def load_snapshot(trade_date):
    f = DATA_DIR / f"daily_basic_{trade_date}.json"
    if not f.exists():
        sys.exit(f"L0 snapshot missing: {f.name} - run market_snapshot.py {trade_date} first")
    obj = json.loads(f.read_text(encoding='utf-8'))
    flds = obj.get('fields', [])
    if 'circ_mv' not in flds:
        sys.exit(f"snapshot {f.name} is v1 (no circ_mv field) - re-pull with market_snapshot.py v2 first")
    rows = [dict(zip(flds, it)) for it in obj.get('items', [])]
    return rows

def is_bj(row):
    return row.get('ts_code', '').endswith('.BJ')

def cmv_yi(row):  # circ_mv (万元) -> 亿元, PRIMARY
    v = row.get('circ_mv')
    return v / 10000.0 if isinstance(v, (int, float)) else None

def tmv_yi(row):  # total_mv -> 亿元, reference only
    v = row.get('total_mv')
    return v / 10000.0 if isinstance(v, (int, float)) else None

def split_pool(rows):
    """Returns (pool_non_bj, bj_rows). BJ ruled out at pool level."""
    return [r for r in rows if not is_bj(r)], [r for r in rows if is_bj(r)]

def exchange_of(ts_code):
    return ts_code.split('.')[-1] if '.' in ts_code else '??'

def stats_report(trade_date):
    rows = load_snapshot(trade_date)
    pool, bj = split_pool(rows)
    mvs = sorted(cmv_yi(r) for r in pool if cmv_yi(r) is not None)
    n = len(mvs)
    none_circ = sum(1 for r in pool if cmv_yi(r) is None)
    def pct(p): return round(mvs[int(p * (n - 1))], 1) if n else None
    out = {"trade_date": trade_date, "total_rows": len(rows),
           "bj_excluded": len(bj), "pool": len(pool),
           "none_circ_mv_in_pool": none_circ, "with_circ_mv": n,
           "metric": "circ_mv (流通市值, 观澜裁定一)",
           "circ_mv_quantiles_yi": {f"P{int(p*100)}": pct(p) for p in (0.1, 0.25, 0.5, 0.75, 0.9, 0.95)},
           "threshold_sensitivity": {}}
    for th in (20, 30, 50, 80, 100, 150):
        keep = sum(1 for v in mvs if v >= th)
        out["threshold_sensitivity"][f"min_mv_{th}yi"] = {"keep": keep, "drop": n - keep}
    exch = {}
    for r in pool:
        e = exchange_of(r.get('ts_code', ''))
        exch[e] = exch.get(e, 0) + 1
    out["exchange_distribution_non_bj"] = exch
    print(json.dumps(out, ensure_ascii=False, indent=1))

def run_filter(trade_date, min_mv_yi):
    rows = load_snapshot(trade_date)
    pool, bj = split_pool(rows)
    none_circ_rows = [r for r in pool if cmv_yi(r) is None]
    kept = [r for r in pool if (cmv_yi(r) or 0) >= min_mv_yi]
    exch_after = {}
    for r in kept:
        e = exchange_of(r.get('ts_code', ''))
        exch_after[e] = exch_after.get(e, 0) + 1
    payload = {"_meta": {"generated_at": datetime.now().isoformat(timespec='seconds'),
                          "trade_date": trade_date,
                          "source_snapshot": f"daily_basic_{trade_date}.json",
                          "layer": "L1 v2 market-cap filter",
                          "metric_primary": "circ_mv (观澜裁定一 2026-09-06)",
                          "min_circ_mv_yi": min_mv_yi,
                          "total_rows": len(rows),
                          "bj_excluded": len(bj), "bj_rule": BJ_RULE,
                          "pool_non_bj": len(pool),
                          "none_circ_mv_dropped": len(none_circ_rows),
                          "none_note": "无流通市值数据的行按0剔除并计数 (宁缺毋假; Nova r6 finding-1)",
                          "kept": len(kept), "dropped_by_threshold": len(pool) - len(none_circ_rows) - len(kept)},
               "items": kept}
    out_file = DATA_DIR / f"screened_{trade_date}_circ{min_mv_yi:g}.json"
    out_file.write_text(json.dumps(payload, ensure_ascii=False), encoding='utf-8')
    print(json.dumps({"status": "ok", "trade_date": trade_date,
                       "metric": "circ_mv", "min_mv_yi": min_mv_yi,
                       "total": len(rows), "bj_excluded": len(bj),
                       "none_circ_mv_dropped": len(none_circ_rows),
                       "kept": len(kept),
                       "exchange_after": exch_after, "file": out_file.name},
                      ensure_ascii=False, indent=1))

def parse_min_mv(args):
    for i, a in enumerate(args):
        if a.startswith('--min-mv='):
            return float(a.split('=', 1)[1])
        if a == '--min-mv':
            if i + 1 >= len(args):
                sys.exit("--min-mv needs a value (亿元), e.g. --min-mv 80")
            try:
                return float(args[i + 1])
            except ValueError:
                sys.exit(f"--min-mv 值无效: {args[i+1]!r} (需要数字, 如 --min-mv 80)")  # r7: graceful, symmetric with missing-value branch
    return None

def main():
    args = sys.argv[1:]
    if not args:
        sys.exit("need a trade_date, plus --stats or --min-mv N (亿元, circ口径)")
    trade_date = args[0]
    if '--stats' in args:
        stats_report(trade_date)
        return
    min_mv = parse_min_mv(args)
    if min_mv is None:
        sys.exit("need --stats or --min-mv N (亿元, circ口径)")
    if not (0 < min_mv <= 100000):
        sys.exit(f"threshold out of sane range: {min_mv} 亿 (check CLI quoting; Nova r6)")
    run_filter(trade_date, min_mv)

if __name__ == '__main__':
    main()