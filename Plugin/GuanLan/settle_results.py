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
from filelock import FileLock
from ledger_guard import recovered_access

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
        if not isinstance(obj, dict):
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

def close_map(api, d_iso, max_back=10):
    """Return (prices, source, used_date); only confirmed closures may roll back.
    Missing data on an OPEN day must never be replaced by an older close.
    Exact-date quotes remain usable without a calendar round trip.
    """
    from datetime import timedelta
    d = date.fromisoformat(d_iso)

    def fetch(cur):
        d8 = cur.strftime('%Y%m%d')
        prices = local_close(d8)
        if prices:
            return prices, 'local', cur.isoformat()
        if api is not None:
            prices = api_close(api, d8)
            if prices:
                return prices, 'api', cur.isoformat()
        return None, 'missing', None

    exact = fetch(d)
    if exact[0] is not None:
        return exact
    if api is None:
        return None, 'calendar_unavailable', None
    try:
        calendar = api(
            'trade_cal',
            {'exchange': 'SSE',
             'start_date': (d - timedelta(days=max_back)).strftime('%Y%m%d'),
             'end_date': d.strftime('%Y%m%d')},
            'cal_date,is_open')
        if not isinstance(calendar, dict):
            return None, 'calendar_unavailable', None
        fields = calendar.get('fields') or []
        if 'cal_date' not in fields or 'is_open' not in fields:
            return None, 'calendar_invalid', None
        open_by_date = {}
        for item in calendar.get('items') or []:
            row = dict(zip(fields, item))
            flag = str(row.get('is_open'))
            if flag in ('0', '1'):
                open_by_date[str(row.get('cal_date'))] = flag == '1'
    except Exception:
        return None, 'calendar_unavailable', None

    for offset in range(max_back + 1):
        cur = d - timedelta(days=offset)
        d8 = cur.strftime('%Y%m%d')
        if d8 not in open_by_date:
            return None, 'calendar_incomplete', None
        if open_by_date[d8]:
            # Exact day was already fetched. An open-day failure is final.
            return fetch(cur) if offset else (None, 'open_day_missing', None)
    return None, 'no_open_day_in_window', None

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

def scan_stop_hit(sym, jday_iso, win_iso, stop_loss, direction, api=None):
    """Return (first hit date, stop price, scanned count).

    Count None means coverage unknown, NOT evidence of no stop hit.
    Missing symbol/extreme prices are unknown even on a known trading day.
    Only a calendar-confirmed closed day may be skipped without local data.
    """
    if stop_loss is None:
        return None, None, 0
    import math
    from datetime import timedelta
    try:
        cur = date.fromisoformat(jday_iso) + timedelta(days=1)
        end = date.fromisoformat(win_iso)
        if isinstance(stop_loss, bool):
            raise ValueError("boolean stop")
        stop = float(stop_loss)
        if not math.isfinite(stop) or stop <= 0 or direction not in ("up", "down", "flat"):
            raise ValueError("invalid stop")
    except (ValueError, TypeError, OverflowError):
        return None, None, None
    code = str(sym).split('.')[0]
    scanned = 0
    closed_days = None
    while cur <= end:
        d8 = cur.strftime("%Y%m%d")
        path = DATA_DIR / f"kline_daily_{d8}.json"
        if not path.exists():
            if closed_days is None:
                closed_days = set()
                try:
                    if api is None:
                        return None, None, None
                    calendar = api(
                        "trade_cal", {"exchange": "SSE",
                                      "start_date": cur.strftime("%Y%m%d"),
                                      "end_date": end.strftime("%Y%m%d")},
                        "cal_date,is_open")
                    fields = calendar["fields"]
                    if not {"cal_date", "is_open"}.issubset(fields):
                        return None, None, None
                    flags = {}
                    for values in calendar["items"]:
                        if len(values) != len(fields):
                            return None, None, None
                        row = dict(zip(fields, values))
                        day, flag = str(row["cal_date"]), str(row["is_open"])
                        if flag not in ("0", "1") or day in flags:
                            return None, None, None
                        flags[day] = flag
                    closed_days = {day for day, flag in flags.items() if flag == "0"}
                except Exception:
                    return None, None, None
            if d8 not in closed_days:
                return None, None, None
            cur += timedelta(days=1)
            continue
        try:
            document = json.loads(path.read_text(encoding="utf-8"))
            fields = document["fields"]
            needed = "high" if direction == "down" else "low"
            if not {"ts_code", needed}.issubset(fields):
                return None, None, None
            matches = []
            for values in document["items"]:
                if len(values) != len(fields):
                    return None, None, None
                row = dict(zip(fields, values))
                if str(row["ts_code"]).split(".")[0] == code:
                    matches.append(row)
            if len(matches) != 1:
                return None, None, None
            raw = matches[0][needed]
            if isinstance(raw, bool):
                return None, None, None
            extreme = float(raw)
            if not math.isfinite(extreme) or extreme <= 0:
                return None, None, None
        except (ValueError, TypeError, KeyError, OSError):
            return None, None, None
        scanned += 1
        if ((direction in ("up", "flat") and extreme <= stop)
                or (direction == "down" and extreme >= stop)):
            return cur.isoformat(), stop, scanned
        cur += timedelta(days=1)
    return None, None, scanned

def _main_locked():
    dry = '--dry-run' in sys.argv
    judgments, j_bad = load_jsonl(J_FILE)
    results, r_bad = load_jsonl(R_FILE)
    if j_bad or r_bad:
        raise ValueError("damaged judgment/result ledger; settlement refused")
    from judgment_identity import (
        select_judgments, result_index, matching_result)
    selected = select_judgments(judgments)
    indexed_results = result_index(results)
    today = date.today().isoformat()
    due = [
        j for j in selected.values()
        if str(j.get("time_window_end", "9999")) <= today
        and matching_result(j, indexed_results) is None]

    report = {'today': today, 'judgments': len(judgments), 'results': len(results),
              'parse_errors': {'j': j_bad, 'r': r_bad}, 'due': len(due), 'settled_new': 0,
              'awaiting': 0, 'skipped': []}
    if not due:
        print(json.dumps(report, ensure_ascii=False, indent=1))
        return
    api = _get_api() if not dry else None
    out_lines = []
    for j in due:
        import math
        sym, win = j.get('symbol'), str(j.get('time_window_end', ''))
        jday = str(j.get('timestamp', ''))[:10]
        try:
            if not isinstance(sym, str) or not sym:
                raise ValueError("symbol required")
            start_day, end_day = date.fromisoformat(jday), date.fromisoformat(win)
            if end_day < start_day or j.get("direction") not in ("up", "down", "flat"):
                raise ValueError("invalid judgment window or direction")
            stop_value = j.get("stop_loss")
            if stop_value is not None:
                if (isinstance(stop_value, bool)
                        or not math.isfinite(float(stop_value))
                        or float(stop_value) <= 0):
                    raise ValueError("invalid stop price")
        except (ValueError, TypeError, OverflowError):
            report["skipped"].append({
                "symbol": sym, "window": win,
                "reason": "判断日期、方向或止损字段非法；未结算"})
            continue
        cm_j, src_j, jday_used = (close_map(api, jday) if api else (None, 'dry', None))
        cm_w, src_w, win_used = (close_map(api, win) if api else (None, 'dry', None))
        pj = (cm_j or {}).get(sym)
        pw = (cm_w or {}).get(sym)
        if any(
                isinstance(value, bool)
                or not isinstance(value, (int, float))
                or not math.isfinite(value) or value <= 0
                for value in (pj, pw)):
            report['skipped'].append({'symbol': sym, 'window': win,
                                       'reason': f"价格缺失 jday={src_j} win={src_w}"})
            continue
        # 23b止损结算语义: 窗口期内触发 -> 按止损事件结算 (2026-09-06签字)
        stop_hit_day, stop_px, scanned_days = scan_stop_hit(
            sym, jday, win, j.get('stop_loss'), j.get('direction'), api=api)
        if j.get("stop_loss") is not None and scanned_days is None:
            report["awaiting"] += 1
            report["skipped"].append({
                "symbol": sym, "window": win,
                "reason": "止损扫描覆盖未知；等待行情或交易日历，不写结算结果"})
            continue
        if stop_hit_day:
            row = {'symbol': sym, 'window_end': win,
                   'model_version': str(j.get('model_version') or ''),  # P0撞键修复: 透传账本维度. b335: 默认''与due查询侧对齐——无mv行归legacy遮蔽防重复写入(b330孪生缝隙)
                   'actual_direction': 'down' if j.get('direction') in ('up', 'flat') else 'up',
                   'actual_return': round((stop_px - pj) / pj, 4),
                   'close_price': stop_px,
                   'timestamp': datetime.now().isoformat(timespec='seconds'),
                   'judge_meta': {'judge_day_close': pj, 'judge_day': jday,
                                   'judge_day_used': jday_used, 'window_end_used': win_used,
                                   'source': f'stop_scan({scanned_days}d)',
                                   'stop_hit_day': stop_hit_day, 'stop_price': stop_px,
                                   'band': None, 'hit': False,
                                   'note': '止损触发结算(23b): 不用窗口末日收盘'}}
            if "judgment_id" in j:
                row["judgment_id"] = j["judgment_id"]
            out_lines.append(json.dumps(row, ensure_ascii=False, allow_nan=False))
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
               'model_version': str(j.get('model_version') or ''),  # P0撞键修复: 透传账本维度. b335: 默认''与查询侧对齐(同上)
               'actual_direction': v['actual_direction'],
               'actual_return': round(p_change, 4),
               'close_price': pw,
               'timestamp': datetime.now().isoformat(timespec='seconds'),
               'judge_meta': {'judge_day_close': pj, 'judge_day': jday,
                               'judge_day_used': jday_used, 'window_end_used': win_used,
                               'source': f"{src_j}/{src_w}",
                               'band': FLAT_BAND,
                               'hit': v['hit'],
                               'stop_scan': scanned_days}}  # 23b披露: 有止损未触发时标注扫描覆盖天数(本地K线缺日->覆盖不全->人工复核)
        if "judgment_id" in j:
            row["judgment_id"] = j["judgment_id"]
        out_lines.append(json.dumps(row, ensure_ascii=False, allow_nan=False))
        report['settled_new'] += 1
    if out_lines and not dry:
        from ledger_io import atomic_write_bytes
        # main() holds the shared lock across recovery, reads and replacement.
        # Preserve existing history byte-for-byte; commit this result batch once.
        existing = R_FILE.read_bytes() if R_FILE.exists() else b""
        separator = (
            b"\n" if existing and not existing.endswith((b"\n", b"\r")) else b"")
        addition = ("\n".join(out_lines) + "\n").encode("utf-8")
        atomic_write_bytes(R_FILE, existing + separator + addition)
    print(json.dumps(report, ensure_ascii=False, indent=1))

def main():
    # Use actual ledger paths, not an implicit production directory.
    root = J_FILE.parent
    if R_FILE.parent.resolve() != root.resolve():
        raise ValueError("judgment and result ledgers must share a directory")
    allowed = {
        "paper_positions.json", "paper_trades.jsonl",
        "paper_account.json", J_FILE.name,
    }
    lock = FileLock(str(root / "guanlan.lock"), timeout=60)
    with recovered_access(root, allowed, lock):
        return _main_locked()


if __name__ == '__main__':
    main()