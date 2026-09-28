# -*- coding: utf-8 -*-
"""GuanLan 23d: results结算管道骨架 (harvest镜像工程).
判定段留接口等口径: 23a flat带宽(观澜)+23b基准价边缘口径(观澜)+23c复核(Nova) → 三件齐后填肉.

已实装 (与口径无关的骨架):
  1. 扫judgments: time_window_end <= today 且 (symbol, window_end)不在results -> 待结算
  2. 双端收盘价: 判断日(timestamp[:10])+窗口末日, 本地kline_daily优先, API兜底
  3. 对账键: (symbol, window_end) 与calibration一致
  4. 写入: append-only + 末字符换行防御 (2026-09-06拼行判例同款)
判定接口 (口径齐后填):
  verdict = judge(p_change, band, direction) — band未配置时输出status=awaiting_calibration不算分
涨跌幅口径 (23b草案, 待观澜定稿): (窗口末日收盘 - 判断日收盘) / 判断日收盘
  判断日收盘缺失(停牌/数据缺) -> 顺延下一有价日; 顺延超5日 -> status=undecided挂起 (23b草案)
止损结算语义 (23b补充 2026-09-06 22:49 观澜签字, 数字审查发现一):
  窗口期内(判断日后, 窗口末日含)止损触发 -> 按止损事件结算, 不用窗口末日收盘价:
    up/flat判断: 任一日 low <= stop_loss  -> actual=down, close_price取stop_loss
    down判断:    任一日 high >= stop_loss -> actual=up,   close_price取stop_loss (对称)
  扫描数据: 本地kline_daily的low/high; 窗口日期文件不全 -> 正常收盘价结算+note标stop_scan覆盖不全

Usage: python settle_results.py [--dry-run]
"""
import json, sys, time
from pathlib import Path
from datetime import datetime, date

sys.stdout.reconfigure(encoding='utf-8', errors='replace')
sys.stderr.reconfigure(encoding='utf-8', errors='replace')

BASE = Path(__file__).parent
DATA_DIR = BASE / "market_data"
J_FILE = BASE / "judgments.jsonl"
R_FILE = BASE / "results.jsonl"
FLAT_BAND = 0.035  # 23a签字 2026-09-07 22:35 观澜: 87日87窗口四分位距校准, 两票带宽总宽7.03%/7.12%比值1.01统一成立, 平均上下界-3.67%/+3.41%对称化取整; 分布不对称(紫金右偏云铝左偏)判为17窗口样本噪声不追; 追溯适用9/10到期两条

def _get_api():
    import importlib.util
    spec = importlib.util.spec_from_file_location('gl', BASE / 'main.py')
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m._tushare_api

def load_jsonl(path):
    rows, bad = [], 0
    if not path.exists():
        return rows, bad
    for line in path.read_text(encoding='utf-8').splitlines():
        line = line.strip()
        if not line:
            continue
        try:
            obj = json.loads(line)
        except json.JSONDecodeError:
            bad += 1
            continue
        if '_meta' in obj or '_example' in obj:
            continue
        rows.append(obj)
    return rows, bad

def local_close(d8):
    """本地kline_daily_YYYYMMDD.json -> {ts_code: close}. d8=YYYYMMDD."""
    f = DATA_DIR / f"kline_daily_{d8}.json"
    if not f.exists():
        return None
    jd = json.loads(f.read_text(encoding='utf-8'))
    di = {k: i for i, k in enumerate(jd.get('fields', []))}
    if 'close' not in di:
        return None
    return {str(it[di['ts_code']]).split('.')[0]: it[di['close']] for it in jd.get('items', []) if it[di['close']] is not None}

def api_close(api, d8):
    r = api('daily', {'trade_date': d8}, 'ts_code,close')
    if r is None:
        return None
    return {str(it[0]).split('.')[0]: it[1] for it in (r.get('items') or []) if it[1] is not None}

def close_map(api, d_iso):
    d8 = d_iso.replace('-', '')
    m = local_close(d8)
    if m is not None:
        return m, 'local'
    m = api_close(api, d8)
    return (m, 'api') if m is not None else (None, 'missing')

def judge(p_change, band, direction):
    """口径接口: 23a带宽+方向映射. band=None -> awaiting_calibration."""
    if band is None:
        return {'status': 'awaiting_calibration',
                'note': '23a flat带宽未定(观澜87日校准) - 骨架不判分'}
    if p_change > band:
        actual = 'up'
    elif p_change < -band:
        actual = 'down'
    else:
        actual = 'flat'
    return {'status': 'ok', 'actual_direction': actual,
            'hit': actual == direction}

def scan_stop_hit(sym, jday_iso, win_iso, stop_loss, direction):
    """23b止损结算语义 (2026-09-06签字): 窗口期内触发 -> (True, 触发日, stop价结算).
    扫描本地kline_daily的low/high (判断日后至窗口末日, 含末日).
    覆盖不全 -> (False, None, None) + 调用方note标注, 回落正常结算."""
    if not stop_loss:
        return None, None, None
    from datetime import timedelta
    try:
        cur = date.fromisoformat(jday_iso) + timedelta(days=1)
        end = date.fromisoformat(win_iso)
    except ValueError:
        return None, None, None
    stop = float(stop_loss)
    hit_day = None
    scanned = 0
    while cur <= end:
        cm = local_close(cur.strftime('%Y%m%d'))
        if cm is not None:
            scanned += 1
            f = DATA_DIR / f"kline_daily_{cur.strftime('%Y%m%d')}.json"
            jd = json.loads(f.read_text(encoding='utf-8'))
            di = {k: i for i, k in enumerate(jd.get('fields', []))}
            low = {it[di['ts_code']]: it[di['low']] for it in jd.get('items', []) if 'low' in di and it[di['low']] is not None}
            high = {it[di['ts_code']]: it[di['high']] for it in jd.get('items', []) if 'high' in di and it[di['high']] is not None}
            lo, hi = low.get(sym), high.get(sym)
            if direction in ('up', 'flat') and lo is not None and lo <= stop:
                hit_day = cur.isoformat()
                break
            if direction == 'down' and hi is not None and hi >= stop:
                hit_day = cur.isoformat()
                break
        cur += timedelta(days=1)
    return (hit_day, stop, scanned) if hit_day else (None, None, scanned)

def main():
    dry = '--dry-run' in sys.argv
    judgments, j_bad = load_jsonl(J_FILE)
    results, r_bad = load_jsonl(R_FILE)
    settled = {(r.get('symbol'), str(r.get('window_end'))) for r in results}
    today = date.today().isoformat()
    due = [j for j in judgments
           if str(j.get('time_window_end', '9999')) <= today
           and (j.get('symbol'), str(j.get('time_window_end'))) not in settled]
    report = {'today': today, 'judgments': len(judgments), 'results': len(results),
              'parse_errors': {'j': j_bad, 'r': r_bad}, 'due': len(due), 'settled_new': 0,
              'awaiting': 0, 'skipped': []}
    if not due:
        print(json.dumps(report, ensure_ascii=False, indent=1))
        return
    api = _get_api() if not dry else None
    out_lines = []
    for j in due:
        sym, win = j['symbol'], str(j['time_window_end'])
        jday = str(j.get('timestamp', ''))[:10]
        cm_j, src_j = (close_map(api, jday) if api else (None, 'dry'))
        cm_w, src_w = (close_map(api, win) if api else (None, 'dry'))
        pj = (cm_j or {}).get(sym)
        pw = (cm_w or {}).get(sym)
        if pj is None or pw is None or pj <= 0:
            report['skipped'].append({'symbol': sym, 'window': win,
                                       'reason': f"价格缺失 jday={src_j} win={src_w}"})
            continue
        # 23b止损结算语义: 窗口期内触发 -> 按止损事件结算 (2026-09-06签字)
        stop_hit_day, stop_px, scanned_days = scan_stop_hit(sym, jday, win, j.get('stop_loss'), j.get('direction'))
        if stop_hit_day:
            row = {'symbol': sym, 'window_end': win,
                   'actual_direction': 'down' if j.get('direction') in ('up', 'flat') else 'up',
                   'actual_return': round((stop_px - pj) / pj, 4),
                   'close_price': stop_px,
                   'timestamp': datetime.now().isoformat(timespec='seconds'),
                   'judge_meta': {'judge_day_close': pj, 'judge_day': jday,
                                   'source': f'stop_scan({scanned_days}d)',
                                   'stop_hit_day': stop_hit_day, 'stop_price': stop_px,
                                   'band': None, 'hit': False,
                                   'note': '止损触发结算(23b): 不用窗口末日收盘'}}
            out_lines.append(json.dumps(row, ensure_ascii=False))
            report['settled_new'] += 1
            continue
        p_change = (pw - pj) / pj
        v = judge(p_change, FLAT_BAND, j.get('direction'))
        if v['status'] == 'awaiting_calibration':
            report['awaiting'] += 1
            report.setdefault('awaiting_detail', []).append(
                {'symbol': sym, 'window': win, 'p_change': round(p_change, 4),
                 'judge_day_close': pj, 'window_close': pw, 'src': f"{src_j}/{src_w}"})
            continue
        row = {'symbol': sym, 'window_end': win,
               'actual_direction': v['actual_direction'],
               'actual_return': round(p_change, 4),
               'close_price': pw,
               'timestamp': datetime.now().isoformat(timespec='seconds'),
               'judge_meta': {'judge_day_close': pj, 'judge_day': jday,
                               'source': f"{src_j}/{src_w}",
                               'band': FLAT_BAND,
                               'hit': v['hit'],
                               'stop_scan': scanned_days}}  # 23b披露: 有止损未触发时标注扫描覆盖天数(本地K线缺日->覆盖不全->人工复核)
        out_lines.append(json.dumps(row, ensure_ascii=False))
        report['settled_new'] += 1
    if out_lines and not dry:
        needs_nl = False
        if R_FILE.exists() and R_FILE.stat().st_size > 0:
            with R_FILE.open('rb') as f:
                f.seek(R_FILE.stat().st_size - 1)
                needs_nl = f.read(1) not in (b"\n", b"\r")
        with R_FILE.open('a', encoding='utf-8') as f:
            if needs_nl:
                f.write("\n")
            for ln in out_lines:
                f.write(ln + "\n")
    print(json.dumps(report, ensure_ascii=False, indent=1))

if __name__ == '__main__':
    main()