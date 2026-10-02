# -*- coding: utf-8 -*-
"""GuanLan v4.2 calibration monthly join.
judgments.jsonl + results.jsonl -> Brier Score + reliability curve.
Usage: python calibration_monthly.py [YYYY-MM]   (no arg = all months)
Ledgers are append-only; join key = (symbol, time_window_end/window_end).
Correction semantics: if multiple judgment lines share a key, the one with
  the latest timestamp wins (corrects-pointer compensation, never deletion).
Outcome semantics: outcome=1 iff actual_direction == judgment.direction.
Brier = (probability - outcome)^2, averaged over matched pairs.
Scoring convention (23c, 2026-09-06 瑶序裁定 - Nova复核通过 2026-09-07 四层全绿): one-vs-rest per direction -
每条判断按"该方向 vs 非该方向"二元计分 (flat判断 = flat vs 非flat), 与judgments
"方向+单概率"的记录形态匹配; 三分类全概率公式需完整分布{p_up,p_down,p_flat},
替判断者假设剩余概率分配=编造信念. 月报纪律: Brier只做纵比(自身历史), 不可横比
不同标的(Base Rate与不可约误差差异 - 2026-09-06调研入档).
First-month rule: matched < 30 -> Brier only, curve suppressed.
diary-import lines without evidence field are EXCLUDED (flagged in report).
W-refeed to kelly is OUT OF SCOPE here (GuanLan command layer decides windowing).
Design: Nova #3 (schema) | Compensation clause: 观澜勘误帖 2026-08-21 | Pipe: 瑶序
"""
import json, sys
from pathlib import Path

BASE = Path(__file__).parent
J_FILE = BASE / "judgments.jsonl"
R_FILE = BASE / "results.jsonl"

def load(path):
    rows, bad = [], 0
    if not path.exists():
        return rows, bad
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line:
            continue
        try:
            obj = json.loads(line)
        except json.JSONDecodeError:
            bad += 1
            continue
        if "_meta" in obj or "_example" in obj:
            continue
        rows.append(obj)
    return rows, bad

def latest_by_key(rows, key_fields, ts_field="timestamp"):
    """Keep the latest-timestamp line per key (compensation semantics)."""
    out = {}
    for r in rows:
        key = tuple(str(r.get(f, "")) for f in key_fields)
        if key not in out or str(r.get(ts_field, "")) >= str(out[key].get(ts_field, "")):
            out[key] = r
    return out

def month_filter(rows, ym, key="timestamp"):
    return [r for r in rows if str(r.get(key, ""))[:7] == ym] if ym else rows

def main():
    ym = sys.argv[1] if len(sys.argv) > 1 else None
    judgments, j_bad = load(J_FILE)
    results, r_bad = load(R_FILE)

    excluded_no_evidence = [
        j for j in judgments
        if j.get("source") == "diary-import" and not j.get("evidence")
    ]
    usable = [j for j in judgments if j not in excluded_no_evidence]
    usable = month_filter(usable, ym)

    j_idx = latest_by_key(usable, ["symbol", "time_window_end"])
    r_idx = latest_by_key(results, ["symbol", "window_end"])

    briers, buckets = [], {i: [0.0, 0, 0] for i in range(5)}
    stop_settlements = []  # Nova r14分账 (2026-09-20): 止损结算行测的是路径结果非预测质量,
    # 混入Brier会把"预测对但路径死"记成满分miss (up 0.65止损后窗口末大涨案例) — 分账处理
    for key, j in j_idx.items():
        r = r_idx.get(key)
        if r is None:
            continue
        _jm = r.get("judge_meta") or {}
        if "stop_scan" in str(_jm.get("source", "")):
            stop_settlements.append({
                "symbol": j.get("symbol"), "direction": j.get("direction"),
                "probability": j.get("probability"),
                "settled_as": r.get("actual_direction"),
                "note": "止损路径结算, 不进预测Brier (路径结果与预测质量分账)"})
            continue
        outcome = 1 if r.get("actual_direction") == j.get("direction") else 0
        try:
            p = float(j.get("probability", 0.5))
        except (TypeError, ValueError):
            continue
        briers.append((p - outcome) ** 2)
        b = min(int(p * 5), 4)
        buckets[b][0] += p; buckets[b][1] += 1; buckets[b][2] += outcome

    matched = len(briers)
    report = {"month": ym or "all", "judgments_total": len(judgments),
              "judgments_usable": len(usable),
              "excluded_no_evidence": len(excluded_no_evidence),
              "matched": matched,
              "parse_errors": {"judgments": j_bad, "results": r_bad},
              # 23c scoring convention (裁定 2026-09-06 瑶序; Nova复核通过 2026-09-07 四层全绿):
              # one-vs-rest per direction; Brier纵比only不可横比 - 见docstring
              "scoring_convention": "one-vs-rest per direction (23c, approved 2026-09-07)",
              # Nova 23c复核发现⑤: base rate层积披露 — flat判断的base rate天然高于up/down
              # (A股周窗横盘为常态), 跨方向Brier不可比; 跨方向比较须按方向分组做可靠性曲线
              "base_rate_note": "flat的base rate高于up/down(横盘常态): 跨方向分数不可比, 仅纵比",
              "stop_settlements_separated": len(stop_settlements),
              "stop_settlements_detail": stop_settlements[:10]}  # r14分账: 止损路径结算单独成列, 不进Brier
    if matched:
        report["brier"] = round(sum(briers) / matched, 4)
        if matched >= 30:
            report["reliability_curve"] = [
                {"bucket": f"{i*20}-{(i+1)*20}%",
                 "avg_pred": round(v[0]/v[1], 3) if v[1] else None,
                 "actual_hit_rate": round(v[2]/v[1], 3) if v[1] else None,
                 "n": v[1]}
                for i, v in sorted(buckets.items()) if v[1]]
        else:
            report["note"] = f"matched={matched} < 30: reliability curve suppressed (first-month rule)"
    else:
        report["note"] = "no matched judgment-result pairs yet"
    print(json.dumps(report, ensure_ascii=False, indent=2))

if __name__ == "__main__":
    main()