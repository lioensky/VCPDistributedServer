# -*- coding: utf-8 -*-
"""GuanLan 23e: 解禁桥 - 终池 × 未来N天解禁对表.
探针实证 (2026-09-06): share_float可拉(2000分token够), 6000行=单次上限(60天窗口顶格截断嫌疑)
→ 按月分片拉取+顶格检测. 数据形态: 每股东一行(float_ratio=该股东解禁占总股本比).

聚合: 按(ts_code, float_date)聚合股东行 -> total_ratio + holders + pevc标记
阈值 (观澜调研9/6四要素第一版): 聚合ratio>=0.50 标red; PE/VC主导(合计>=50%解禁量)标yellow
输出: unlock_report_{date}.json - 终池内未来60天解禁票, 人工决策用.

Usage: python unlock_check.py 20260904 [--days 60]
"""
import json, sys, time
from pathlib import Path
from datetime import datetime, date

sys.stdout.reconfigure(encoding='utf-8', errors='replace')
sys.stderr.reconfigure(encoding='utf-8', errors='replace')

BASE = Path(__file__).parent
DATA_DIR = BASE / "market_data"

FIELDS = 'ts_code,ann_date,float_date,float_share,float_ratio,holder_name'
PACING = 0.35
# PEVC两级分词 (观澜 2026-09-06 22:49签字, 数字审查发现三):
# 宽词('投资'/'资本')误命中产业资本战投平台——而产业资本减持意愿恰低; 公募资管亦非真PE/VC
PEVC_STRONG = ('私募', '创投', '风投')  # 强信号: 命中才计入主导判定(黄灯资格)
PEVC_WEAK = ('基金', '投资', '资产管理', '资本')  # 弱信号: 只进holders明细flag, 不算主导

def _get_api():
    import importlib.util
    spec = importlib.util.spec_from_file_location('gl', BASE / 'main.py')
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m._tushare_api

def fetch_unlocks_pool(api, pool_codes, start_d, end_d):
    """逐票拉取 (2026-09-06晚修正: 探针实证全市场单周即顶6000上限, 月分片假设报废——
    share_float粒度=每股东每批次一行, 周行数6000+远超事件数直觉, 量级判例见日记).
    按票拉取: 每次返回单票数据永不触顶, 天然即池内. 单票None重试1次, 持续失败记名单不阻塞."""
    rows, failures = [], []
    for code in sorted(pool_codes):
        r = None
        for attempt in (1, 2):
            r = api('share_float', {'ts_code': code, 'start_date': start_d, 'end_date': end_d}, FIELDS)
            if r is not None:
                break
            time.sleep(1.0)
        if r is None:
            failures.append(code)
            continue
        rows.extend(r.get('items') or [])
        time.sleep(PACING)
    return rows, failures

def aggregate(rows):
    """每股东一行 -> 按(ts_code, float_date)聚合."""
    agg = {}
    for it in rows:
        code, fdate = it[0], it[2]
        ratio_pct = it[4] if isinstance(it[4], (int, float)) else 0  # 原生单位=百分比 (M8: 神华13行校准——每行share/(ratio/100)=同一基准183亿股)
        ratio = ratio_pct / 100.0  # -> 真分数, 与阈值0.50(=50%总股本)同空间
        holder = it[5] or ''
        shares = it[3] if isinstance(it[3], (int, float)) else 0
        k = (code, fdate)
        a = agg.setdefault(k, {'total_ratio': 0.0, 'holders': [], 'pevc_shares': 0.0, 'total_shares': 0.0, 'ann_date': it[1]})
        a['total_ratio'] += ratio
        a['total_shares'] += shares
        # PEVC两级 (22:49签字): 强信号计入主导, 弱信号只flag明细
        strong = any(w in holder for w in PEVC_STRONG)
        weak_only = (not strong) and any(w in holder for w in PEVC_WEAK)
        if strong:
            a['pevc_shares'] += shares
        a['holders'].append({'name': holder, 'ratio': ratio_pct,
                             'pevc': 'strong' if strong else ('weak' if weak_only else '')})  # 明细保留原生%+两级flag
    return agg

def main():
    args = sys.argv[1:]
    if not args:
        sys.exit("need trade_date, e.g. python unlock_check.py 20260904 [--days 60]")
    d = args[0]
    days = 60
    if '--days' in args:
        days = int(args[args.index('--days') + 1])
    pool_f = DATA_DIR / f"final_pool_{d}.json"
    if not pool_f.exists():
        sys.exit(f"final pool missing: {pool_f.name}")
    pool = {r['code'] for r in json.loads(pool_f.read_text(encoding='utf-8')).get('items', [])}
    start = date.today().strftime("%Y%m%d")
    from datetime import timedelta
    end = (date.today() + timedelta(days=days)).strftime("%Y%m%d")
    api = _get_api()
    rows, failures = fetch_unlocks_pool(api, pool, start, end)
    agg = aggregate(rows)
    hits = []
    for (code, fdate), a in sorted(agg.items(), key=lambda x: x[0][1]):
        if code not in pool:
            continue
        pevc_lead = a['total_shares'] > 0 and (a['pevc_shares'] / a['total_shares']) >= 0.5
        level = 'RED' if a['total_ratio'] >= 0.50 else ('YELLOW' if pevc_lead else 'INFO')
        hits.append({'ts_code': code, 'float_date': fdate, 'ann_date': a['ann_date'],
                     'total_ratio': round(a['total_ratio'], 4),
                     'total_share_wan': round(a['total_shares'], 1),  # M8: float_share原生=万股(神华校准闭环: sum(share万)÷(sum(ratio%)/100)=183.1亿=真实总股本)
                     'pevc_lead': pevc_lead, 'level': level,
                     'holders': a['holders'][:8]})
    lv = {'RED': 0, 'YELLOW': 0, 'INFO': 0}
    for h in hits:
        lv[h['level']] += 1
    out = {"_meta": {"generated_at": datetime.now().isoformat(timespec='seconds'),
                      "pool_date": d, "pool_size": len(pool),
                      "window": f"{start}..{end}", "days": days,
                      "raw_rows": len(rows), "agg_events": len(agg),
                      "fetch_failures": failures,
                      "thresholds": "RED: 聚合解禁占总股本>=50% | YELLOW: PE/VC主导(>=50%解禁量) | INFO: 其余",
                      "source": "tushare share_float 按票拉取 (量级判例: 全市场单周即顶6000上限, 2026-09-06探针)",
                      "note": "持仓自查: 紫金601899 2026全年解禁0行(P2探针) | M8单位校准(2026-09-06): float_ratio原生=百分比(神华13行每行share÷(ratio/100)=同一183亿股基准, 量纲闭环), 代码内已转真分数; Issue#1130重复嫌疑撤诉(三票exact-duplicate=0, 600060四行=四个不同激励对象, 于芝涛两行=2022/2026两批次)"},
           "stats": lv, "items": hits}
    out_f = DATA_DIR / f"unlock_report_{d}.json"
    out_f.write_text(json.dumps(out, ensure_ascii=False), encoding='utf-8')
    print(json.dumps({"status": "ok", "pool": len(pool), "window_days": days,
                       "raw_rows": len(rows), "fetch_failures": len(failures),
                       "hits": len(hits), "levels": lv,
                       "first_hits": [(h['ts_code'], h['float_date'], h['level']) for h in hits[:6]],
                       "file": out_f.name}, ensure_ascii=False))

if __name__ == '__main__':
    main()