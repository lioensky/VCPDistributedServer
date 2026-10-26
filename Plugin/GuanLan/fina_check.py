# -*- coding: utf-8 -*-
"""GuanLan 22d L3: financial three-question check over L1 screened pool.
输入: screened_{date}_circ80.json (L1 v2 output) -> 输出: fina_passed_{date}.json

三问 (观澜签字 2026-09-06, 七项全签):
  Q1 赚钱吗: 最近两个年度报告(12-31) ROE >= 8      [年度口径, 忠实签字; 中报进note不进判定]
  Q2 欠钱多吗: 最新报告期 debt_to_assets <= 60      [非金融; 金融豁免=签字规则]
  Q3 现金流真吗: cashflow.n_cashflow_act / cashflow.net_profit >= 0.5
      同报告期、同份合并现金流量表；净利润非正则失败，缺报表或版本冲突则pending。
      op_of_gr是营业利润比例，不是经营现金流，禁止替代。不存在完整历史版本证据时不现场重建历史池。

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
ROE_MIN = 8.0          # Q1, 年度口径 | 出处: 观澜8/17三问原定义(连续两年ROE>=8为质量股通用门槛, 价值投资质量筛选传统; 五风格组分化: 消费12%/金融10%另定, 此处L3全池底线)
DEBT_MAX = 60.0        # Q2, 百分比 | 出处: 非金融企业健康杠杆线(教材参考值60%, 较70%高风险线从严半档, 2026-10-11 VSearch验证; 金融股豁免因吸收存款即负债, 结构特殊——观澜9/6签字)
OCF_NP_MIN = 0.5       # Q3: 同份合并现金流量表经营现金流净额/净利润；阈值未变，旧营业利润替代公式已废止。
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

def judge(rows, is_fin, as_of=None, cashflow_rows=None):
    """Three questions over reports announced before the target date.

    Date-only announcements on the target day are conservatively excluded.
    This does not prove historical revision availability from the provider.
    """
    import math

    def finite_number(value):
        return (not isinstance(value, bool)
                and isinstance(value, (int, float))
                and math.isfinite(value))

    if not rows:
        return {'verdict': 'api_empty', 'reason': 'fina_indicator返回空'}
    cutoff_text = as_of if as_of is not None else datetime.now().strftime("%Y%m%d")

    def parse_day(value):
        if (not isinstance(value, str) or len(value) != 8
                or not value.isascii() or not value.isdigit()):
            raise ValueError("invalid financial date")
        parsed = datetime.strptime(value, "%Y%m%d").date()
        if parsed.strftime("%Y%m%d") != value:
            raise ValueError("noncanonical financial date")
        return parsed

    cutoff = parse_day(cutoff_text)
    by_period = {}
    for row in rows:
        try:
            if not isinstance(row, dict):
                raise ValueError("financial row must be an object")
            announced = parse_day(row.get("ann_date"))
            period = parse_day(row.get("end_date"))
            if announced >= cutoff or period > cutoff:
                continue
            if announced < period:
                raise ValueError("announcement precedes report period")
            previous = by_period.get(period)
            if previous is None or row["ann_date"] > previous["ann_date"]:
                by_period[period] = row
            elif row["ann_date"] == previous["ann_date"] and row != previous:
                return {'verdict': 'pending',
                        'reason': '同报告期同公告日存在冲突版本，无法确认当时可用数据'}
        except (ValueError, TypeError, OverflowError):
            return {'verdict': 'pending',
                    'reason': '财务公告日或报告期缺失/非法，不能确认目标日前可得性'}
    if not by_period:
        return {'verdict': 'pending',
                'reason': '目标日前无可确认已公告财报；当日公告无时分，保守排除'}
    rows = [by_period[period] for period in sorted(by_period, reverse=True)]
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
        elif any(not finite_number(v) for v in roes):
            q1 = {'pass': False, 'reason': f'ROE数据缺失: {roes}'}
        else:
            ok = all(float(v) >= ROE_MIN for v in roes)
            q1 = {'pass': ok, 'reason': f"年度ROE {annuals[1]['end_date']}={roes[1]}, {annuals[0]['end_date']}={roes[0]} vs {ROE_MIN}"}
    # Q2: 负债率 (金融豁免)
    debt = latest.get('debt_to_assets')
    if is_fin:
        q2 = {'pass': True, 'exempt': True, 'reason': f'金融股豁免(签字规则), 行业数据{debt}'}
    elif not finite_number(debt) or debt < 0:
        q2 = {'pass': False, 'reason': f'负债率数据缺失: {debt}'}
    else:
        q2 = {'pass': float(debt) <= DEBT_MAX, 'reason': f"负债率{debt} vs {DEBT_MAX}"}
    # Q3 uses amounts from ONE consolidated cashflow statement.
    # op_of_gr is operating profit / revenue, NOT operating cashflow.
    candidates = []
    for statement in cashflow_rows or []:
        try:
            if not isinstance(statement, dict):
                raise ValueError("invalid cashflow row")
            if statement.get("end_date") != latest.get("end_date"):
                continue
            if str(statement.get("report_type")) != "1":
                continue
            announced = parse_day(statement.get("ann_date"))
            actual = parse_day(statement.get("f_ann_date"))
            period = parse_day(statement.get("end_date"))
            if min(announced, actual) < period:
                raise ValueError("announcement precedes period")
            if max(announced, actual) >= cutoff:
                continue
            candidates.append(statement)
        except (ValueError, TypeError, OverflowError):
            return {"verdict": "pending",
                    "reason": "现金流报表日期或结构非法，不能确认同期间可用数据"}
    if not candidates:
        return {"verdict": "pending",
                "reason": "缺少目标日前同报告期合并现金流量表，未使用营业利润替代"}
    newest = max(max(r["ann_date"], r["f_ann_date"]) for r in candidates)
    versions = [
        r for r in candidates
        if max(r["ann_date"], r["f_ann_date"]) == newest]
    amounts = {(r.get("n_cashflow_act"), r.get("net_profit")) for r in versions}
    if len(amounts) != 1:
        return {"verdict": "pending",
                "reason": "同报告期现金流报表版本冲突，不能任意选择"}
    ocf, net_profit = next(iter(amounts))
    if not finite_number(ocf) or not finite_number(net_profit):
        return {"verdict": "pending", "reason": "经营现金流或净利润金额缺失"}
    if net_profit <= 0:
        q3 = {"pass": False, "reason": "同份现金流量表净利润非正，比值无意义"}
    else:
        ratio = float(ocf) / float(net_profit)
        q3 = {
            "pass": math.isfinite(ratio) and ratio >= OCF_NP_MIN,
            "ratio": ratio if math.isfinite(ratio) else None,
            "source": "cashflow",
            "report_period": latest["end_date"],
            "announcement_date": newest,
            "definition": "n_cashflow_act / net_profit; same consolidated statement",
            "reason": "同份合并现金流量表经营现金流净额/净利润，对照阈值%s" % OCF_NP_MIN}
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
    if (len(date) != 8 or not date.isascii() or not date.isdigit()
            or datetime.strptime(date, "%Y%m%d").strftime("%Y%m%d") != date):
        raise ValueError("invalid financial evaluation date")
    if date != datetime.now().strftime("%Y%m%d"):
        print(json.dumps({
            "status": "blocked",
            "error_code": "historical_financial_versions_unverified",
            "date": date,
            "message": "当前接口未证明完整历史版本可得性；禁止现场取最新数据重建过去的财务通过池。历史文件保留。"
        }, ensure_ascii=False))
        sys.exit(1)
    limit = None
    if '--limit' in args:
        limit = int(args[args.index('--limit') + 1])
        if limit <= 0:
            raise ValueError("financial limit must be positive")
    src = DATA_DIR / f"screened_{date}_circ80.json"
    if not src.exists():
        sys.exit(f"L1 output missing: {src.name}")
    pool = json.loads(src.read_text(encoding='utf-8'))['items']
    if limit:
        pool = pool[:limit]
    api = _get_api()
    ind_map = load_industry_map(api, refresh='--refresh-industry' in args)
    # Version the cache namespace rather than blocking on or overwriting
    # historical artifacts produced under a different announcement policy.
    policy_dir = DATA_DIR / "fina_cashflow_v2"
    policy_dir.mkdir(exist_ok=True)
    ckpt_f = policy_dir / f"fina_checkpoint_{date}.jsonl"
    completed = {}
    done = set()
    if ckpt_f.exists():
        for line in ckpt_f.read_text(encoding='utf-8').splitlines():
            if line.strip():
                try:
                    _row = json.loads(line)
                    if (not isinstance(_row, dict)
                            or not isinstance(_row.get("ts_code"), str)
                            or not _row["ts_code"]):
                        raise ValueError("invalid financial checkpoint row")
                    if _row.get("verdict") != "api_fail" and (
                            _row.get("evaluation_as_of") != date
                            or _row.get("financial_policy") != "cashflow-v2"
                            or _row.get("announcement_policy")
                               != "ann_date strictly before target date"):
                        raise ValueError(
                            "legacy financial checkpoint policy; preserved, "
                            "isolated rebuild required before reuse")
                    # M6 fix (Nova r8): api_fail留在checkpoint记录(簿记真)但不计入done -
                    # 传输层失败(重试后仍None)不算"已处理", 同日重跑自动重试;
                    # api_empty是"查到无数据"的稳定态, 留在done避免浪费调用
                    if _row.get('verdict') != 'api_fail':
                        if _row.get("verdict") not in ("pass", "fail", "pending", "api_empty"):
                            raise ValueError("invalid financial checkpoint verdict")
                        completed[_row["ts_code"]] = _row
                        done.add(_row['ts_code'])
                except json.JSONDecodeError as exc:
                    raise ValueError(
                        "damaged financial checkpoint; preserved, operation refused") from exc
    out_f = policy_dir / f"fina_passed_{date}.jsonl"
    pool_codes = {row["ts_code"] for row in pool}
    if len(pool_codes) != len(pool):
        raise ValueError("duplicate financial input code")
    # The checkpoint is authoritative. A crash between checkpoint and export
    # is repaired on the next completed run, without refetching finished rows.
    from ledger_io import atomic_write_bytes
    checkpoint_bytes = ckpt_f.read_bytes() if ckpt_f.exists() else b""
    if checkpoint_bytes and not checkpoint_bytes.endswith((b"\n", b"\r")):
        checkpoint_bytes += b"\n"
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
            try:
                if not isinstance(r, dict):
                    raise ValueError("financial response must be an object")
                flds, items = r.get("fields"), r.get("items")
                required = {
                    "ts_code", "ann_date", "end_date", "roe",
                    "debt_to_assets", "op_of_gr", "netprofit_margin"}
                if (not isinstance(flds, list)
                        or any(not isinstance(field, str) for field in flds)
                        or len(set(flds)) != len(flds)
                        or not required.issubset(flds)
                        or not isinstance(items, list)):
                    raise ValueError("invalid financial response schema")
                rows = []
                for item in items:
                    if not isinstance(item, (list, tuple)) or len(item) != len(flds):
                        raise ValueError("invalid financial row width")
                    observation = dict(zip(flds, item))
                    if observation.get("ts_code") != code:
                        raise ValueError("financial symbol mismatch")
                    rows.append(observation)
                cash = api(
                    "cashflow", {"ts_code": code, "report_type": "1"},
                    "ts_code,ann_date,f_ann_date,end_date,report_type,n_cashflow_act,net_profit,update_flag")
                if not isinstance(cash, dict):
                    raise ValueError("cashflow response unavailable")
                cash_fields, cash_items = cash.get("fields"), cash.get("items")
                cash_required = {
                    "ts_code", "ann_date", "f_ann_date", "end_date",
                    "report_type", "n_cashflow_act", "net_profit"}
                if (not isinstance(cash_fields, list)
                        or any(not isinstance(f, str) for f in cash_fields)
                        or len(set(cash_fields)) != len(cash_fields)
                        or not cash_required.issubset(cash_fields)
                        or not isinstance(cash_items, list)):
                    raise ValueError("invalid cashflow schema")
                cash_rows = []
                for item in cash_items:
                    if not isinstance(item, (list, tuple)) or len(item) != len(cash_fields):
                        raise ValueError("invalid cashflow row width")
                    statement = dict(zip(cash_fields, item))
                    if statement.get("ts_code") != code:
                        raise ValueError("cashflow symbol mismatch")
                    cash_rows.append(statement)
                verdict = judge(rows, is_fin, as_of=date, cashflow_rows=cash_rows)
            except (ValueError, TypeError, OverflowError):
                verdict = {
                    "verdict": "api_fail",
                    "reason": "财务响应结构或标的校验失败，未使用该响应判定"}
            result = {
                'ts_code': code, 'name': info.get('name'),
                'industry': info.get('industry'), **verdict,
                'evaluation_as_of': date,
                'announcement_policy': 'ann_date strictly before target date',
                'point_in_time_verified': False}
            stats[result['verdict'] if result['verdict'] in ('pass', 'fail', 'pending') else 'api_fail'] += 1
        result.update({
            "evaluation_as_of": date,
            "announcement_policy": "ann_date strictly before target date",
            "point_in_time_verified": False,
            "financial_policy": "cashflow-v2",
            "historical_reconstruction_allowed": False})
        addition = (
            json.dumps(result, ensure_ascii=False, allow_nan=False) + "\n"
        ).encode("utf-8")
        atomic_write_bytes(ckpt_f, checkpoint_bytes + addition)
        checkpoint_bytes += addition
        if result["verdict"] != "api_fail":
            completed[code] = result
        stats['processed_new'] += 1
        if i % 50 == 0:
            el = time.time() - t0
            print(f"progress {i}/{len(pool)} | {json.dumps(stats)} | {el:.0f}s elapsed", flush=True)
    # --limit is a diagnostic partial run, not a complete export.
    complete = limit is None and pool_codes.issubset(completed)
    if complete:
        passed_rows = [
            completed[code] for code in sorted(pool_codes)
            if completed[code]["verdict"] == "pass"]
        atomic_write_bytes(
            out_f, "".join(
                json.dumps(row, ensure_ascii=False, allow_nan=False) + "\n"
                for row in passed_rows).encode("utf-8"))
    print(json.dumps({
        'status': 'ok' if complete else 'partial',
        'date': date, 'pool': len(pool), **stats,
        'export_complete': complete,
        'export_file': out_f.relative_to(DATA_DIR).as_posix() if complete else None,
        'unresolved_codes': sorted(pool_codes - completed.keys()),
        'note': (
            '完整通过池已原子导出' if complete
            else '本轮不完整，未替换通过池；可复用checkpoint继续处理'),
        'elapsed_s': round(time.time() - t0)
    }, ensure_ascii=False, indent=1, allow_nan=False))
    if not complete:
        sys.exit(1)

if __name__ == '__main__':
    main()