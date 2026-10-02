# -*- coding: utf-8 -*-
"""GuanLan 23f: 终池排序小工具 (连续分数版, 观澜9/6调研确认"连续分数排序比硬分类稳健").
输入: tech_passed_{date}.json (v1.1含vol_ratio) + final_pool_{date}.json (终池名单)
输出: ranked_{date}.json - 终池142只按合成分数降序, 服务人工细看从头部看起.

合成分数 (无参数可调, 防过度工程):
  z(MA20-MA60)/close)  趋势强度: 均线差值占价格比例的z-score (跨池标准化, 消除价格量纲)
  + z(vol_ratio)        量能强度: 量比z-score (R4同源数据)
两因子等权 - 观澜未指定权重前不发明; 以后加权属v2话题.

Usage: python rank_pool.py 20260904
"""
import json, sys
from pathlib import Path
from datetime import datetime

sys.stdout.reconfigure(encoding='utf-8', errors='replace')
sys.stderr.reconfigure(encoding='utf-8', errors='replace')

BASE = Path(__file__).parent
DATA_DIR = BASE / "market_data"

def zscores(xs):
    n = len(xs)
    if n < 2:
        return [0.0] * n
    mu = sum(xs) / n
    var = sum((x - mu) ** 2 for x in xs) / n
    sd = var ** 0.5
    if sd == 0:
        return [0.0] * n
    return [(x - mu) / sd for x in xs]

def main():
    args = sys.argv[1:]
    if not args:
        sys.exit("need trade_date, e.g. python rank_pool.py 20260904")
    date = args[0]
    tech_f = DATA_DIR / f"tech_passed_{date}.json"
    pool_f = DATA_DIR / f"final_pool_{date}.json"
    for f in (tech_f, pool_f):
        if not f.exists():
            sys.exit(f"input missing: {f.name}")
    tech = {r['ts_code']: r for r in json.loads(tech_f.read_text(encoding='utf-8')).get('items', [])}
    pool = json.loads(pool_f.read_text(encoding='utf-8')).get('items', [])
    rows = []
    for p in pool:
        t = tech.get(p['code'])
        if not t or t.get('vol_ratio') is None or not t.get('ma20') or not t.get('ma60'):
            rows.append({'code': p['code'], 'name': p.get('name', ''),
                         'score': None, 'reason': 'tech数据缺字段'})
            continue
        trend = (t['ma20'] - t['ma60']) / t['latest_adj_close']  # M7 fix (Nova r9): 分母换同尺度后复权收盘——原raw_close使每票trend被乘复权因子(平安139倍影子冠军), fallback删去(raw与adj同来自tech输出必存在)
        rows.append({'code': p['code'], 'name': p.get('name', ''),
                     'trend_raw': round(trend, 4), 'vol_ratio': t['vol_ratio'],
                     'ma20': t['ma20'], 'ma60': t['ma60']})
    scored = [r for r in rows if r.get('score') is None and 'trend_raw' in r]
    zs_t = zscores([r['trend_raw'] for r in scored])
    zs_v = zscores([r['vol_ratio'] for r in scored])
    for r, zt, zv in zip(scored, zs_t, zs_v):
        r['z_trend'], r['z_vol'] = round(zt, 3), round(zv, 3)
        r['score'] = round(zt + zv, 3)
    scored.sort(key=lambda r: r['score'], reverse=True)
    missing = [r for r in rows if r.get('score') is None]
    out = {"_meta": {"generated_at": datetime.now().isoformat(timespec='seconds'),
                      "trade_date": date, "pool": len(pool),
                      "scored": len(scored), "unscored": len(missing),
                      "formula": "z(trend强度)+z(vol_ratio) 等权 (23f, 观澜9/6签字连续分数版)",
                      "note": "无参数可调; 权重化属v2话题"},
           "items": scored, "unscored": missing}
    out_f = DATA_DIR / f"ranked_{date}.json"
    out_f.write_text(json.dumps(out, ensure_ascii=False), encoding='utf-8')
    print(json.dumps({"status": "ok", "date": date, "pool": len(pool),
                       "scored": len(scored), "unscored": len(missing),
                       "top5": [(r['code'], r['score']) for r in scored[:5]],
                       "file": out_f.name}, ensure_ascii=False))

if __name__ == '__main__':
    main()