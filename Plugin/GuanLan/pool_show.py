# -*- coding: utf-8 -*-
"""GuanLan 34c: final pool viewer (satellite, read-only).
痛点 (#34c): funnel_daily回执只报diff统计(added/removed/计数), 查终池完整名单
需FileOperator直读json绕路. 本脚本一行命令解决: 读最新(或指定)final_pool_*.json,
输出全名单+meta. 零API调用, 零写入, 纯读 (settle_results.py卫星模式同款纪律).

未来若升为GuanLan action, 本体可直接复用 (batch_runner模式: dispatcher调卫星脚本).

Usage:
  python pool_show.py            # 最新终池
  python pool_show.py 20260928   # 指定日期
"""
import json, sys
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8', errors='replace')  # GBK console guard (r7惯例)
sys.stderr.reconfigure(encoding='utf-8', errors='replace')

BASE = Path(__file__).parent
DATA_DIR = BASE / "market_data"

def main():
    args = [a for a in sys.argv[1:] if not a.startswith('--')]
    from datetime import datetime, date
    def valid_date(value):
        try:
            return (isinstance(value, str) and len(value) == 8
                    and value.isascii() and value.isdigit()
                    and datetime.strptime(value, "%Y%m%d").strftime("%Y%m%d") == value)
        except ValueError:
            return False
    if len(args) > 1:
        raise ValueError("expected at most one date")
    if args:
        if not valid_date(args[0]):
            raise ValueError("invalid pool date")
        f = DATA_DIR / f"final_pool_{args[0]}.json"
        if not f.exists():
            sys.exit(f"final pool not found: {f.name}")
    else:
        files = sorted(
            path for path in DATA_DIR.glob("final_pool_*.json")
            if valid_date(path.stem.split("_")[-1])
            and path.stem.split("_")[-1] <= date.today().strftime("%Y%m%d"))
        if not files:
            sys.exit("no final_pool_*.json found in market_data/")
        f = files[-1]
    obj = json.loads(f.read_text(encoding='utf-8'))
    if not isinstance(obj, dict):
        raise ValueError("pool must be an object")
    meta, items = obj.get("_meta"), obj.get("items")
    expected_date = f.stem.split("_")[-1]
    if (not isinstance(meta, dict) or meta.get("trade_date") != expected_date
            or not isinstance(items, list)):
        raise ValueError("invalid pool metadata or items")
    seen = set()
    for item in items:
        if (not isinstance(item, dict) or not isinstance(item.get("code"), str)
                or not item["code"] or item["code"] in seen):
            raise ValueError("invalid or duplicate pool item")
        seen.add(item["code"])
    current_policy = meta.get("financial_policy") == "cashflow-v2"
    out = {"status": "ok", "file": f.name,
           "financial_policy": meta.get("financial_policy") or "legacy-invalidated",
           "usable_for_selection": current_policy,
           "requires_rebuild": not current_policy,
           "warning": (
               "读取成功不代表当日有效；请核对池日期和来源"
               if current_policy else
               "历史池使用旧财务公式或版本不明；仅供查档，不得用于当前选股，须按cashflow-v2重新生成"),
           "meta": {k: meta.get(k) for k in
                    ('trade_date', 'generated_at', 'funnel', 'fina_source',
                     'prev_pool_date', 'l1', 'l2', 'fina_pool', 'final',
                     'point_in_time_verified', 'historical_use_warning')},
           "count": len(items),
           "items": items}
    out["meta"]["point_in_time_verified"] = (
        meta.get("point_in_time_verified") is True)
    out["meta"]["historical_use_warning"] = (
        meta.get("historical_use_warning")
        or "历史财务版本未验证，不得作为无前视偏差回测证据")
    print(json.dumps(out, ensure_ascii=False))

if __name__ == '__main__':
    main()