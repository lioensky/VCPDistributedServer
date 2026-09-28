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
        return {"step": name, "ok": False, "error": (p.stderr or p.stdout or "")[-200:]}
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
    steps = [
        run_step("market_snapshot.py", d),
        run_step("kline_snapshot.py", d),
        run_step("market_filter.py", d, "--min-mv", "80"),
        run_step("tech_check.py", d),
    ]
    failed = [s for s in steps if not s['ok']]
    if failed:
        print(json.dumps({"status": "fail", "trade_date": d, "failed_steps": failed,
                          "note": "失败保旧: 沿用昨日终池, 次日自动补 (fail-safe)"}, ensure_ascii=False))
        sys.exit(1)
    # L2 pass count from tech output stats
    tech_meta = {}
    tech_f = DATA_DIR / f"tech_passed_{d}.json"
    if tech_f.exists():
        tech_meta = json.loads(tech_f.read_text(encoding='utf-8')).get('_meta', {})
    l2 = tech_meta.get('stats', {}).get('pass')
    # final pool: tech items ∩ latest fina_passed
    tech_codes = {r['ts_code'] for r in (json.loads(tech_f.read_text(encoding='utf-8')).get('items', [])
                  if tech_f.exists() else [])}
    fina_codes = set()
    fina_files = sorted(DATA_DIR.glob("fina_passed_*.jsonl"))
    fina_src = fina_files[-1].name if fina_files else None
    if fina_src:
        for line in (DATA_DIR / fina_src).read_text(encoding='utf-8').splitlines():
            if line.strip():
                try:
                    fina_codes.add(json.loads(line)['ts_code'])
                except json.JSONDecodeError:
                    pass
    final = sorted(tech_codes & fina_codes)
    # diff vs previous final_pool (any earlier date)
    prev_files = sorted(DATA_DIR.glob("final_pool_*.json"))
    prev_codes = set()
    prev_date = None
    candidates = [f for f in prev_files if f.name != f"final_pool_{d}.json"]
    if candidates:
        prev_date = candidates[-1].stem.split("_")[-1]
        try:
            prev_codes = {r['code'] for r in json.loads(candidates[-1].read_text(encoding='utf-8')).get('items', [])}
        except (json.JSONDecodeError, KeyError):
            prev_codes = set()
    diff = {"added": sorted(set(final) - prev_codes), "removed": sorted(prev_codes - set(final))}
    # persist today's final pool
    ind = {}
    ind_f = DATA_DIR / "industry_map.json"
    if ind_f.exists():
        ind = json.loads(ind_f.read_text(encoding='utf-8'))
    out = {"_meta": {"generated_at": datetime.now().isoformat(timespec='seconds'),
                      "trade_date": d, "funnel": "daily routine v1.1 (R4 signed)",
                      "fina_source": fina_src, "prev_pool_date": prev_date,
                      "l1": read_meta_count(f"screened_{d}_circ80.json", 'kept'),
                      "l2": l2, "fina_pool": len(fina_codes), "final": len(final)},
           "items": [{"code": c, "name": ind.get(c, {}).get('name', ''),
                       "industry": ind.get(c, {}).get('industry', '')} for c in final]}
    (DATA_DIR / f"final_pool_{d}.json").write_text(json.dumps(out, ensure_ascii=False), encoding='utf-8')
    print(json.dumps({"status": "ok", "trade_date": d,
                       "l1": out['_meta']['l1'], "l2": l2, "final": len(final),
                       "fina_source": fina_src, "prev_pool": prev_date,
                       "diff": {"added": diff['added'][:20], "removed": diff['removed'][:20],
                                 "added_n": len(diff['added']), "removed_n": len(diff['removed'])}},
                      ensure_ascii=False))

if __name__ == '__main__':
    main()