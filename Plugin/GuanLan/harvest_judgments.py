# -*- coding: utf-8 -*-
"""GuanLan v4.3 judgment harvester (22a diary-import pipeline).
Scans 观澜's diary folder, extracts structured judgment blocks,
appends them to judgments.jsonl. Idempotent via watermark.

Design decisions (会审 2026-09-02):
- Template matching, NOT semantic understanding (方向J哲学: 概率问题变查表问题)
- Watermark: {filename: mtime_ns} persisted in harvest_state.json - performance cache ONLY, correctness lives in content-fingerprint dedup (fixed 2026-09-02/03)
- timestamp = diary write-time parsed from filename (VCP DailyNote naming), NOT harvest time (写时真值)
- Dedup key: (symbol, time_window_end, direction, probability) content fingerprint - position-independent: survives DailyNote update, organize rename, same-day rewrite (2026-09-03 spec batch)
- seq computed at harvest: Nth judgment of that (agent, day)
- Host: 观澜盘后日报 daily task calls GuanLan action harvest_judgments (翔 decision 2026-09-03, plugin-first); standalone run OK. (2026-09-03 note: docstring had said "AutoScheduler" - that component name never existed, see forum post "真教训绑着假名字"; real host always was VCPTaskAssistant, now the daily-report task)

Spec: judgment_spec_v1.md (观澜 v1.0, 2026-09-03) - 〔JUDGE〕 pipe blocks, 6 fields, STATE_MAP enum mapping

Usage: python harvest_judgments.py [--dry-run]
Design: 瑶序 2026-09-02 | Spec: 观澜 v1.0 (2026-09-03)
"""
import json, os, re, sys
from pathlib import Path
from filelock import FileLock

BASE = Path(__file__).parent
J_FILE = BASE / "judgments.jsonl"
STATE_FILE = BASE / "harvest_state.json"
DATA_LOCK = FileLock(str(BASE / "guanlan.lock"), timeout=60)  # L8: same lock file as main.py DATA_LOCK - harvest instances mutually exclude each other AND plugin-side writes; 60s loud timeout, never silent hang (Nova audit round 3)
# Configurable via config.env (v4.5, backward-compatible defaults)
AGENT = os.environ.get("GUANLAN_AGENT_NAME", "观澜")
MODEL_VERSION = os.environ.get("GUANLAN_MODEL_VERSION", "glm-5.3")
DIARY_DIR = Path(os.environ.get("GUANLAN_DIARY_DIR") or str(BASE.parent.parent / "dailynote" / AGENT))  # Plugin\GuanLan -> VCPToolBox root -> dailynote; override for non-VCP deployments

# ---- filled from 观澜 spec v1.0 (judgment_spec_v1.md, 2026-09-03) ----
BLOCK_PATTERN = re.compile(r"〔JUDGE〕\r?\n(.*?)〔/JUDGE〕", re.S)
STATE_MAP = {"盘后例行": "routine_after_close", "盘中紧急": "intraday_urgent",
             "勘误重写": "correction_rewrite", "深夜": "late_night"}
_FN_TS = re.compile(r"(\d{4}-\d{2}-\d{2})-(\d{2})_(\d{2})_(\d{2})")

def extract_fields(block_text, diary_name):
    """Parse one 〔JUDGE〕 block per spec v1.0. Return ledger row dict or None."""
    m = _FN_TS.search(diary_name)
    if not m:
        return None  # filename carries write-time truth; unparseable -> reject (conservative)
    row = {"timestamp": "%sT%s:%s:%s" % m.groups()}
    for line in block_text.splitlines():
        line = line.strip()
        if ":" in line:
            key, val = line.split(":", 1)
        elif "：" in line:
            key, val = line.split("：", 1)
        else:
            continue
        key, val = key.strip().lower(), val.strip()
        if not val:
            continue
        if key == "标的":
            if not re.fullmatch(r"\d{6}", val):
                return None
            row["symbol"] = val
        elif key == "方向":
            if val not in ("up", "down", "flat"):
                return None
            row["direction"] = val
        elif key == "概率":
            try:
                p = float(val)
            except ValueError:
                return None  # fuzzy words rejected at spec layer
            if not (0.0 <= p <= 1.0):
                return None
            row["probability"] = p
        elif key == "窗口":
            if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", val):
                return None
            row["time_window_end"] = val
        elif key == "止损" and val != "无":
            try:
                row["stop_loss"] = float(val)
            except ValueError:
                return None
        elif key == "state":
            if val not in STATE_MAP:
                return None
            row["state"] = STATE_MAP[val]
        elif key == "注":
            row["note"] = val
    if any(k not in row for k in ("symbol", "direction", "probability", "time_window_end", "state")):
        return None  # required-field check per spec section 4
    return row
# ----------------------------------------------------------------------------

def load_ledger_keys():
    """Existing (symbol, window, direction, probability, stop_loss) 5-tuple fingerprints for dedup."""
    keys = set()
    if J_FILE.exists():
        for line in J_FILE.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if not line:
                continue
            try:
                obj = json.loads(line)
            except json.JSONDecodeError:
                continue
            if "_meta" in obj or "_example" in obj:
                continue
            keys.add((obj.get("symbol"), obj.get("time_window_end"), obj.get("direction"), obj.get("probability"), obj.get("stop_loss")))  # 5-tuple fingerprint: stop_loss in key so stop-loss-only errata survive dedup (M3 fix, Nova audit round 2)
    return keys

def load_watermark():
    """Return {filename: mtime_ns}. Pure performance cache - correctness lives in dedup keys. M1 fix 2026-09-02 (Nova audit): was a name-set that silently skipped blocks appended via DailyNote update."""
    if STATE_FILE.exists():
        try:
            return json.loads(STATE_FILE.read_text(encoding="utf-8")).get("processed", {})
        except (json.JSONDecodeError, KeyError):
            pass
    return {}

def save_watermark(processed):
    STATE_FILE.write_text(json.dumps({"processed": processed}, ensure_ascii=False, indent=1), encoding="utf-8")

def next_seq(existing_lines, agent, day_str, new_rows):
    """Max seq among same (agent, day) in ledger + already-accepted new rows, +1 basis."""
    mx = 0
    for obj in existing_lines + new_rows:
        if obj.get("agent") == agent and str(obj.get("timestamp", ""))[:10] == day_str:
            try:
                mx = max(mx, int(obj.get("seq", 0)))
            except (TypeError, ValueError):
                pass
    return mx

def _main_locked():
    dry = "--dry-run" in sys.argv
    if BLOCK_PATTERN is None:
        print(json.dumps({"status": "blocked", "reason": "BLOCK_PATTERN pending 观澜 diary spec v1.0",
                          "ledger": str(J_FILE), "diary_dir": str(DIARY_DIR)}, ensure_ascii=False))
        return

    processed = load_watermark()
    dedup_keys = load_ledger_keys()
    ledger_lines = []
    if J_FILE.exists():
        for line in J_FILE.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if line:
                try:
                    obj = json.loads(line)
                    if "_meta" not in obj and "_example" not in obj:
                        ledger_lines.append(obj)
                except json.JSONDecodeError:
                    pass

    report = {"files_scanned": 0, "files_new": 0, "blocks_found": 0,
              "rows_appended": 0, "dup_skipped": 0, "malformed_skipped": 0}
    new_rows = []
    scanned_mtimes = {}  # harvest-time mtime per file (NOT commit-time): a file updated mid-harvest stays dirty for next run
    for diary in sorted(DIARY_DIR.glob("*.txt")):
        report["files_scanned"] += 1
        try:
            cur_mtime = diary.stat().st_mtime_ns
        except OSError:
            continue
        if processed.get(diary.name) == cur_mtime:
            continue  # perf skip only: file unchanged. Updated files get rescanned; dedup keys block re-harvest.
        report["files_new"] += 1
        scanned_mtimes[diary.name] = cur_mtime
        text = diary.read_text(encoding="utf-8", errors="replace")
        for m in BLOCK_PATTERN.finditer(text):
            report["blocks_found"] += 1
            fields = extract_fields(m.group(1), diary.name)
            if not fields:
                report["malformed_skipped"] += 1
                continue
            row = dict(fields)
            row["agent"] = AGENT
            row["source"] = "diary-import"
            row["evidence"] = diary.name
            row["model_version"] = MODEL_VERSION
            key = (row.get("symbol"), row.get("time_window_end"), row.get("direction"), row.get("probability"), row.get("stop_loss"))  # M3: stop_loss joins fingerprint - stop-loss-only errata must not be deduped away
            if key in dedup_keys:
                report["dup_skipped"] += 1
                continue
            day = str(row.get("timestamp", ""))[:10]
            row["seq"] = next_seq(ledger_lines, AGENT, day, new_rows) + 1
            dedup_keys.add(key)
            new_rows.append(row)

    if not dry:
        if new_rows:
            # 拼行防御 (2026-09-06判例): 追加前检查文件末字符, 非换行先补 -
            # 根因: v4.3重写WriteFile末尾无\n, 首收追加直接拼接产生{_example}{row1}死行
            _needs_nl = False
            if J_FILE.exists() and J_FILE.stat().st_size > 0:
                with J_FILE.open("rb") as _f:
                    _f.seek(J_FILE.stat().st_size - 1)
                    _needs_nl = _f.read(1) not in (b"\n", b"\r")
            with J_FILE.open("a", encoding="utf-8") as f:
                if _needs_nl:
                    f.write("\n")
                for row in new_rows:
                    f.write(json.dumps(row, ensure_ascii=False) + "\n")
        fresh = dict(processed)
        fresh.update(scanned_mtimes)  # L1 fix: watermark advances even when new_rows empty; mtime from harvest-time not commit-time
        save_watermark(fresh)
    report["rows_appended"] = len(new_rows)  # L6 fix 2026-09-02 (观澜 audit): counter declared but never wired; dry mode reads as "would append N"
    report["mode"] = "dry-run" if dry else "commit"
    print(json.dumps(report, ensure_ascii=False, indent=2))

def main():
    # L8: lock spans scan+dedup+commit - two concurrent harvest instances reading pre-write snapshots
    # would BOTH judge new rows as unseen and double-append. Whole-run lock, not write-only lock.
    with DATA_LOCK:
        _main_locked()

if __name__ == "__main__":
    main()