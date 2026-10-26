# -*- coding: utf-8 -*-
"""GL-JCL 观澜判断校准实验室 — paper_trading.py 批1 (2026-10-14)
架构: 瑶序host引用传递裁决——main._paper_dispatch转发壳传入host=globals(), 本模块零import main, 循环import根除
设计: paper_trading_design_v1.md v1.4 (制度等价十条收编, 翔10-14 11:38批)
判例落地: Nova b326/b327审查(缺键即拒契约/哨兵隔离/active函数内过滤) + 观澜Q1-Q4签字 + #36a部分平仓禁摊薄
验收链: 观澜2026-10-14 15:30签收main.py阶段(b326+b327), 本文件为施工顺序第2步
"""
import json
import os
import math
from decimal import Decimal
from datetime import datetime, date, timedelta
from pathlib import Path
from contextvars import ContextVar
from ledger_batch import LedgerBatch, CommittedOutcomeError
from ledger_guard import recovered_access
import request_receipts as _receipts

_ACTIVE_BATCH = ContextVar("paper_active_batch", default=None)

def _batch_target(path):
    batch = _ACTIVE_BATCH.get()
    if batch is None:
        raise ValueError("paper ledger access requires transaction context")
    target = Path(path)
    if target.parent.resolve() != batch.store.root:
        raise ValueError("paper ledger outside transaction directory")
    batch.store._path(target.name)
    return batch, target.name

def _ledger_bytes(path):
    batch, name = _batch_target(path)
    return batch.read_bytes(name)

def _stage_json(path, value):
    batch, name = _batch_target(path)
    batch.stage_json(name, value)

def _stage_append(path, row):
    batch, name = _batch_target(path)
    batch.append_jsonl(name, row)

PLUGIN_DIR = os.path.dirname(os.path.abspath(__file__))
P_POSITIONS = os.path.join(PLUGIN_DIR, "paper_positions.json")
P_TRADES = os.path.join(PLUGIN_DIR, "paper_trades.jsonl")
P_ACCOUNT = os.path.join(PLUGIN_DIR, "paper_account.json")
P_SNAPDIR = os.path.join(PLUGIN_DIR, "paper_snapshots")
P_JUDGMENTS = os.path.join(PLUGIN_DIR, "judgments.jsonl")  # 设计§3.1行为5: paper行混入judgments(model_version区分), settle三元组对齐(批1第4步)

PAPER_CAPITAL_INIT = 10000.0  # v1.4 §4: 虚拟本金与real锚(14201.77)解耦, 防锚缺陷传染
MAX_HOLD_NATURAL_DAYS = 28    # §7: 最长20交易日≈28自然日(time_expiry), settle close_map回退自动对齐(#9判例)

BUY_INTENTS = {"trend_follow", "mean_reversion", "value_breaknet", "event_driven", "intuition_test", "random_baseline"}
SELL_INTENTS = {"stop_loss_hit", "target_hit", "logic_invalidated", "time_expiry", "discipline", "partial_profit"}
GROUPS = {"exp", "ctrl_a", "ctrl_b"}
GROUP_INTENT = {"ctrl_a": "intuition_test", "ctrl_b": "random_baseline"}  # §2.5枚举联动

# ========== IO层 (judgments容灾标准同权: 原子写/append-only/末行换行防御2026-09-06判例) ==========

def _write_json_atomic(path, obj):
    from ledger_io import atomic_write_json
    atomic_write_json(path, obj)

def read_paper_positions():
    try:
        if _ACTIVE_BATCH.get() is not None:
            raw = _ledger_bytes(P_POSITIONS)
            if raw is None:
                return []
            obj = json.loads(raw)
        else:
            if not os.path.exists(P_POSITIONS):
                return []
            with open(P_POSITIONS, "r", encoding="utf-8") as f:
                obj = json.load(f)
        if not isinstance(obj, dict) or not isinstance(obj.get("positions"), list):
            raise ValueError("positions must be an explicit list")
        for p in obj["positions"]:
            if (not isinstance(p, dict)
                    or not isinstance(p.get("symbol"), str) or not p["symbol"]
                    or p.get("status") not in ("active", "closed")):
                raise ValueError("invalid paper position identity or status")
            if p["status"] != "active":
                continue
            shares = p.get("shares")
            if isinstance(shares, bool) or not isinstance(shares, int) or shares <= 0:
                raise ValueError("paper position requires positive integer shares")
            for field in ("cost", "stop_loss", "target"):
                value = p.get(field)
                if (isinstance(value, bool) or not isinstance(value, (int, float))
                        or not math.isfinite(value) or value <= 0):
                    raise ValueError("invalid paper position price")
            if p.get("group") not in GROUPS:
                raise ValueError("invalid paper position group")
            if ("pending_action" in p
                    and not isinstance(p["pending_action"], dict)):
                raise ValueError("invalid pending paper action")
        return obj["positions"]
    except Exception as exc:
        raise ValueError("paper positions unreadable; refusing operation") from exc

def save_paper_positions(positions, host):
    with host["DATA_LOCK"]:
        value = {"updated": datetime.now().strftime("%Y-%m-%d"),
                 "positions": positions}
        if _ACTIVE_BATCH.get() is not None:
            _stage_json(P_POSITIONS, value)
        else:
            _write_json_atomic(P_POSITIONS, value)

def read_paper_trades():
    rows = []
    if _ACTIVE_BATCH.get() is not None:
        raw = _ledger_bytes(P_TRADES)
        if raw is None:
            return rows
        text = raw.decode("utf-8")
    else:
        if not os.path.exists(P_TRADES):
            return rows
        with open(P_TRADES, "r", encoding="utf-8") as f:
            text = f.read()
    for line in text.splitlines():
        line = line.strip()
        if not line:
            continue
        try:
            row = json.loads(line)
        except json.JSONDecodeError as exc:
            raise ValueError("paper trades contain invalid JSON; refusing operation") from exc
        if not isinstance(row, dict):
            raise ValueError("paper trade row must be an object")
        if row.get("action") in ("buy", "sell"):
            if not isinstance(row.get("symbol"), str) or not row["symbol"]:
                raise ValueError("paper trade symbol required")
            trade_date = row.get("date")
            if not isinstance(trade_date, str):
                raise ValueError("paper trade date required")
            if datetime.strptime(trade_date, "%Y-%m-%d").strftime("%Y-%m-%d") != trade_date:
                raise ValueError("invalid paper trade date")
            quantity = row.get("shares")
            if (isinstance(quantity, bool) or not isinstance(quantity, int)
                    or quantity <= 0):
                raise ValueError("invalid paper trade quantity")
            fields = ("price", "pnl") if row["action"] == "sell" else ("price",)
            for field in fields:
                value = row.get(field)
                if (isinstance(value, bool) or not isinstance(value, (int, float))
                        or not math.isfinite(value)
                        or (field == "price" and value <= 0)):
                    raise ValueError("invalid paper trade numeric field")
        rows.append(row)
    return rows

def append_paper_trade(row, host):
    with host["DATA_LOCK"]:
        if _ACTIVE_BATCH.get() is not None:
            _stage_append(P_TRADES, row)
            return
        needs_nl = False
        if os.path.exists(P_TRADES) and os.path.getsize(P_TRADES) > 0:
            with open(P_TRADES, "rb") as f:
                f.seek(os.path.getsize(P_TRADES) - 1)
                needs_nl = f.read(1) not in (b"\n", b"\r")
        with open(P_TRADES, "a", encoding="utf-8") as f:
            if needs_nl:
                f.write("\n")
            f.write(json.dumps(row, ensure_ascii=False) + "\n")

def read_paper_account():
    def validate(account):
        if not isinstance(account, dict):
            raise ValueError("paper account must be an object")
        for key in ("paper_capital", "available_cash"):
            value = account.get(key)
            if (isinstance(value, bool) or not isinstance(value, (int, float))
                    or not math.isfinite(value)):
                raise ValueError("paper account requires finite amounts")
        if account["paper_capital"] < 0:
            raise ValueError("paper capital cannot be negative")
        if ("_booking_receipts_v1" in account
                and not isinstance(account["_booking_receipts_v1"], dict)):
            raise ValueError("paper receipt ledger invalid")
        return account

    try:
        if _ACTIVE_BATCH.get() is not None:
            raw = _ledger_bytes(P_ACCOUNT)
            if raw is not None:
                return validate(json.loads(raw))
        elif os.path.exists(P_ACCOUNT):
            with open(P_ACCOUNT, "r", encoding="utf-8") as f:
                return validate(json.load(f))
        # Missing account is initialization only for a genuinely unbooked
        # portfolio. Never recreate capital over an existing trading history.
        if (any(p.get("status") == "active" for p in read_paper_positions())
                or any(t.get("action") in ("buy", "sell")
                       for t in read_paper_trades())):
            raise ValueError("paper account missing over existing bookings")
        return {"paper_capital": PAPER_CAPITAL_INIT,
                "available_cash": PAPER_CAPITAL_INIT,
                "updated": datetime.now().strftime("%Y-%m-%d"),
                "cash_events": []}
    except Exception as exc:
        raise ValueError("paper account unreadable; refusing operation") from exc

def save_paper_account(acct, host):
    with host["DATA_LOCK"]:
        if _ACTIVE_BATCH.get() is not None:
            _stage_json(P_ACCOUNT, acct)
        else:
            _write_json_atomic(P_ACCOUNT, acct)

def append_judgment_row(row, host):
    """设计§3.1行为5: conviction带上时同步写judgments行(model_version=paper-v0).
    evidence强制指针(2026-08-21判例): 无快照文件名不入账."""
    with host["DATA_LOCK"]:
        if _ACTIVE_BATCH.get() is not None:
            _stage_append(P_JUDGMENTS, row)
            return
        needs_nl = False
        if os.path.exists(P_JUDGMENTS) and os.path.getsize(P_JUDGMENTS) > 0:
            with open(P_JUDGMENTS, "rb") as f:
                f.seek(os.path.getsize(P_JUDGMENTS) - 1)
                needs_nl = f.read(1) not in (b"\n", b"\r")
        with open(P_JUDGMENTS, "a", encoding="utf-8") as f:
            if needs_nl:
                f.write("\n")
            f.write(json.dumps(row, ensure_ascii=False) + "\n")

def _build_ledger():
    """闸注入账本——b327契约全键携带(trades/capital/positions必需, cleared_until可选).
    cleared_until取paper自己的(不读real risk_state, Nova P2哨兵隔离的注入侧配合)."""
    acct = read_paper_account()
    return {"trades": read_paper_trades(),
            "capital": float(acct.get("paper_capital", 0.0)),
            "positions": read_paper_positions(),
            "cleared_until": str(acct.get("loss_halt_cleared_until", ""))}

def _log_rejected(symbol, action, rej, group, intent, host):
    """rejected行落paper_trades (v1.4 §3.1行为1: 拒单记录=框架空头期正确行为证据链, 周报输出exp组N单全拒)"""
    row = {"symbol": symbol, "action": action + "_rejected", "date": datetime.now().strftime("%Y-%m-%d"),
           "gate": rej.get("gate"), "reason_code": rej.get("reason", ""), "message": str(rej.get("message", ""))[:200],
           "group": group or "", "intent": intent or ""}
    if "calc" in rej:
        row["calc"] = rej["calc"]
    append_paper_trade(row, host)

# ========== 制度等价四件套 (v1.4 §2.6, 观澜Q1/Q2签字 2026-10-14) ==========

def _limit_band(symbol, name):
    """涨跌停带宽矩阵: 68科创/30创业恒±20%(注册制无ST降幅——观澜事实修正v1.4);
    主板±10%; 名称*ST/ST/退市整理±5% (34b判例同源: 名称前缀判ST, 不另查industry_map);
    北交所43/83/87/92恒±30% (b336 Nova终审P2-1安全网——主修=ctrl_b抽样排除, 此档防手动提名盲区)"""
    if str(symbol).startswith(("68", "30")):
        return 0.20
    if str(symbol).startswith(("43", "83", "87", "92")):
        return 0.30
    n = str(name or "")
    if n.startswith("*ST") or n.startswith("ST") or n.startswith("退"):
        return 0.05
    return 0.10

def _check_market_rules(symbol, quote, side, host=None, *, confirmed_day=None):
    """制度等价校验段(v1.4 §3.1): 停牌拒单 / 一字板双条件拒单(四值相等 AND ==涨跌停价, 防缩量十字星误杀) /
    OHLC缺失宁拒勿假(limit_check_degraded, 观澜Q2签字) / 行情失败显式拒单禁fallback收盘价(v1.3补丁④).
    返回: None=通过 / {"status":"rejected"} / {"status":"deferred"}(卖侧一字跌停转顺延族)"""
    if not isinstance(quote, dict) or quote.get("error"):
        return {"status": "rejected", "gate": "market_rule", "reason": "quote_unavailable",
                "message": "行情获取失败, 显式拒单禁fallback收盘价 (v1.3补丁④)"}
    # Simulated fills require a live executable session, not a dated close.
    from datetime import timezone, time as clock_time
    china = timezone(timedelta(hours=8))
    now = datetime.now(china)
    session = now.time().replace(tzinfo=None)
    if not (clock_time(9, 30) <= session < clock_time(11, 30)
            or clock_time(13, 0) <= session < clock_time(14, 57)):
        return {"status": "rejected", "gate": "market_rule",
                "reason": "outside_continuous_session",
                "message": "模拟成交仅限连续竞价时段；不模拟集合竞价成交"}
    try:
        raw_timestamp = quote.get("时间戳")
        if not isinstance(raw_timestamp, str) or not raw_timestamp.strip():
            raise ValueError("source timestamp missing")
        stamp = raw_timestamp.strip()
        if len(stamp) == 14 and stamp.isascii() and stamp.isdigit():
            quoted_at = datetime.strptime(stamp, "%Y%m%d%H%M%S").replace(tzinfo=china)
        else:
            quoted_at = datetime.fromisoformat(stamp)
            if quoted_at.tzinfo is None:
                quoted_at = quoted_at.replace(tzinfo=china)
            quoted_at = quoted_at.astimezone(china)
        age = (now - quoted_at).total_seconds()
        if quoted_at.date() != now.date() or not -5 <= age <= 120:
            raise ValueError("stale or future quote")
    except (ValueError, TypeError, OverflowError):
        return {"status": "rejected", "gate": "market_rule",
                "reason": "quote_timestamp_invalid_or_stale",
                "message": "源行情时间缺失、非法或过期，模拟成交拒绝"}
    try:
        if not isinstance(host, dict) or not callable(host.get("_tushare_api")):
            raise ValueError("calendar provider missing")
        day = now.strftime("%Y%m%d")
        if confirmed_day == day:
            # Internal same-operation reuse only; never persisted as a cache.
            calendar = {
                "fields": ["cal_date", "is_open"], "items": [[day, 1]]}
        else:
            calendar = host["_tushare_api"](
                "trade_cal", {"exchange": "SSE", "start_date": day, "end_date": day},
                "cal_date,is_open")
        if not isinstance(calendar, dict):
            raise ValueError("calendar unavailable")
        fields, items = calendar.get("fields"), calendar.get("items")
        if (not isinstance(fields, list)
                or any(not isinstance(field, str) for field in fields)
                or len(set(fields)) != len(fields)
                or not {"cal_date", "is_open"}.issubset(fields)
                or not isinstance(items, list) or len(items) != 1):
            raise ValueError("invalid calendar")
        if not isinstance(items[0], (list, tuple)) or len(items[0]) != len(fields):
            raise ValueError("invalid calendar row")
        row = dict(zip(fields, items[0]))
        if str(row.get("cal_date")) != day or str(row.get("is_open")) != "1":
            raise ValueError("trading day not confirmed")
    except Exception:
        return {"status": "rejected", "gate": "market_rule",
                "reason": "trading_day_unconfirmed",
                "message": "交易日历未确认今日开市，模拟成交拒绝"}
    # Calendar IO may cross a session boundary or exhaust the quote lifetime.
    # Recheck the clock only; reuse the confirmed day and source timestamp.
    checked_at = datetime.now(china)
    checked_session = checked_at.time().replace(tzinfo=None)
    if (checked_at.date() != now.date()
            or not (clock_time(9, 30) <= checked_session < clock_time(11, 30)
                    or clock_time(13, 0) <= checked_session < clock_time(14, 57))
            or not -5 <= (checked_at - quoted_at).total_seconds() <= 120):
        return {"status": "rejected", "gate": "market_rule",
                "reason": "quote_or_session_expired_during_validation",
                "message": "校验期间行情过期或交易时段结束；未使用旧观察成交"}
    try:
        values = {}
        for field in ("最新价", "成交量", "今开", "最高", "最低", "昨收"):
            raw = quote.get(field)
            if isinstance(raw, bool):
                raise ValueError("boolean quote value")
            number = 0.0 if raw is None or raw == "" else float(raw)
            if not math.isfinite(number) or number < 0:
                raise ValueError("nonfinite or negative quote value")
            values[field] = number
    except (ValueError, TypeError, OverflowError):
        return {"status": "rejected", "gate": "market_rule",
                "reason": "invalid_quote_numeric",
                "message": "行情数值非法、非有限或为负，拒绝使用"}
    px = values["最新价"]
    if px <= 0:
        return {"status": "rejected", "gate": "market_rule", "reason": "suspended_or_invalid",
                "message": "最新价无效(0), 疑似停牌, 拒单 (制度等价§2.6)"}
    if values["成交量"] == 0:
        return {"status": "rejected", "gate": "market_rule", "reason": "suspended_zero_volume",
                "message": "成交量0, 停牌判定, 拒单 (制度等价§2.6)"}
    op, hi, lo, pc = (values[k] for k in ("今开", "最高", "最低", "昨收"))
    if not (op and hi and lo and pc):
        return {"status": "rejected", "gate": "market_rule", "reason": "limit_check_degraded",
                "message": "OHLC字段不全(数据降级), 一字板判定不可靠, 宁拒勿假 (观澜Q2签字)"}
    if op == hi == lo == px:  # 双条件之一: 四值相等
        band = _limit_band(symbol, quote.get("名称") or "")
        lim_up, lim_dn = round(pc * (1 + band), 2), round(pc * (1 - band), 2)
        if side == "buy" and px == lim_up:
            return {"status": "rejected", "gate": "market_rule", "reason": "limit_up_locked",
                    "message": "一字涨停买不进, 拒单 (制度等价§2.6)"}
        if side == "sell" and px == lim_dn:
            return {"status": "deferred", "gate": "market_rule", "reason": "limit_down_locked",
                    "message": "一字跌停卖不出, 转顺延族次日执行 (Q4统一语义)"}
    return None

# ========== T+1与顺延族 (观澜Q1/Q4签字) ==========

_SETTLE = None

def _get_settle(host):
    """settle复用(瑶序裁决二): importlib加载, 顶层无副作用(main()在__main__ guard内), 交易日判定单一事实源."""
    global _SETTLE
    if _SETTLE is None:
        import importlib.util as ilu
        base = host.get("PLUGIN_DIR", PLUGIN_DIR)
        spec = ilu.spec_from_file_location("settle_results_gl", os.path.join(base, "settle_results.py"))
        _SETTLE = ilu.module_from_spec(spec)
        spec.loader.exec_module(_SETTLE)
    return _SETTLE

def _is_trade_day(d_iso, host):
    """交易日判定复用settle.local_close回退(观澜Q1签字: 数据源等级与settle一致防双源)."""
    return bool(_get_settle(host).local_close(d_iso.replace("-", "")))

def _t1_sellable(pos, host):
    """Date eligibility only; _check_market_rules must also confirm an open session.

    On a confirmed open trading day, a valid earlier purchase date is sufficient
    for T+1. No intermediate calendar query or local K-line proxy is needed.
    """
    from datetime import timezone
    raw_entry = pos.get("entry_date")
    if not isinstance(raw_entry, str):
        raise ValueError("entry date required for T+1")
    entry = date.fromisoformat(raw_entry)
    if entry.isoformat() != raw_entry:
        raise ValueError("invalid entry date for T+1")
    today = datetime.now(timezone(timedelta(hours=8))).date()
    if today == entry:
        return False, True
    if today < entry:
        raise ValueError("future entry date for T+1")
    return True, False

def _upsert_position(positions, pos, host):
    for i, p in enumerate(positions):
        if p.get("symbol") == pos.get("symbol") and p.get("entry_date") == pos.get("entry_date"):
            positions[i] = pos
            break
    else:
        positions.append(pos)
    save_paper_positions(positions, host)

# ========== 三命令 (§3.1/3.2/3.3) ==========

def _paper_buy(params, symbol, cmd, host):
    today = datetime.now().strftime("%Y-%m-%d")
    group = params.get("group") or cmd.get("group", "")
    intent = params.get("intent") or cmd.get("intent", "")
    expectation = params.get("expectation") or cmd.get("expectation", "")
    shares_raw = params.get("shares", cmd.get("shares"))
    try:
        if isinstance(shares_raw, bool):
            raise ValueError("boolean quantity")
        quantity = Decimal(str(shares_raw))
        if (not quantity.is_finite() or quantity <= 0
                or quantity != quantity.to_integral_value()):
            raise ValueError("quantity must be a positive integer")
        shares = int(quantity)
    except Exception:
        return {"status": "error", "message": "shares必须为正整数，不接受布尔值或小数"}
    stop_loss = params.get("stop_loss", cmd.get("stop_loss"))
    target = params.get("target", cmd.get("target"))
    reason = params.get("reason") or cmd.get("reason", "")
    override_market = params.get("override_market") or cmd.get("override_market")
    override_budget = params.get("override_budget") or cmd.get("override_budget")
    override_by = params.get("override_by") or cmd.get("override_by", "")
    override_reason = params.get("override_reason") or cmd.get("override_reason", "")
    conviction = params.get("conviction", cmd.get("conviction"))
    try:
        for label, value in (("stop_loss", stop_loss), ("target", target)):
            if isinstance(value, bool):
                raise ValueError(label)
            number = float(value)
            if not math.isfinite(number) or number <= 0:
                raise ValueError(label)
        stop_loss, target = float(stop_loss), float(target)
        if conviction not in (None, ""):
            if isinstance(conviction, bool):
                raise ValueError("conviction")
            conviction = float(conviction)
            if not math.isfinite(conviction) or not 0 <= conviction <= 1:
                raise ValueError("conviction")
    except (TypeError, ValueError, OverflowError):
        return {"status": "error",
                "message": "止损及目标必须为有限正数；conviction须为0至1的有限概率"}
    # --- 参数契约 ---
    if not symbol or group not in GROUPS or not shares or stop_loss in (None, "", 0) or not target or not expectation or not intent:
        return {"status": "error", "message": "缺少/无效必填参数: symbol/group(exp|ctrl_a|ctrl_b)/intent/expectation/shares/stop_loss/target (§3.1)"}
    if intent not in BUY_INTENTS:
        return {"status": "error", "message": "intent=%s不在buy枚举(%s) §2.5" % (intent, sorted(BUY_INTENTS))}
    if GROUP_INTENT.get(group) and intent != GROUP_INTENT[group]:
        return {"status": "error", "message": "%s组intent须=%s (§2.5联动)" % (group, GROUP_INTENT[group])}
    if shares <= 0 or shares % 100 != 0:
        return {"status": "error", "message": "买入须整手(100股整数倍), 当前%d股 (制度等价§2.6)" % shares}
    # --- override四键校验(M16真盘镜像main.L1880-1888, 拒得早零网络; b337) ---
    _ov_p = {}
    if override_market or override_budget:
        _ov_p = {"override_market": bool(override_market),
                 "override_budget": bool(override_budget),
                 "override_by": str(override_by or ""),
                 "override_reason": str(override_reason or "")}
        if not _ov_p["override_by"] or not _ov_p["override_reason"]:
            r = {"status": "rejected", "gate": "override_invalid",
                 "message": "拒单: override需完整四键(override_market/override_budget/override_by/override_reason), 终裁人和理由不得为空. (M16镜像)"}
            _log_rejected(symbol, "buy", r, group, intent, host)
            return r
    positions = read_paper_positions()
    for p in positions:
        if p["symbol"] == symbol and p.get("status") == "active":
            return {"status": "exists", "message": "%s已有活跃paper持仓" % symbol}
    # --- 行情+制度等价 ---
    quote = host["get_realtime_quote"](symbol)
    rej = _check_market_rules(symbol, quote, "buy", host=host)
    if rej is not None:
        if rej.get("status") == "rejected":
            _log_rejected(symbol, "buy", rej, group, intent, host)
        return rej
    from datetime import timezone
    confirmed_day = datetime.now(
        timezone(timedelta(hours=8))).strftime("%Y%m%d")
    px = float(quote["最新价"])
    # --- 风控闸(单一事实源, b327全键契约) ---
    # 翔2026-10-15 17:00架构裁决(v1.6): 判断闸降级附注不拦截——闸门是顾问不是守卫.
    # 判断闸=Rule6市场闸(gate=market_regime)+Rule2预算(calc含risk_amount): 意见写入gate_opinions随单留证, 建仓继续.
    # 纪律闸=Rule3连亏/Rule4日熔断/Rule5月闸 + 制度闸=Rule1止损/paper_cash/ledger_contract/市场规则: 保持拦截(训练目标本身).
    # 周报分组结算: framework_ok vs framework_says_no 两组胜率差 = 闸门校准终极数据.
    cfg = host["_load_risk_config"]()
    gate_opinions = []
    ledger = _build_ledger()
    check_override = dict(_ov_p)
    # Shared checker returns the FIRST failure. An advisory must not hide
    # later mandatory rules. At most two advisory bypasses, then a final check.
    for _attempt in range(3):
        gate = host["_risk_gate_check"](
            symbol, px, shares, float(stop_loss), cfg,
            override=check_override, ledger=ledger)
        if gate is None:
            break
        _calc = gate.get("calc", {}) or {}
        bypass_key = None
        if gate.get("status") == "rejected":
            if gate.get("gate") == "market_regime":
                bypass_key = "override_market"
            elif (gate.get("gate") == "pre_trade_risk"
                  and _calc.get("rule") == "single_trade_risk 2% floor"
                  and "risk_amount" in _calc):
                bypass_key = "override_budget"
        if bypass_key is None or check_override.get(bypass_key):
            _log_rejected(symbol, "buy", gate, group, intent, host)
            return gate
        gate_opinions.append({"gate": gate.get("gate"), "verdict": "framework_says_no",
                              "message": gate.get("message", ""), "calc": _calc,
                              "noted_at": datetime.now().isoformat(timespec="seconds"),
                              "authority": "翔2026-10-15裁决: 判断闸降级附注(v1.6)"})
        check_override[bypass_key] = True
    else:
        return {"status": "error", "gate": "risk_check_incomplete",
                "message": "风控链未完成检查，停止写账"}
    if _ov_p:
        reason = (reason or "") + " [OVERRIDE:%s: %s]" % (_ov_p["override_by"], _ov_p["override_reason"])
    # --- 资金(1手超预算应换替补, 禁特批——v1.4整手规则) ---
    fees = host["_calc_fees"](symbol, px, shares, "buy")
    cost_total = round(px * shares + fees["total_fee"], 2)
    acct = read_paper_account()
    if float(acct.get("available_cash", 0)) < cost_total:
        r = {"status": "rejected", "gate": "paper_cash",
             "message": "paper可用资金%.2f不足(需%.2f含费), 拒单——1手超预算应换替补不特批 (v1.4整手规则)" % (float(acct.get("available_cash", 0)), cost_total)}
        _log_rejected(symbol, "buy", r, group, intent, host)
        return r
    # Risk checks may perform network IO. Revalidate the SAME observation;
    # a new price would require rerunning all price-dependent risk checks.
    rej = _check_market_rules(
        symbol, quote, "buy", host=host, confirmed_day=confirmed_day)
    if rej is not None:
        _log_rejected(symbol, "buy", rej, group, intent, host)
        return rej
    # --- 快照出生证先行(v1.3补丁①: 落盘成功才写账; ③时间戳防同日撞车; ⑤data_quality) ---
    snap = {"snapshot_meta": {"symbol": symbol, "created_at": datetime.now().isoformat(timespec="seconds"),
                              "quote_timestamp": quote.get("时间戳"),
                              "captured_at": datetime.now().isoformat(timespec="seconds")},
            "quote": quote,
            "data_quality": {"source": quote.get("source") or "unknown",
                             "timestamp_available": bool(quote.get("时间戳")),
                             "degraded": (not quote.get("时间戳") or not all(
                                 quote.get(k) for k in ("最高", "最低", "今开", "昨收")))},
            "decision": {"group": group, "intent": intent, "expectation": expectation, "reason": reason,
                         "conviction": conviction, "shares": shares,
                         "stop_loss": float(stop_loss), "target": float(target)}}
    os.makedirs(P_SNAPDIR, exist_ok=True)
    import uuid
    snap_fname = "%s_%s_%s.json" % (
        datetime.now().strftime("%Y%m%d_%H%M%S_%f"), symbol, uuid.uuid4().hex)
    try:
        _write_json_atomic(os.path.join(P_SNAPDIR, snap_fname), snap)
    except Exception:
        return {"status": "error", "error_code": "snapshot_persistence_failed",
                "message": "快照落盘失败；未提交记账，请核对存储状态"}
    # --- 写账 ---
    actual_cost = round((px * shares + fees["total_fee"]) / shares, 4)
    positions.append({"symbol": symbol, "name": quote.get("名称") or host["_get_name"](symbol) or symbol,
                      "cost": actual_cost, "shares": int(shares), "stop_loss": float(stop_loss),
                      "target": float(target), "entry_date": today, "added": today,
                      "entry_reason": reason, "group": group, "intent": intent,
                      "expectation": expectation, "snapshot": snap_fname, "status": "active",
                      "gate_opinions": gate_opinions})
    save_paper_positions(positions, host)
    append_paper_trade({"symbol": symbol, "action": "buy", "price": px, "shares": int(shares),
                        "date": today, "group": group, "intent": intent, "fees": fees,
                        "snapshot": snap_fname, "reason": reason,
                        "gate_opinions": gate_opinions}, host)
    acct["available_cash"] = round(float(acct.get("available_cash", 0)) - cost_total, 2)
    acct["updated"] = today
    save_paper_account(acct, host)
    # --- judgments行(§3.1行为5: conviction带->judgments, model_version=paper-v0, evidence=快照指针) ---
    jd = None
    if conviction not in (None, ""):
        try:
            jd = {"timestamp": datetime.now().isoformat(timespec="seconds"), "symbol": symbol,
                  "judgment_id": "paper:" + snap_fname.rsplit("_", 1)[-1].removesuffix(".json"),
                  "direction": "up", "probability": float(conviction),
                  "time_window_end": (date.today() + timedelta(days=MAX_HOLD_NATURAL_DAYS)).isoformat(),
                  "stop_loss": float(stop_loss), "state": "paper_%s" % group,
                  "note": (expectation or reason)[:200], "agent": "观澜", "source": "paper-trade",
                  "evidence": "paper_snapshots/%s" % snap_fname,
                  "model_version": "paper-v0", "group": group,
                  "gate_verdict": ("framework_says_no" if gate_opinions else "framework_ok")}
            append_judgment_row(jd, host)
        except (TypeError, ValueError):
            # Probability was validated before staging. A failure here means
            # the evidence write failed: abort the entire booking transaction.
            raise ValueError("judgment evidence staging failed; booking aborted") from None
    # --- Q2耗尽监控(不重置, <50%报翔——批1回执内警告, 触发后由观澜日报上呈) ---
    warn = None
    if float(acct.get("paper_capital", 0)) > 0 and float(acct["available_cash"]) < float(acct["paper_capital"]) * 0.5:
        warn = "paper可用资金已低于总资本50%%(%.2f/%.2f), 耗尽监控 (Q2)" % (float(acct["available_cash"]), float(acct["paper_capital"]))
    return {"status": "added", "symbol": symbol, "price": px, "shares": shares,
            "cost_diluted": actual_cost, "fees": fees, "snapshot": snap_fname,
            "judgment": jd, "capital_warning": warn, "gate_opinions": gate_opinions,
            "message": "paper买入 %s @%.2f x%d 组=%s intent=%s%s" % (
                symbol, px, shares, group, intent,
                " [闸门附注: %s条判断闸意见留证, 架构裁决v1.6]" % len(gate_opinions) if gate_opinions else "")}

def _paper_sell(params, symbol, cmd, host):
    today = datetime.now().strftime("%Y-%m-%d")
    intent = params.get("intent") or cmd.get("intent", "")
    reason = params.get("reason") or cmd.get("reason", "")
    shares_provided = "shares" in params or "shares" in cmd
    shares_req = params["shares"] if "shares" in params else cmd.get("shares")
    if shares_provided:
        try:
            if isinstance(shares_req, bool):
                raise ValueError("boolean quantity")
            quantity = Decimal(str(shares_req))
            if (not quantity.is_finite() or quantity <= 0
                    or quantity != quantity.to_integral_value()):
                raise ValueError("quantity must be a positive integer")
            shares_req = int(quantity)
        except Exception:
            return {"status": "error",
                    "message": "显式卖出数量须为有限正整数；全平请省略shares"}
    if not symbol or intent not in SELL_INTENTS:
        return {"status": "error", "message": "缺少symbol或intent不在sell枚举(%s) §2.5" % sorted(SELL_INTENTS)}
    positions = read_paper_positions()
    pos = next((p for p in positions if p["symbol"] == symbol and p.get("status") == "active"), None)
    if pos is None:
        return {"status": "error", "message": "%s无活跃paper持仓" % symbol}
    close_shares = int(shares_req) if shares_provided else int(pos["shares"])
    if close_shares > int(pos["shares"]):
        close_shares = int(pos["shares"])
    if close_shares <= 0:
        return {"status": "error", "message": "卖出数量无效(%s)" % shares_req}
    # Preserve the first trigger across repeated calls and locked-limit days.
    pending = pos.get("pending_action")
    if pending:
        try:
            trigger_day = date.fromisoformat(pending["trigger_date"])
            trigger_price = pending["trigger_price"]
            if (pending.get("type") != "sell"
                    or trigger_day.isoformat() != pending["trigger_date"]
                    or trigger_day > date.fromisoformat(today)
                    or isinstance(trigger_price, bool)
                    or not isinstance(trigger_price, (int, float))
                    or not math.isfinite(trigger_price) or trigger_price <= 0):
                raise ValueError("invalid pending action")
        except (KeyError, TypeError, ValueError, OverflowError):
            return {"status": "error", "reason": "invalid_pending_action",
                    "message": "顺延记录非法；未执行卖出，请先核对原始触发证据"}
        if trigger_day == date.fromisoformat(today):
            return {"status": "deferred", "gate": "pending_next_day",
                    "reason": "pending_trigger_day",
                    "message": "已有当日顺延记录；保留首次触发证据，不在触发日重放成交"}
    # Validate the observation before registering even a deferred action.
    # Reuse this quote and verdict below; do not fetch/calendar-check twice.
    quote = host["get_realtime_quote"](symbol)
    rej = _check_market_rules(symbol, quote, "sell", host=host)
    if rej is not None and rej.get("status") != "deferred":
        _log_rejected(symbol, "sell", rej, pos.get("group", ""), intent, host)
        return rej
    # --- T+1(Q1) + 顺延族登记(Q4) ---
    sellable, is_t_day = _t1_sellable(pos, host)
    if not sellable:
        if is_t_day and intent == "stop_loss_hit":
            pos["pending_action"] = {"type": "sell", "intent": intent, "trigger_date": today,
                                     "trigger_price": float(pos.get("stop_loss") or 0),
                                     "slippage_class": "exec_delayed"}
            _upsert_position(positions, pos, host)
            return {"status": "deferred", "gate": "t_plus_1", "reason": "t1_stop_deferred", "intent": intent,
                    "message": "T+1当日不可卖; 止损触发已登记顺延(trigger=%.2f), 次日paper_sell自动按首笔有效价执行+exec_delayed (Q1/Q4)" % float(pos.get("stop_loss") or 0)}
        return {"status": "rejected", "gate": "t_plus_1", "reason": "t1_locked",
                "message": "T+1约束: %s买入今日不可卖 (Q1)" % pos.get("entry_date")}
    if rej is not None:
        if rej.get("status") == "deferred":  # 一字跌停 -> 顺延族
            if not pending:
                pos["pending_action"] = {
                    "type": "sell", "intent": intent, "trigger_date": today,
                    "trigger_price": float(quote["最新价"]),
                    "slippage_class": "exec_delayed"}
                _upsert_position(positions, pos, host)
            return rej
        _log_rejected(symbol, "sell", rej, pos.get("group", ""), intent, host)
        return rej
    px = float(quote["最新价"])
    # --- 顺延执行态: pending存在 -> 本单即顺延成交, 结算exec_slippage(制度损耗exec_delayed, 观澜Q4双分类) ---
    pend = pos.get("pending_action")
    exec_meta = None
    if pend:
        trig_px = float(pend.get("trigger_price") or 0)
        exec_meta = {"exec_type": "deferred_sell", "trigger_date": pend.get("trigger_date"),
                     "trigger_price": trig_px, "exec_price": px,
                     "exec_slippage": (round(px - trig_px, 4) if trig_px > 0 else None),
                     "slippage_class": pend.get("slippage_class", "exec_delayed")}
    # --- 费率结算 + #36a教训: 部分平仓剩余成本保持原单价禁摊薄 ---
    fees = host["_calc_fees"](symbol, px, close_shares, "sell")
    raw_amount = round(px * close_shares, 2)
    return_total = round(raw_amount - fees["total_fee"], 2)
    cost_basis = round(float(pos["cost"]) * close_shares, 2)
    pnl = round(return_total - cost_basis, 2)
    acct = read_paper_account()
    acct["available_cash"] = round(float(acct.get("available_cash", 0)) + return_total, 2)
    acct["updated"] = today
    save_paper_account(acct, host)  # paper_capital初始锚不动(Q2不重置), 累计已实现月报从trades聚合
    trade_row = {"symbol": symbol, "action": "sell", "price": px, "shares": close_shares,
                 "date": today, "intent": intent, "reason": reason, "fees": fees, "pnl": pnl,
                 "group": pos.get("group", ""), "entry_date": pos.get("entry_date")}
    if exec_meta:
        trade_row.update(exec_meta)
        if close_shares >= int(pos["shares"]):
            pos.pop("pending_action", None)
    append_paper_trade(trade_row, host)
    if close_shares >= int(pos["shares"]):
        pos["status"] = "closed"
        pos["closed_date"] = today
        pos["exit_price"] = px
        pos["pnl"] = pnl
    else:
        pos["shares"] = int(pos["shares"]) - close_shares  # cost字段不动(#36a)
    _upsert_position(positions, pos, host)
    return {"status": "closed", "symbol": symbol, "price": px, "shares": close_shares,
            "pnl": pnl, "fees": fees, "intent": intent, "exec": exec_meta,
            "message": "paper卖出 %s @%.2f x%d pnl=%.2f intent=%s%s" % (symbol, px, close_shares, pnl, intent, " [顺延执行exec_delayed]" if exec_meta else "")}

def _paper_portfolio(params, symbol, cmd, host):
    positions = read_paper_positions()
    acct = read_paper_account()
    actives = [p for p in positions if p.get("status") == "active"]
    rows = []
    for p in actives:
        q = host["get_realtime_quote"](p["symbol"])
        try:
            if not isinstance(q, dict) or q.get("error"):
                raise ValueError("quote unavailable")
            raw_price = q.get("最新价")
            if isinstance(raw_price, bool):
                raise ValueError("boolean quote price")
            px = float(raw_price)
            if not math.isfinite(px) or px <= 0:
                raise ValueError("invalid quote price")
        except (ValueError, TypeError, OverflowError):
            px = 0
        rows.append({"symbol": p["symbol"], "name": p.get("name"), "group": p.get("group"),
                     "cost": p.get("cost"), "shares": p.get("shares"), "price": px,
                     "unrealized_pnl": (round((px - float(p["cost"])) * int(p["shares"]), 2) if px > 0 else None),
                     "to_stop_pct": (round((float(p["stop_loss"]) / px - 1) * 100, 2) if px > 0 else None),
                     "to_target_pct": (round((float(p["target"]) / px - 1) * 100, 2) if px > 0 else None),
                     "stop_loss": p.get("stop_loss"), "target": p.get("target"),
                     "stop_hit": (px <= float(p["stop_loss"]) if px > 0 else None),
                     "target_hit": (px >= float(p["target"]) if px > 0 else None),
                     "quote_available": px > 0,
                     "quote_timestamp": q.get("时间戳") if isinstance(q, dict) else None,
                     "quote_source": q.get("source") if isinstance(q, dict) else None,
                     "entry_date": p.get("entry_date"), "pending": bool(p.get("pending_action"))})
    grp = {}
    for p in actives:
        g = p.get("group", "?")
        grp.setdefault(g, {"count": 0, "cost": 0.0})
        grp[g]["count"] += 1
        grp[g]["cost"] = round(grp[g]["cost"] + float(p.get("cost", 0)) * int(p.get("shares", 0)), 2)
    trades = read_paper_trades()
    realized = round(sum(float(t.get("pnl", 0)) for t in trades if t.get("action") == "sell"), 2)
    real_actives = [p for p in host["read_positions"]() if p.get("status") == "active"]
    cap_warn = (float(acct.get("paper_capital", 0)) > 0
                and float(acct.get("available_cash", 0)) < float(acct.get("paper_capital", 0)) * 0.5)
    missing_quotes = [r["symbol"] for r in rows if not r["quote_available"]]
    known_unrealized = round(sum(r["unrealized_pnl"] for r in rows
                                 if r["unrealized_pnl"] is not None), 2)
    return {"paper_capital": acct.get("paper_capital"), "available_cash": acct.get("available_cash"),
            "realized_total": realized,
            "valuation_complete": not missing_quotes,
            "missing_quotes": missing_quotes,
            "unrealized_known_total": known_unrealized,
            "unrealized_total": (known_unrealized if not missing_quotes else None),
            "positions": rows, "groups": grp,
            "real_contrast": {"active_count": len(real_actives), "symbols": [p["symbol"] for p in real_actives]},
            "capital_warning": ("available<50%%capital(%.2f/%.2f), 耗尽监控 (Q2)" % (float(acct.get("available_cash", 0)), float(acct.get("paper_capital", 0)))) if cap_warn else None,
            "note": "批1: 止损触发=手动paper_sell(intent=stop_loss_hit); 周报巡检兜底delayed_execution入档(纪律损耗列)"}

# ========== 转发壳入口 (main._paper_dispatch -> handle) ==========

def _paper_request_identity(action, params, symbol, cmd):
    """Fingerprint explicit business inputs, never raw command metadata.

    Input representation changes may conservatively conflict; do not coerce
    booleans/fractional quantities here and bypass business validation.
    """
    left = params.get("request_id")
    right = cmd.get("request_id")
    if left is not None and right is not None and left != right:
        raise _receipts.ReceiptError("request_id fields disagree")
    key = _receipts.request_key(left if left is not None else right)
    if key is None:
        return None, None
    arguments = {"symbol": symbol}
    if action == "paper_buy":
        defaults = {
            "group": "", "intent": "", "expectation": "",
            "stop_loss": None, "target": None, "reason": "",
            "override_market": None, "override_budget": None,
            "override_by": "", "override_reason": "",
        }
        for field, default in defaults.items():
            if field in ("stop_loss", "target"):
                arguments[field] = params.get(field, cmd.get(field, default))
            else:
                arguments[field] = params.get(field) or cmd.get(field, default)
        for field in ("shares", "conviction"):
            arguments[field] = params.get(field, cmd.get(field))
    elif action == "paper_sell":
        arguments["intent"] = params.get("intent") or cmd.get("intent", "")
        arguments["reason"] = params.get("reason") or cmd.get("reason", "")
        arguments["shares_provided"] = "shares" in params or "shares" in cmd
        arguments["shares"] = (
            params["shares"] if "shares" in params else cmd.get("shares"))
    else:
        raise _receipts.ReceiptError("request_id requires a booking command")
    return key, _receipts.fingerprint(action, arguments)

def handle(action, params, symbol, cmd, host=None):
    if host is None:
        return {"status": "error", "message": "host未注入"}
    try:
        handlers = {
            "paper_buy": _paper_buy, "paper_sell": _paper_sell,
            "paper_portfolio": _paper_portfolio,
        }
        if action not in handlers:
            return {"status": "error", "message": "未知paper命令"}
        if _ACTIVE_BATCH.get() is not None:
            raise ValueError("nested paper transaction refused")
        paths = [Path(p) for p in (
            P_POSITIONS, P_TRADES, P_ACCOUNT, P_JUDGMENTS)]
        root = paths[0].parent.resolve()
        if any(p.parent.resolve() != root for p in paths):
            raise ValueError("paper ledgers must share a directory")
        names = {p.name for p in paths}
        if len(names) != len(paths):
            raise ValueError("paper ledger filenames must be distinct")
        with recovered_access(root, names, host["DATA_LOCK"]) as store:
            batch = LedgerBatch(store)
            token = _ACTIVE_BATCH.set(batch)
            try:
                request_id, digest = _paper_request_identity(
                    action, params or {}, symbol, cmd or {})
                if request_id is not None:
                    previous = _receipts.lookup(
                        read_paper_account(), request_id, digest)
                    if previous is not None:
                        batch.discard()
                        return previous
                result = handlers[action](
                    params or {}, symbol, cmd or {}, host)
                if not isinstance(result, dict):
                    raise ValueError("paper handler returned invalid result")
                if result.get("status") == "error":
                    batch.discard()
                else:
                    if request_id is not None:
                        account = _receipts.record(
                            read_paper_account(), request_id, digest, result)
                        save_paper_account(account, host)
                    batch.commit()
                return result
            finally:
                _ACTIVE_BATCH.reset(token)
    except _receipts.ReceiptConflict:
        return {
            "status": "error", "error_code": "request_id_conflict",
            "retry_safe": False,
            "message": "request_id已用于不同的记账请求；未执行本次操作",
        }
    except CommittedOutcomeError:
        return {
            "status": "committed_needs_reconciliation",
            "committed": True, "retry_safe": False,
            "message": "账本已提交但回执或清理异常；先核对账本，禁止直接重试",
        }
    except Exception as e:
        return {
            "status": "error", "retry_safe": False,
            "message": "paper操作失败；核对恢复状态后再决定是否重试 (%s)"
                       % type(e).__name__,
        }