# -*- coding: utf-8 -*-
"""M15 batch_screen async runner (2026-09-21). argv[1] = JSON {symbols, with_flow, with_exemption, out_path}.
Runs gm.batch_screen (single source of truth, zero logic fork) and writes result JSON to out_path."""
import sys, os, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import main as gm
from pathlib import Path
import re
from ledger_io import atomic_write_json

req = json.loads(sys.argv[1])
if not isinstance(req, dict):
    raise ValueError("batch request must be an object")
root = Path(__file__).resolve().parent / "market_data"
target = Path(req["out_path"])
if (target.parent.resolve() != root.resolve()
        or not re.fullmatch(r"batch_result_[0-9a-f]{10}\.json", target.name)
        or target.is_symlink()):
    raise ValueError("invalid batch result destination")
r = gm.batch_screen(
    req["symbols"], with_flow=req.get("with_flow", True),
    with_exemption=req.get("with_exemption", False))
if not isinstance(r, dict):
    raise ValueError("batch result must be an object")
r["source"] = "runner"
atomic_write_json(target, r)
print("[batch_runner] result persisted")
