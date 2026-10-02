# -*- coding: utf-8 -*-
"""GuanLan 22d L2: technical filter over L1 pool using per-date K-line matrix.

复权铁律应用层 (瑶序 2026-08-27): 指标用后复权序列 = close x adj_factor (动态计算);
  展示/参考用原价. 底层kline文件一个字节不改.

技术标准 (R1/R2/R3 + R4 v1.1 观澜已签字 2026-09-06 - R4 17:05签, K=0.8按量比分布P10选定):
  R1 多头排列: MA20 > MA60                (后复权口径)
  R2 站上均线: 最新后复权收盘 >= MA20
  R3 历史充足: 窗口内 >= 60 个交易日       (新股或长期停牌不足 -> 宁缺毋假剔除, 理由注明)
  R4 量能持续: 近5日均量 >= 0.8 × 前20日均量 (基线=最近25日排除近5日, 防自污染)

停牌铁律: inner join - 停牌日无 daily 行, 该日不入该股序列 (Nova 2026-08-27).

Usage:
  python tech_check.py 20260904
"""
import json, sys
from pathlib import Path
from datetime import datetime

sys.stdout.reconfigure(encoding='utf-8', errors='replace')
sys.stderr.reconfigure(encoding='utf-8', errors='replace')

BASE = Path(__file__).parent
DATA_DIR = BASE / "market_data"
MA_FAST, MA_SLOW = 20, 60

def load_matrix(until_date):
    """全部 kline 日期 <= until_date 升序. 返回 (dates_used, {ts_code: [(date, close, factor)]}).
    inner join: 股票须当日有行情(daily)且有因子(adj_factor), 缺任一该日不入序列."""
    d_files = sorted(DATA_DIR.glob("kline_daily_*.json"))
    dates_used, series = [], {}
    for fd in d_files:
        d = fd.stem.split("_")[-1]
        if d > until_date:
            continue
        fa = DATA_DIR / f"kline_adj_{d}.json"
        if not fa.exists():
            continue  # 配对不齐的日期整体跳过 (该日不可计算, 诚实)
        jd = json.loads(fd.read_text(encoding='utf-8'))
        ja = json.loads(fa.read_text(encoding='utf-8'))
        di = {k: i for i, k in enumerate(jd.get('fields', []))}
        ai = {k: i for i, k in enumerate(ja.get('fields', []))}
        closes = {it[di['ts_code']]: it[di['close']] for it in jd.get('items', [])
                  if it[di['close']] is not None}
        factors = {it[ai['ts_code']]: it[ai['adj_factor']] for it in ja.get('items', [])
                   if it[ai['adj_factor']] is not None}
        vols_today = {it[di['ts_code']]: it[di['vol']] for it in jd.get('items', [])
                      if 'vol' in di and it[di['vol']] is not None}
        dates_used.append(d)
        for code, close in closes.items():
            f = factors.get(code)
            if f is not None:
                v = vols_today.get(code)
                series.setdefault(code, []).append((d, close, f, v))  # v1.1 R4: +vol (观澜签字 2026-09-06 K=0.8)
    return dates_used, series

def judge_stock(points):
    """points: 升序 [(date, close_raw, factor, vol)] v1.1四元组. 后复权=close*factor 动态计算; vol供R4."""
    n = len(points)
    if n < MA_SLOW:
        return {'verdict': 'insufficient_history', 'n_days': n,
                'reason': f'窗口内仅{n}个交易日 < {MA_SLOW} (新股或长期停牌, 宁缺毋假)'}
    adj = [c * f for _, c, f, *_ in points]
    ma_f = sum(adj[-MA_FAST:]) / MA_FAST
    ma_s = sum(adj[-MA_SLOW:]) / MA_SLOW
    latest = adj[-1]
    r1, r2 = ma_f > ma_s, latest >= ma_f
    # R4 (v1.1, 观澜签字 2026-09-06: K=0.8 量能枯竭剃刀): 近5日均量 >= 0.8 × 前20日均量
    # 基线防自污染: 前20日 = 最近25日中排除最近5日 (观澜探针同款构造)
    vols = [v for *_, v in points if v is not None]
    vol_ratio = None  # 23f: 结构化量比字段(排序供数据), 原先只埋在reason文字里
    if len(vols) >= 25:
        v5 = sum(vols[-5:]) / 5
        v20p = sum(vols[-25:-5]) / 20
        if v20p <= 0:
            r4, r4_note = False, "前20日均量为0(长期停牌或数据缺失)"
        else:
            vol_ratio = round(v5 / v20p, 3)
            r4, r4_note = v5 >= 0.8 * v20p, f"量比{v5/v20p:.3f} vs 0.8 (5日均量/前20日均量)"
    else:
        r4, r4_note = False, f"量数据不足{len(vols)}/25"
    if r1 and r2 and r4:
        verdict = 'pass'
        reason = f"多头排列 MA20={ma_f:.3f}>MA60={ma_s:.3f}; 站上MA20 ({latest:.3f}>={ma_f:.3f}); {r4_note} [后复权]"
    else:
        verdict = 'fail'
        fails = []
        if not r1:
            fails.append(f"MA20={ma_f:.3f}<=MA60={ma_s:.3f} 非多头排列")
        if not r2:
            fails.append(f"收盘{latest:.3f}<MA20={ma_f:.3f} 跌破均线")
        if not r4:
            fails.append(f"R4量能: {r4_note}")
        reason = "; ".join(fails)
    return {'verdict': verdict, 'n_days': n, 'reason': reason,
            'ma20': round(ma_f, 4), 'ma60': round(ma_s, 4),
            'latest_adj_close': round(latest, 4), 'latest_raw_close': points[-1][1],
            'vol_ratio': vol_ratio}  # 23f fix: 算了没输出是批1的bug, 本笔出列

def main():
    args = sys.argv[1:]
    if not args:
        sys.exit("need trade_date, e.g. python tech_check.py 20260904")
    date = args[0]
    src = DATA_DIR / f"screened_{date}_circ80.json"
    if not src.exists():
        sys.exit(f"L1 output missing: {src.name}")
    pool = json.loads(src.read_text(encoding='utf-8'))['items']
    dates_used, series = load_matrix(date)
    if len(dates_used) < MA_SLOW:
        sys.exit(f"kline matrix only {len(dates_used)} days (< {MA_SLOW}) - run kline_snapshot.py --backfill first")
    results, stats = [], {'pass': 0, 'fail': 0, 'insufficient_history': 0, 'no_data': 0}
    for row in pool:
        code = row['ts_code']
        pts = series.get(code)
        if not pts:
            results.append({'ts_code': code, 'verdict': 'no_data',
                            'reason': 'kline矩阵无数据 (L1有票但K线无行, 数据一致性信号)'})
            stats['no_data'] += 1
            continue
        res = judge_stock(pts)
        stats[res['verdict']] += 1
        results.append({'ts_code': code, **res})
    passed = [r for r in results if r['verdict'] == 'pass']
    out = {"_meta": {"generated_at": datetime.now().isoformat(timespec='seconds'),
                      "trade_date": date, "source_pool": src.name, "pool": len(pool),
                      "kline_days_used": len(dates_used),
                      "kline_window": f"{dates_used[0]}..{dates_used[-1]}",
                      "criteria": {"R1": "MA20>MA60 多头排列(后复权)",
                                    "R2": "最新收盘>=MA20",
                                    "R3": "窗口>=60交易日(新股/长停宁缺毋假)",
                                    "R4": "近5日均量>=0.8×前20日均量(量能枯竭剃刀, K=0.8按量比分布P10选定)"},
                      "criteria_status": "R1/R2/R3+R4(v1.1) 观澜签字 2026-09-06 (R4 17:05签)",
                      "adjust_method": "后复权=close*adj_factor 动态计算, 底层原价不动 (复权铁律)",
                      "stats": stats},
           "items": passed,
           "all_results": results}
    out_file = DATA_DIR / f"tech_passed_{date}.json"
    out_file.write_text(json.dumps(out, ensure_ascii=False), encoding='utf-8')
    print(json.dumps({"status": "ok", "trade_date": date, "pool": len(pool),
                       "kline_days": len(dates_used), **stats,
                       "passed": len(passed), "file": out_file.name}, ensure_ascii=False, indent=1))

if __name__ == '__main__':
    main()