# -*- coding: utf-8 -*-
"""Spec v1.0 real-path tests for harvest_judgments.py (瑶序, 2026-09-03).
Complements test_harvest_m1.py (mock-path skeleton tests by 观澜 9/2).
That file monkeypatches extract_fields away; THIS file exercises the REAL
BLOCK_PATTERN + extract_fields + STATE_MAP filled from judgment_spec_v1.md.
Sandbox isolation only for DIARY_DIR/J_FILE/STATE_FILE - parsing layer untouched.
Run: python test_harvest_spec.py   (after Nova M2 audit: real path had zero coverage)

R1 real-path first flight : spec-format multi-line block parses, all 8 fields land,
                             timestamp FROM FILENAME (not block, not harvest time)
R2 fuzzy probability      : "偏高" rejected at spec layer (extract_fields -> None)
R3 legacy single-line form: old test-format block invisible to real BLOCK_PATTERN
                             (regex requires newline after 〔JUDGE〕) -> findall empty
R4 short state enum       : "盘后" (mock-era enum) rejected by real STATE_MAP
R5 M3 verdict             : same 4-tuple, different stop_loss -> BOTH rows survive
                             dedup (5-tuple fingerprint); exact duplicate still blocked
"""
import shutil, sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
import harvest_judgments as hj

BASE = Path(__file__).parent
TMP_DIARY = BASE / "_test_diary_r"
TMP_J = BASE / "_test_judgments_r.jsonl"
TMP_STATE = BASE / "_test_state_r.json"

RESULTS = []
def check(name, cond, detail=""):
    RESULTS.append((name, bool(cond)))
    print(f"[{'PASS' if cond else 'FAIL'}] {name}" + (f" | {detail}" if detail else ""))

def reset_env():
    """Sandbox paths ONLY. Real BLOCK_PATTERN/extract_fields/STATE_MAP stay live."""
    if TMP_DIARY.exists():
        shutil.rmtree(TMP_DIARY)
    TMP_DIARY.mkdir()
    for f in (TMP_J, TMP_STATE):
        if f.exists():
            f.unlink()
    hj.J_FILE = TMP_J
    hj.STATE_FILE = TMP_STATE
    hj.DIARY_DIR = TMP_DIARY

def harvest():
    sys.argv = ["harvest_judgments.py"]
    hj.main()

def rows():
    if not TMP_J.exists():
        return []
    import json
    out = []
    for line in TMP_J.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line:
            continue
        try:
            obj = json.loads(line)
        except json.JSONDecodeError:
            continue
        if "_meta" in obj or "_example" in obj:
            continue
        out.append(obj)
    return out

SPEC_BLOCK = ("[20:00] 盘后判断\n〔JUDGE〕\n标的: 601899\n方向: up\n概率: 0.65\n"
              "窗口: 2026-09-10\n止损: 30.00\nstate: 盘后例行\n注: 首块\n〔/JUDGE〕\n")

# ---- R1: real-path first flight ----
reset_env()
(TMP_DIARY / "2026-09-03-20_00_00.txt").write_text(SPEC_BLOCK, encoding="utf-8")
harvest()
r = rows()
check("R1 spec block harvested (1 row)", len(r) == 1, f"rows={len(r)}")
if r:
    b = r[0]
    check("R1 symbol 6-digit", b.get("symbol") == "601899")
    check("R1 direction up", b.get("direction") == "up")
    check("R1 probability float 0.65", b.get("probability") == 0.65)
    check("R1 window parsed", b.get("time_window_end") == "2026-09-10")
    check("R1 stop_loss float", b.get("stop_loss") == 30.0)
    check("R1 state enum mapped", b.get("state") == "routine_after_close")
    check("R1 timestamp FROM FILENAME", b.get("timestamp") == "2026-09-03T20:00:00",
          f"ts={b.get('timestamp')}")
    check("R1 seq first of day", b.get("seq") == 1)
    check("R1 note carried", b.get("note") == "首块")
else:
    for n in ("R1 symbol", "R1 direction", "R1 probability", "R1 window",
              "R1 stop_loss", "R1 state enum", "R1 timestamp", "R1 seq", "R1 note"):
        check(n + " (skipped: no row)", False)

# ---- R2/R3/R4: rejection paths, asserted at unit level ----
fuzzy_block = "标的: 601899\n方向: up\n概率: 偏高\n窗口: 2026-09-10\n止损: 30.00\nstate: 盘后例行\n"
check("R2 fuzzy probability rejected (None)", hj.extract_fields(fuzzy_block, "2026-09-03-20_00_00.txt") is None)

legacy_line = "〔JUDGE〕symbol:601899|dir:up|p:0.65|win:2026-09-10|sl:30.0|ts:2026-09-03T20:00:00|state:盘后〔/JUDGE〕"
check("R3 legacy single-line form invisible to real BLOCK_PATTERN",
      len(hj.BLOCK_PATTERN.findall(legacy_line)) == 0)

short_state_block = "标的: 601899\n方向: up\n概率: 0.65\n窗口: 2026-09-10\n止损: 30.00\nstate: 盘后\n"
check("R4 short enum 盘后 rejected by real STATE_MAP (None)",
      hj.extract_fields(short_state_block, "2026-09-03-20_00_00.txt") is None)
check("R4b bad filename rejected (no VCP timestamp)",
      hj.extract_fields("标的: 601899\n方向: up\n概率: 0.65\n窗口: 2026-09-10\nstate: 盘后例行\n", "random.txt") is None)

# ---- R5: M3 verdict - stop-loss errata survive dedup ----
errata = ("[21:00] 止损勘误\n〔JUDGE〕\n标的: 601899\n方向: up\n概率: 0.65\n"
          "窗口: 2026-09-10\n止损: 29.80\nstate: 勘误重写\n注: 止损下移\n〔/JUDGE〕\n")
(TMP_DIARY / "2026-09-03-21_00_00.txt").write_text(errata, encoding="utf-8")
harvest()
r = rows()
check("R5 M3: stop-loss errata row SURVIVES dedup (2 rows, not 1)", len(r) == 2, f"rows={len(r)}")
sl = sorted([x.get("stop_loss") for x in r if x.get("stop_loss") is not None])
check("R5 both stop_loss values in ledger", sl == [29.8, 30.0], f"sl={sl}")
err = [x for x in r if x.get("state") == "correction_rewrite"]
check("R5 errata state mapped", len(err) == 1 and err[0].get("seq") == 2)

# exact duplicate (same 5-tuple, new file) must still be blocked
(TMP_DIARY / "2026-09-03-22_00_00.txt").write_text(SPEC_BLOCK, encoding="utf-8")
harvest()
check("R5b exact duplicate still deduped (rows stay 2)", len(rows()) == 2, f"rows={len(rows())}")

# ---- cleanup ----
shutil.rmtree(TMP_DIARY, ignore_errors=True)
for f in (TMP_J, TMP_STATE):
    if f.exists():
        f.unlink()

fails = [n for n, ok in RESULTS if not ok]
print(f"\n===== {len(RESULTS) - len(fails)}/{len(RESULTS)} PASS =====")
if fails:
    print("FAILED: " + ", ".join(fails))
    sys.exit(1)
print("ALL GREEN - real path verified: spec blocks parse, fuzzy/legacy/short-enum rejected, M3 stop-loss errata survive.")
sys.exit(0)