# -*- coding: utf-8 -*-
"""GuanLan menu_sync: 派发器action清单 vs manifest invocationCommands 的diff守卫.
病根 (7/19诊断, 9/6实证): manifest冻结v4.0两月三版本 - "记得更新"治不了惯性病.
治法: 机器检查的不变量替代靠记忆的美德 (失败是响的, 文档层应用).

Check:
  1. 派发器物理action全集 (main.py的 elif action == "X" 模式)
  2. manifest已登记集 (capabilities.invocationCommands[].commandIdentifier)
  -> 输出: 已登记/未登记/幽灵登记(菜单有派发器无) 三张表
Exit: 未登记非空 -> exit 1 (可挂daily_reconcile或发布前手跑; 当前36老action未登记为已知态, exit规则用--strict控制)

Usage:
  python menu_sync.py            # 报告模式(默认, 老action缺失不exit 1)
  python menu_sync.py --strict   # 严格模式(任何缺失exit 1, 全量登记完成后启用)
"""
import json, re, sys
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8', errors='replace')
sys.stderr.reconfigure(encoding='utf-8', errors='replace')

BASE = Path(__file__).parent
DISPATCHER = BASE / "main.py"
MANIFEST = BASE / "plugin-manifest.json"

# 登记政策 (翔裁 2026-09-14 00:42): manifest菜单定位为"生态共享命令"——
# 只登记跨Agent有意义的命令(收割/漏斗/批量三问/风控查询等7条即此性质);
# 36条老action为GuanLan内部命令, 明确豁免不登记(私人插件无第三方消费者, 补登无收益)。
# --strict启用条件改为"新增生态级命令未登记", 老命令存量36为设计常态非欠账。
KNOWN_UNREGISTERED_OK = True  # 报告模式默认豁免老action的exit码

def dispatcher_actions():
    src = DISPATCHER.read_text(encoding='utf-8')
    # Nova r14修正 (2026-09-20): 派发器首分支是 if 不是 elif (L4034 realtime_quote) —
    # 原正则从首跑起少数1, "44"读数九天, 45才是真值
    return sorted(set(re.findall(r'(?:elif|if) action == "(\w+)"', src)))

def manifest_actions():
    try:
        d = json.loads(MANIFEST.read_text(encoding='utf-8'))
        return sorted(c.get('commandIdentifier', '') for c in
                      d.get('capabilities', {}).get('invocationCommands', []))
    except (json.JSONDecodeError, KeyError, OSError):
        return []

def main():
    strict = '--strict' in sys.argv
    disp, mani = dispatcher_actions(), manifest_actions()
    unreg = [a for a in disp if a not in mani]
    ghost = [m for m in mani if m not in disp]
    reg = [a for a in disp if a in mani]
    print(json.dumps({
        "dispatcher_total": len(disp),
        "registered": len(reg), "registered_list": reg,
        "unregistered": len(unreg), "unregistered_list": unreg,
        "ghost_registrations": ghost,
        "mode": "strict" if strict else "report",
    }, ensure_ascii=False, indent=1))
    if ghost:
        print("GHOST: manifest登记了派发器不存在的action - 检查是否删了功能忘清菜单", file=sys.stderr)
        sys.exit(1)
    if strict and unreg:
        print(f"STRICT FAIL: {len(unreg)} dispatcher actions unregistered", file=sys.stderr)
        sys.exit(1)

if __name__ == '__main__':
    main()