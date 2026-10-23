"""Validated end-of-day temperature inputs; no filesystem writes."""
import math
import re
import statistics
from datetime import datetime, timedelta, timezone


def load_inputs(api, fetch_up, fetch_down, now=None):
    now = now or datetime.now(timezone(timedelta(hours=8)))
    now = now.astimezone(timezone(timedelta(hours=8)))
    end = now.date()
    if now.hour < 15:
        end -= timedelta(days=1)
    start = end - timedelta(days=40)

    def table(name, params, required):
        data = api(name, params, ",".join(required))
        if not isinstance(data, dict):
            raise ValueError("source unavailable")
        fields, items = data.get("fields"), data.get("items")
        if (not isinstance(fields, list) or
                any(not isinstance(f, str) for f in fields) or
                len(set(fields)) != len(fields) or
                not set(required).issubset(fields) or
                not isinstance(items, list)):
            raise ValueError("invalid source schema")
        rows = []
        for item in items:
            if not isinstance(item, (list, tuple)) or len(item) != len(fields):
                raise ValueError("invalid source row")
            rows.append(dict(zip(fields, item)))
        return rows

    calendar = table("trade_cal", {
        "exchange": "SSE", "start_date": start.strftime("%Y%m%d"),
        "end_date": end.strftime("%Y%m%d")}, ["cal_date", "is_open"])
    flags = {}
    for row in calendar:
        stamp = row["cal_date"]
        if not isinstance(stamp, str) or not re.fullmatch(r"[0-9]{8}", stamp):
            raise ValueError("invalid calendar date")
        day = datetime.strptime(stamp, "%Y%m%d").date()
        flag = str(row["is_open"])
        if day in flags or not start <= day <= end or flag not in ("0", "1"):
            raise ValueError("invalid calendar coverage")
        flags[day] = flag
    cursor = end
    while cursor >= start:
        if cursor not in flags:
            raise ValueError("calendar gap")
        if flags[cursor] == "1":
            break
        cursor -= timedelta(days=1)
    else:
        raise ValueError("completed session unavailable")
    day = cursor.strftime("%Y%m%d")

    def keyed(name, columns):
        rows = table(name, {"trade_date": day},
                     ["ts_code", "trade_date"] + columns)
        result = {}
        for row in rows:
            code = row["ts_code"]
            if (not isinstance(code, str) or
                    not re.fullmatch(r"[0-9]{6}\.(SH|SZ|BJ)", code) or
                    code in result or row["trade_date"] != day):
                raise ValueError("invalid daily identity")
            for column in columns:
                value = row[column]
                if (isinstance(value, bool) or
                        not isinstance(value, (int, float)) or
                        not math.isfinite(value) or
                        (column != "pct_chg" and value < 0)):
                    raise ValueError("invalid daily number")
            result[code] = row
        if not result:
            raise ValueError("empty daily data")
        return result

    daily = keyed("daily", ["pct_chg", "amount"])
    basic = keyed("daily_basic", ["turnover_rate"])
    if set(daily) != set(basic):
        raise ValueError("daily and turnover coverage differs")
    codes = {code.split(".")[0] for code in daily}
    if len(codes) != len(daily):
        raise ValueError("ambiguous market identities")

    def pool(fetch):
        import pandas as pd
        frame = fetch(date=day)
        if not isinstance(frame, pd.DataFrame) or "代码" not in frame.columns:
            raise ValueError("limit pool unavailable or schema invalid")
        values = frame["代码"].tolist()
        if (any(not isinstance(code, str) or
                not re.fullmatch(r"[0-9]{6}", code) or code not in codes
                for code in values) or len(set(values)) != len(values)):
            raise ValueError("limit pool universe differs")
        return frame, set(values)

    up_pool, up_codes = pool(fetch_up)
    down_pool, down_codes = pool(fetch_down)
    if up_codes & down_codes:
        raise ValueError("conflicting limit pools")
    up = sum(row["pct_chg"] > 0 for row in daily.values())
    down = sum(row["pct_chg"] < 0 for row in daily.values())
    hot = (up_pool["所属行业"].value_counts().head(5).to_dict()
           if "所属行业" in up_pool.columns else {})
    return {
        "date": day, "advance": up, "decline": down,
        "flat": len(daily) - up - down,
        "up_down_ratio": round(up / max(down, 1), 2),
        "turnover_median": round(statistics.median(
            row["turnover_rate"] for row in basic.values()), 2),
        "total_amount_yi": round(sum(
            row["amount"] for row in daily.values()) / 100000, 0),
        "limit_up": len(up_codes), "limit_down": len(down_codes),
        "hot_sectors": hot, "sample_count": len(daily),
        "mode": "completed_session",
        "sample_scope": "Tushare daily当日有交易记录股票；非全部上市股票",
        "data_source": "Tushare daily/daily_basic；东方财富涨跌停池（AKShare）",
        "date_verification": "日线日期已校验；涨跌停池按请求日期获取，响应无独立日期列",
        "coverage_note": "两表代码集合及涨跌停池成员已校验；不证明上游全市场无遗漏"}