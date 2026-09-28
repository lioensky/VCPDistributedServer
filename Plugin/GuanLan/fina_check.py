# -*- coding: utf-8 -*-
"""GuanLan 22d L3: financial three-question check over L1 screened pool.
输入: screened_{date}_circ80.json (L1 v2 output) -> 输出: fina_passed_{date}.json

三问 (观澜签字 2026-09-06, 七项全签):
  Q1 赚钱吗: 最近两个年度报告(12-31) ROE >= 8      [年度口径, 忠实签字; 中报进note不进判定]
  Q2 欠钱多吗: 最新报告期 debt_to_assets <= 60      [非金融; 金融豁免=签字规则]
  Q3 现金流真吗: op_of_gr / netprofit_margin >= 0.5 [经营现金流/净利润, 数学推导: 两字段分母同为营业收入, 约掉]
                                              [netprofit_margin <= 0 -> Q3 fail (除零防御, 亏损股Q1亦挂)]

Design (瑶序 2026-09-06, per probes T4-T6):
- fina_indicator 单票一次调用返回全历史(~100行) - 年度验证零额外成本
- 缺中报: 最新 end_date < 20260630 -> pending (宁缺毋假, 二次筛)
- 金融豁免: industry in FIN_SET 跳Q2 (Q1/Q3照跑, 按签字范围)
- pacing 0.35s/票 (~171 QPM, 200分档QPM=200 安全); API None重试1次
- checkpoint: 逐票append jsonl, 中断重跑跳过已处理 (harvest哲学)
- industry_map: 本地缓存低频数据, --refresh-industry 手动刷新

Usage:
  python fina_check.py 20260904 --limit 10    # 小样本
  python fina_check.py 20260904               # 全量 (~11 min pacing)
"""
import json, sys, time
from pathlib import Path
from datetime import datetime

sys.stdout.reconfigure(encoding='utf-8', errors='replace')
sys.stderr.reconfigure(encoding='utf-8', errors='replace')

BASE = Path(__file__).parent
DATA_DIR = BASE / "market_data"

FIN_SET = {'银行', '证券', '保险', '多元金融', '信托'}  # 观澜签字豁免范围, meta可调
ROE_MIN = 8.0          # Q1, 年度口径 | 出处: 观澜8/17三问原定义(连续两年ROE>=8为质量股通用门槛, 巴菲特式选股标准族; 五风格组分化: 消费12%/金融10%另定, 此处L3全池底线)
DEBT_MAX = 60.0        # Q2, 百分比 | 出处: 非金融企业健康杠杆线(业界通用60%分界; 金融股豁免因吸收存款即负债, 结构特殊——观澜9/6签字)
OCF_NP_MIN = 0.5       # Q3 | 出处: 盈利质量门槛(经营现金流/净利润>=0.5防纸面利润, 财务审计常用健康线; 数学推导=op_of_gr与netprofit_margin约分, 瑶序9/6会审)
MIDYEAR = '20260630'   # 中报期, pending判定线 | 维护: 每季度首周人工更新下期(看板#23维护栏, 首查2027-01)
PACING = 0.35          # 秒/票

def _get_api():
    import importlib.util
    spec = importlib.util.spec_from_file_location('gl', BASE / 'main.py')
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m._tushare_api

def load_industry_map(api, refresh=False):
    f = DATA_DIR / "industry_map.json"
    if f.exists() and not refresh:
        return json.loads(f.read_text(encoding='utf-8'))
    r = api('stock_basic', {'list_status': 'L'}, 'ts_code,name,industry')
    m = {it[0]: {'name': it[1], 'industry': it[2]} for it in (r.get('items') or [])}
    f.write_text(json.dumps(m, ensure_ascii=False), encoding='utf-8')
    return m

def fetch_fina(api, ts_code):
    """全历史一次拉取; None重试1次; 再None返回None."""
    for attempt in (1, 2):
        r = api('fina_indicator', {'ts_code': ts_code},
                'ts_code,ann_date,end_date,roe,debt_to_assets,op_of_gr,netprofit_margin')
        if r is not None:
            return r
        if attempt == 1:
            time.sleep(1.0)
    return None

def judge(rows, is_fin):
    """三问判定. rows = fina_indicator items (dict rows)."""
    if not rows:
        return {'verdict': 'api_empty', 'reason': 'fina_indicator返回空'}
    rows = sorted(rows, key=lambda r: str(r.get('end_date', '')), reverse=True)
    latest = rows[0]
    # pending: 中报未披露
    if str(latest.get('end_date', '')) < MIDYEAR:
        return {'verdict': 'pending', 'reason': f"最新报告期{latest.get('end_date')} < {MIDYEAR}, 中报未披露",
                'latest_end': latest.get('end_date')}
    # Q1: 最近两个年度报告 ROE >= 8
    annuals = [r for r in rows if str(r.get('end_date', '')).endswith('1231')][:2]
    q1 = None
    if len(annuals) < 2:
        q1 = {'pass': False, 'reason': f"年度报告不足两年({len(annuals)})"}
    else:
        # L10 fix (Nova r8): 观澜签字原文"连续两年" - 年报断档(如2025+2023)不冒充连续, 宁缺毋假
        y_gap = int(str(annuals[0]['end_date'])[:4]) - int(str(annuals[1]['end_date'])[:4])
        roes = [r.get('roe') for r in annuals]
        if y_gap != 1:
            q1 = {'pass': False, 'reason': f"年度报告断档({annuals[1]['end_date']}~{annuals[0]['end_date']}间隔{y_gap}年), 宁缺毋假"}
        elif any(not isinstance(v, (int, float)) for v in roes):
            q1 = {'pass': False, 'reason': f'ROE数据缺失: {roes}'}
        else:
            ok = all(float(v) >= ROE_MIN for v in roes)
            q1 = {'pass': ok, 'reason': f"年度ROE {annuals[1]['end_date']}={roes[1]}, {annuals[0]['end_date']}={roes[0]} vs {ROE_MIN}"}
    # Q2: 负债率 (金融豁免)
    debt = latest.get('debt_to_assets')
    if is_fin:
        q2 = {'pass': True, 'exempt': True, 'reason': f'金融股豁免(签字规则), 行业数据{debt}'}
    elif not isinstance(debt, (int, float)):
        q2 = {'pass': False, 'reason': f'负债率数据缺失: {debt}'}
    else:
        q2 = {'pass': float(debt) <= DEBT_MAX, 'reason': f"负债率{debt} vs {DEBT_MAX}"}
    # Q3: 经营现金流/净利润 (op_of_gr / netprofit_margin, 分母营业收入约掉)
    op, npm = latest.get('op_of_gr'), latest.get('netprofit_margin')
    if not isinstance(op, (int, float)) or not isinstance(npm, (int, float)):
        q3 = {'pass': False, 'reason': f'现金流/利润率数据缺失: op={op}, npm={npm}'}
    elif float(npm) <= 0:
        q3 = {'pass': False, 'reason': f'净利率{npm}<=0, 比值无意义(亏损)'}
    else:
        ratio = float(op) / float(npm)
        q3 = {'pass': ratio >= OCF_NP_MIN, 'reason': f"现金流/净利润={ratio:.3f} (op {op}/npm {npm}) vs {OCF_NP_MIN}"}
    all_pass = q1['pass'] and q2['pass'] and q3['pass']
    note = f"最新期{latest.get('end_date')} roe={latest.get('roe')} (中报参考, 判定用年度)"
    return {'verdict': 'pass' if all_pass else 'fail',
            'q1': q1, 'q2': q2, 'q3': q3, 'note': note,
            'latest_end': latest.get('end_date')}

def main():
    args = sys.argv[1:]
    if not args:
        sys.exit("need trade_date, e.g. python fina_check.py 20260904 [--limit 10]")
    date = args[0]
    limit = None
    if '--limit' in args:
        limit = int(args[args.index('--limit') + 1])
    src = DATA_DIR / f"screened_{date}_circ80.json"
    if not src.exists():
        sys.exit(f"L1 output missing: {src.name}")
    pool = json.loads(src.read_text(encoding='utf-8'))['items']
    if limit:
        pool = pool[:limit]
    api = _get_api()
    ind_map = load_industry_map(api, refresh='--refresh-industry' in args)
    ckpt_f = DATA_DIR / f"fina_checkpoint_{date}.jsonl"
    done = set()
    if ckpt_f.exists():
        for line in ckpt_f.read_text(encoding='utf-8').splitlines():
            if line.strip():
                try:
                    _row = json.loads(line)
                    # M6 fix (Nova r8): api_fail留在checkpoint记录(簿记真)但不计入done -
                    # 传输层失败(重试后仍None)不算"已处理", 同日重跑自动重试;
                    # api_empty是"查到无数据"的稳定态, 留在done避免浪费调用
                    if _row.get('verdict') != 'api_fail':
                        done.add(_row['ts_code'])
                except json.JSONDecodeError:
                    pass
    out_f = DATA_DIR / f"fina_passed_{date}.jsonl"
    ckpt = ckpt_f.open('a', encoding='utf-8')
    passed_f = out_f.open('a', encoding='utf-8')
    stats = {'processed_new': 0, 'skip_done': 0, 'pass': 0, 'fail': 0, 'pending': 0, 'api_fail': 0}
    t0 = time.time()
    for i, row in enumerate(pool, 1):
        code = row['ts_code']
        if code in done:
            stats['skip_done'] += 1
            continue
        info = ind_map.get(code, {})
        is_fin = info.get('industry') in FIN_SET
        r = fetch_fina(api, code)
        time.sleep(PACING)
        if r is None:
            result = {'ts_code': code, 'name': info.get('name'), 'industry': info.get('industry'),
                      'verdict': 'api_fail', 'reason': '重试后仍None'}
            stats['api_fail'] += 1
        else:
            flds = r.get('fields', [])
            rows = [dict(zip(flds, it)) for it in (r.get('items') or [])]
            result = {'ts_code': code, 'name': info.get('name'), 'industry': info.get('industry'),
                      **judge(rows, is_fin)}
            stats[result['verdict'] if result['verdict'] in ('pass', 'fail', 'pending') else 'api_fail'] += 1
        ckpt.write(json.dumps(result, ensure_ascii=False) + '\n')
        if result['verdict'] == 'pass':
            passed_f.write(json.dumps(result, ensure_ascii=False) + '\n')
        stats['processed_new'] += 1
        if i % 50 == 0:
            el = time.time() - t0
            print(f"progress {i}/{len(pool)} | {json.dumps(stats)} | {el:.0f}s elapsed", flush=True)
    ckpt.close(); passed_f.close()
    print(json.dumps({'date': date, 'pool': len(pool), **stats,
                      'elapsed_s': round(time.time() - t0)}, ensure_ascii=False, indent=1))

if __name__ == '__main__':
    main()