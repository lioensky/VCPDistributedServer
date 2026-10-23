# -*- coding: utf-8 -*-
"""GuanLan 22d: daily funnel routine (template step 2.7 backend).
串行: 当日快照 -> 当日K线 -> L1市值过滤 -> L2技术过滤(v1.1含R4) -> 终池交集 -> 与昨日diff.
fina 不在每日管道 (季度数据, checkpoint增量, 观澜spec 2026-09-06 17:14).

Fail-safe: 任一步失败 -> 整体fail, 日报按模板降级"沿用昨日终池" (失败保旧).
预算嵌套 (Nova r8 B披露): 外层包装110s是唯一真闸门; STEP_TIMEOUT=100只兜"单步挂死" -
四步串行最坏400s的数学上限实际被110s先掐, fail-safe方向正确; 孤儿孙进程幂等(文件存在即skip)无害.
每步幂等 (文件存在即skip), 重复调用零浪费.

Usage:
  python funnel_daily.py [YYYYMMDD]   # 默认今日
"""
import json, subprocess, sys, os
from pathlib import Path
from datetime import datetime, date
from ledger_io import atomic_write_json

sys.stdout.reconfigure(encoding='utf-8', errors='replace')
sys.stderr.reconfigure(encoding='utf-8', errors='replace')

BASE = Path(__file__).parent
DATA_DIR = BASE / "market_data"
STEP_TIMEOUT = 100  # 秒, 每步上限 (观澜spec总110s, 单步100留余量)

def run_step(name, *args):
    cmd = [sys.executable, str(BASE / name), *args]
    env = {**os.environ, "PYTHONIOENCODING": "utf-8"}
    try:
        p = subprocess.run(cmd, capture_output=True, text=True, encoding='utf-8',
                           timeout=STEP_TIMEOUT, cwd=str(BASE), env=env)
    except subprocess.TimeoutExpired:
        return {"step": name, "ok": False, "error": "timeout"}
    if p.returncode != 0:
        return {"step": name, "ok": False, "error": "subprocess failed",
                "exit_code": p.returncode}
    if name in ("market_snapshot.py", "kline_snapshot.py"):
        try:
            report = json.loads(p.stdout)
            if not isinstance(report, dict):
                raise ValueError("report must be an object")
            if name == "market_snapshot.py":
                dates = [str(a) for a in args if not str(a).startswith("--")]
                if not dates:
                    raise ValueError("requested date missing")
                for d in dates:
                    item = report.get("snapshot_" + d)
                    if not isinstance(item, dict) or item.get("status") not in ("ok", "skip"):
                        raise ValueError("snapshot not successful")
                delisted = report.get("delisted")
                if not isinstance(delisted, dict) or delisted.get("status") not in ("ok", "skip"):
                    raise ValueError("delisted refresh not successful")
            else:
                counts = [report.get(k) for k in ("ok", "skip", "fail")]
                if any(type(v) is not int or v < 0 for v in counts):
                    raise ValueError("invalid result counts")
                expected = len([a for a in args if not str(a).startswith("--")])
                if counts[2] != 0 or counts[0] + counts[1] != expected or expected == 0:
                    raise ValueError("incomplete or failed snapshots")
                if report.get("fails") != []:
                    raise ValueError("failure details present or missing")
        except (ValueError, TypeError):
            return {"step": name, "ok": False,
                    "error": "snapshot business report failed validation"}
    if name in ("market_filter.py", "tech_check.py"):
        try:
            report = json.loads(p.stdout)
            if (not isinstance(report, dict)
                    or report.get("status") != "ok" or report.get("error")):
                raise ValueError("stage business failure")
            count_key = "kept" if name == "market_filter.py" else "passed"
            count = report.get(count_key)
            if type(count) is not int or count < 0:
                raise ValueError("invalid stage count")
        except (ValueError, TypeError):
            return {"step": name, "ok": False,
                    "error": "filter business report failed validation"}
    return {"step": name, "ok": True}

def read_meta_count(pattern, key='kept'):
    """从最新匹配文件的_meta取数字."""
    files = sorted(DATA_DIR.glob(pattern))
    if not files:
        return None
    try:
        m = json.loads(files[-1].read_text(encoding='utf-8')).get('_meta', {})
        return m.get(key)
    except (json.JSONDecodeError, OSError):
        return None

def main():
    d = sys.argv[1] if len(sys.argv) > 1 else date.today().strftime("%Y%m%d")
    if (len(d) != 8 or not d.isascii() or not d.isdigit()
            or datetime.strptime(d, "%Y%m%d").strftime("%Y%m%d") != d):
        raise ValueError("invalid target trade date")
    for name, arguments in (
            ("market_snapshot.py", (d,)),
            ("kline_snapshot.py", (d,)),
            ("market_filter.py", (d, "--min-mv", "80")),
            ("tech_check.py", (d,))):
        step = run_step(name, *arguments)
        if not step["ok"]:
            print(json.dumps({
                "status": "fail", "trade_date": d, "failed_steps": [step],
                "note": "前置失败，后续未执行；最终候选池未更新"
            }, ensure_ascii=False))
            sys.exit(1)
    # A successful subprocess receipt cannot replace a valid stage artifact.
    tech_f = DATA_DIR / f"tech_passed_{d}.json"
    if not tech_f.is_file():
        raise ValueError("technical pool missing; final pool unchanged")
    technical = json.loads(tech_f.read_text(encoding="utf-8"))
    if not isinstance(technical, dict):
        raise ValueError("invalid technical pool")
    tech_meta, tech_items = technical.get("_meta"), technical.get("items")
    if (not isinstance(tech_meta, dict) or not isinstance(tech_items, list)
            or tech_meta.get("trade_date") != d
            or not isinstance(tech_meta.get("stats"), dict)):
        raise ValueError("technical pool date or structure invalid")
    l2 = tech_meta["stats"].get("pass")
    if type(l2) is not int or l2 < 0 or l2 != len(tech_items):
        raise ValueError("technical pool count mismatch")
    tech_codes = set()
    for row in tech_items:
        if (not isinstance(row, dict)
                or not isinstance(row.get("ts_code"), str)
                or not row["ts_code"] or row["ts_code"] in tech_codes):
            raise ValueError("invalid or duplicate technical pool code")
        tech_codes.add(row["ts_code"])
    # final pool: validated technical items intersect nonfuture financial pool.
    fina_codes = set()
    policy_dir = DATA_DIR / "fina_cashflow_v2"
    fina_files = sorted(
        (f for f in policy_dir.glob("fina_passed_*.jsonl")
         if len(f.stem.split("_")[-1]) == 8
         and f.stem.split("_")[-1].isascii()
         and f.stem.split("_")[-1].isdigit()
         and f.stem.split("_")[-1] <= d),
        key=lambda f: (f.stem.split("_")[-1], f.parent == policy_dir))
    if not fina_files:
        raise ValueError(
            "no cashflow-v2 financial pool; old-formula pools refused, final pool unchanged")
    fina_path = fina_files[-1]
    fina_src = fina_path.relative_to(DATA_DIR).as_posix()
    announcement_filtered = fina_path.parent == policy_dir
    financial_date = fina_path.stem.split("_")[-1]
    for line in fina_path.read_text(encoding='utf-8').splitlines():
        if line.strip():
            row = json.loads(line)
            if (not isinstance(row, dict)
                    or not isinstance(row.get("ts_code"), str)
                    or not row["ts_code"]
                    or row.get("verdict") != "pass"):
                raise ValueError("invalid financial pool row")
            if row["ts_code"] in fina_codes:
                raise ValueError("duplicate financial pool code")
            if (
                    row.get("financial_policy") != "cashflow-v2"
                    or row.get("evaluation_as_of") != financial_date
                    or row.get("announcement_policy")
                       != "ann_date strictly before target date"):
                raise ValueError("financial announcement policy mismatch")
            fina_codes.add(row["ts_code"])
    final = sorted(tech_codes & fina_codes)
    # diff vs previous final_pool (any earlier date)
    prev_files = sorted(DATA_DIR.glob("final_pool_*.json"))
    prev_codes = set()
    prev_date = None
    candidates = [
        f for f in prev_files
        if len(f.stem.split("_")[-1]) == 8
        and f.stem.split("_")[-1].isascii()
        and f.stem.split("_")[-1].isdigit()
        and f.stem.split("_")[-1] < d]
    if candidates:
        prev_date = candidates[-1].stem.split("_")[-1]
        try:
            prev_codes = {r['code'] for r in json.loads(candidates[-1].read_text(encoding='utf-8')).get('items', [])}
        except (json.JSONDecodeError, KeyError, TypeError) as exc:
            raise ValueError("previous pool invalid; diff unavailable") from exc
    diff = {"added": sorted(set(final) - prev_codes), "removed": sorted(prev_codes - set(final))}
    # persist today's final pool
    ind = {}
    ind_f = DATA_DIR / "industry_map.json"
    if ind_f.exists():
        ind = json.loads(ind_f.read_text(encoding='utf-8'))
    out = {"_meta": {"generated_at": datetime.now().isoformat(timespec='seconds'),
                      "trade_date": d, "funnel": "daily routine v1.1 (R4 signed)",
                      "fina_source": fina_src, "prev_pool_date": prev_date,
                      "financial_announcement_filtered": announcement_filtered,
                      "financial_policy": "cashflow-v2",
                      "historical_reconstruction_allowed": False,
                      "point_in_time_verified": False,
                      "historical_use_warning": "文件日期非财务披露可得性证明；禁止作为无前视偏差回测证据",
                      "l1": read_meta_count(f"screened_{d}_circ80.json", 'kept'),
                      "l2": l2, "fina_pool": len(fina_codes), "final": len(final)},
           "items": [{"code": c, "name": ind.get(c, {}).get('name', ''),
                       "industry": ind.get(c, {}).get('industry', '')} for c in final]}
    atomic_write_json(DATA_DIR / f"final_pool_{d}.json", out)
    print(json.dumps({"status": "ok", "trade_date": d,
                       "l1": out['_meta']['l1'], "l2": l2, "final": len(final),
                       "fina_source": fina_src, "prev_pool": prev_date,
                       "diff": {"added": diff['added'][:20], "removed": diff['removed'][:20],
                                 "added_n": len(diff['added']), "removed_n": len(diff['removed'])}},
                      ensure_ascii=False))

if __name__ == '__main__':
    main()