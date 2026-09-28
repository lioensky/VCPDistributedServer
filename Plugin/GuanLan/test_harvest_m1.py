# -*- coding: utf-8 -*-
"""M1 fix acceptance test for harvest_judgments.py (观澜, 2026-09-02).
Black-box: monkeypatches module globals (BLOCK_PATTERN/extract_fields/DIARY_DIR/
J_FILE/STATE_FILE) into an isolated sandbox. Production file untouched.
Run: python test_harvest_m1.py
Cases: T1 first harvest / T2 update-append rescans (M1 core) / T3 idle rerun /
       T5 empty-blocks file advances watermark (L1) / T4 watermark loss -> dedup safety.
Block format = 观澜 diary spec v1.0 draft (also the living example for 瑶序's TODO).
"""
import json, re, shutil, sys, time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
import harvest_judgments as hj

BASE = Path(__file__).parent
TMP_DIARY = BASE / "_test_diary"
TMP_J = BASE / "_test_judgments.jsonl"
TMP_STATE = BASE / "_test_state.json"

TEST_PATTERN = re.compile(r"〔JUDGE〕(.*?)〔/JUDGE〕", re.S)
TEST_STATE_MAP = {"盘后": "routine_after_close", "盘中": "intraday_urgent",
                  "勘误": "correction_rewrite", "深夜": "late_night"}

def test_extract(block_text, diary_date):
    """Spec v1.0 draft extractor: pipe-separated k:v inside 〔JUDGE〕 wrapper."""
    fields = {}
    for pair in block_text.strip().split("|"):
        k, _, v = pair.partition(":")
        fields[k.strip()] = v.strip()
    try:
        return {
            "symbol": fields["symbol"],
            "direction": fields["dir"],
            "probability": float(fields["p"]),
            "time_window_end": fields["win"],
            "stop_loss": float(fields["sl"]) if fields.get("sl") else None,
            "timestamp": fields["ts"],
            "state": TEST_STATE_MAP.get(fields.get("state", ""), "routine_after_close"),
        }
    except (KeyError, ValueError):
        return None

def reset_env():
    if TMP_DIARY.exists():
        shutil.rmtree(TMP_DIARY)
    TMP_DIARY.mkdir()
    for f in (TMP_J, TMP_STATE):
        if f.exists():
            f.unlink()
    hj.J_FILE = TMP_J
    hj.STATE_FILE = TMP_STATE
    hj.DIARY_DIR = TMP_DIARY
    hj.BLOCK_PATTERN = TEST_PATTERN
    hj.extract_fields = test_extract
    hj.STATE_MAP = TEST_STATE_MAP

def rows():
    if not TMP_J.exists():
        return []
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

def harvest(dry=False):
    sys.argv = ["harvest_judgments.py"] + (["--dry-run"] if dry else [])
    hj.main()

def wm():
    return json.loads(TMP_STATE.read_text(encoding="utf-8"))["processed"] if TMP_STATE.exists() else {}

RESULTS = []
def check(name, cond, detail=""):
    RESULTS.append((name, bool(cond)))
    print(f"[{'PASS' if cond else 'FAIL'}] {name}" + (f" | {detail}" if detail else ""))

# ---- T1: first harvest ----
reset_env()
(TMP_DIARY / "2026-09-01-20_00_00.txt").write_text(
    "[20:00] 周判断\n〔JUDGE〕symbol:601899|dir:up|p:0.65|win:2026-09-08|sl:30.0|ts:2026-09-01T20:00:00|state:盘后〔/JUDGE〕\n"
    "[20:05] 补一条ETF判断\n〔JUDGE〕symbol:588000|dir:down|p:0.55|win:2026-09-08|sl:|ts:2026-09-01T20:05:00|state:盘后〔/JUDGE〕\n",
    encoding="utf-8")
harvest()
r = rows()
check("T1 first harvest appends 2 rows", len(r) == 2, f"rows={len(r)}")
check("T1 seq 1,2 assigned", [x.get("seq") for x in r] == [1, 2])
check("T1 agent/source/evidence stamped", all(x["agent"] == "观澜" and x["source"] == "diary-import" and x["evidence"].endswith(".txt") for x in r))
check("T1 probability parsed as float", r[0]["probability"] == 0.65)
check("T1 state mapped to enum", r[0]["state"] == "routine_after_close")

# ---- T2: M1 core - update-append same file ----
time.sleep(0.02)
with (TMP_DIARY / "2026-09-01-20_00_00.txt").open("a", encoding="utf-8") as f:
    f.write("[21:30] 盘后update追加的勘误判断\n〔JUDGE〕symbol:601899|dir:up|p:0.70|win:2026-09-08|sl:30.5|ts:2026-09-01T21:30:00|state:勘误〔/JUDGE〕\n")
harvest()
r = rows()
check("T2 M1: appended block harvested (total 3, not stuck at 2)", len(r) == 3, f"rows={len(r)}")
new = [x for x in r if x["timestamp"] == "2026-09-01T21:30:00"]
check("T2 new block present exactly once", len(new) == 1)
check("T2 old blocks NOT duplicated", sum(1 for x in r if x["timestamp"] == "2026-09-01T20:00:00") == 1)
check("T2 seq continues within day (3)", new and new[0]["seq"] == 3, f"seq={new[0].get('seq') if new else 'NA'}")
check("T2 state 勘误 mapped", new and new[0]["state"] == "correction_rewrite")

# ---- T3: idle rerun ----
harvest()
check("T3 idle rerun adds nothing", len(rows()) == 3)

# ---- T5: L1 - empty-blocks file advances watermark ----
(TMP_DIARY / "2026-09-02-09_00_00.txt").write_text("[09:00] 普通日记，无判断块\n", encoding="utf-8")
harvest()
check("T5 no rows from blockless file", len(rows()) == 3)
check("T5 watermark advanced for blockless file (L1)", "2026-09-02-09_00_00.txt" in wm())

# ---- T4: crash simulation - watermark lost, dedup must hold ----
TMP_STATE.unlink()
harvest()
check("T4 watermark loss causes zero duplication", len(rows()) == 3, f"rows={len(rows())}")

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
print("ALL GREEN - M1 fix semantics verified: update-append rescanned, dedup blocks old blocks, watermark is perf-only.")
sys.exit(0)