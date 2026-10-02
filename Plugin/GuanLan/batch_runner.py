# -*- coding: utf-8 -*-
"""M15 batch_screen async runner (2026-09-21). argv[1] = JSON {symbols, with_flow, with_exemption, out_path}.
Runs gm.batch_screen (single source of truth, zero logic fork) and writes result JSON to out_path."""
import sys, os, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import main as gm
req = json.loads(sys.argv[1])
r = gm.batch_screen(req["symbols"], with_flow=req.get("with_flow", True), with_exemption=req.get("with_exemption", False))
r["source"] = "runner"
with open(req["out_path"], "w", encoding="utf-8") as f:
    json.dump(r, f, ensure_ascii=False, default=str)
print("[batch_runner] written:", req["out_path"])
