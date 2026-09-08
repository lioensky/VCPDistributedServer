#!/usr/bin/env python3
"""
GMR 推理 sidecar。

【架构定位】本进程是快回路的服务端，监听 127.0.0.1:6091。

    快回路(~100ms):  Blender GMR Add-on  ->  本进程     [不经过 VCP]
    管理回路(秒级):  VCP -> BlenderBridge -> gmr ex -> 本进程

拖拽推理必须由 Blender Add-on 直连本进程。绝不能走 blender-mcp——
上游单并发(BLENDER_BUSY) + 双跳延迟，交互推理塞进去必然请求堆积锁死。

【为什么用标准库 http.server】
零依赖即可启动。S0 阶段没装 PyTorch 也能跑通全链路：无模型时 /infer 走
三次贝塞尔插值兜底，正好对应论文"用传统插值顶替 ML-Betweener"的第一步。

【接口契约（改动需同步 sidecar.js）】
  GET  /health      -> {status, loaded, device, torch_available, backend, ...}
  POST /load_model  <- {model_id, path, kind, format, joints, fps, window, up_axis, feature_dim, device}
  POST /infer       <- {constraints:[...], window:[a,b], seed, steps, model_id, base_motion}
                    -> {model_id, frames, joints, seed, motion|output_file, backend}
  POST /unload      -> 卸载当前模型

【约束契约】constraints 每项对应 Blender 侧挂在 Empty 上的 gmr_* 自定义属性：
  {"type":"sparse",   "joint":"foot_L", "frame":30, "loc":[x,y,z], "rot":[...]}
  {"type":"fullbody", "frame":0,        "pose":[[...], ...]}
这是三条回路共享的同一套语言。
"""

import argparse
import json
import os
import sys
import threading
import time
import traceback
from datetime import datetime, timezone
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

# 与本文件同目录
import model_config as mc

NL = chr(10)

# sidecar 是常驻进程，状态可留内存（与 Node 侧每次新进程不同）
STATE = {
    "loaded": None,
    "model": None,
    "device": "cpu",
    "started_at": None,
    "infer_count": 0,
    "last_latency_ms": None,
    # 模型配置表与由它解析出的采样入口。启动时加载一次，热重载走 /reload_config。
    "config": None,
    "config_error": None,
    "sampler": None,
}
STATE_LOCK = threading.Lock()


def load_gmr_config(path=None, quiet=False):
    """
    加载模型配置表并解析采样入口。

    配置错误不使进程退出——sidecar 是常驻服务，退出会让 Blender 侧连接直接断掉。
    改为记录 config_error 并降级到贝塞尔兜底，/health 里可见错误原因。
    """
    try:
        cfg = mc.load_config(path, quiet=quiet)
    except ValueError as e:
        with STATE_LOCK:
            STATE["config"] = None
            STATE["config_error"] = str(e)
            STATE["sampler"] = None
        print("[gmr-sidecar] 配置加载失败，降级贝塞尔兜底: " + str(e), file=sys.stderr, flush=True)
        return None

    sampler = None
    err = None
    if cfg:
        try:
            sampler = mc.resolve(cfg, "sampler", "sample")
        except ValueError as e:
            err = str(e)
            print("[gmr-sidecar] 采样入口解析失败，降级贝塞尔兜底: " + str(e), file=sys.stderr, flush=True)

    with STATE_LOCK:
        STATE["config"] = cfg
        STATE["config_error"] = err
        STATE["sampler"] = sampler
    return cfg


def now_iso():
    return datetime.now(timezone.utc).astimezone().isoformat()


def torch_available():
    try:
        import torch  # noqa: F401
        return True
    except ImportError:
        return False


def resolve_device(pref):
    if pref and pref != "auto":
        return pref
    try:
        import torch
        return "cuda" if torch.cuda.is_available() else "cpu"
    except ImportError:
        return "cpu"


def load_model_impl(spec):
    """
    按配置表载入模型。不需要改本函数即可接入模型——填 gmr/model_config.json
    的 model.module 与 model.loader 即可。

    loader 的契约是 loader(config, checkpoint_path, device) -> model。

    安全要点：loader 实现里若用 torch.load 读 .pt/.pth，务必 weights_only=True。
    否则 pickle 反序列化等同于执行任意代码——这也是 registry.js 的
    SAFE_FORMATS 只列 safetensors/onnx/npz 的原因。

    未配置 model.loader 时返回 None，/infer 走贝塞尔兜底。
    """
    path = spec.get("path")
    if path and not os.path.exists(path):
        raise FileNotFoundError("模型文件不存在: " + str(path))

    with STATE_LOCK:
        cfg = STATE["config"]

    if not cfg:
        return None

    loader = mc.resolve(cfg, "model", "loader")
    if loader is None:
        print("[gmr-sidecar] 配置未提供 model.loader，无法载入权重，将走贝塞尔兜底。", flush=True)
        return None

    device = mc.resolve_device(cfg, spec.get("device"))
    model = loader(cfg, path, device)
    if model is None:
        raise ValueError("model.loader 返回了 None。请检查其实现是否返回模型实例。")
    print("[gmr-sidecar] 模型已载入: " + str(path) + " device=" + device, flush=True)
    return model


def cubic_bezier_scalar(p0, p1, p2, p3, t):
    """标准三次贝塞尔，用于骨架期的无模型兜底插值。"""
    mt = 1.0 - t
    return (mt * mt * mt * p0
            + 3.0 * mt * mt * t * p1
            + 3.0 * mt * t * t * p2
            + t * t * t * p3)


def bezier_fallback(constraints, frame_start, frame_end):
    """
    无模型兜底：稀疏约束按帧排序，相邻两点间做三次贝塞尔插值。

    注意：控制点取三分位时三次贝塞尔精确退化为线性插值
    B(t) = a + (b - a) * t，故轨迹是分段线性、节点处一阶导不连续。
    这对验证链路的用途足够；若需真正的 C1 连续，需按相邻段斜率
    推导切线（Catmull-Rom，或 Blender F-Curve 的 auto-clamped handle）。

    这不是"生成"只是插值，但足以验证整条链路，
    并对应论文第一阶段"用传统插值顶替 ML-Betweener"的做法。
    """
    pts = []
    for c in constraints:
        frame = c.get("frame")
        loc = c.get("loc")
        if frame is None or not loc:
            continue
        pts.append((int(frame), [float(v) for v in loc]))
    pts.sort(key=lambda x: x[0])

    if not pts:
        raise ValueError("constraints 中没有可用的 (frame, loc) 数据点。")

    if len(pts) == 1:
        single = pts[0][1]
        return [list(single) for _ in range(frame_start, frame_end + 1)]

    motion = []
    for f in range(frame_start, frame_end + 1):
        if f <= pts[0][0]:
            motion.append(list(pts[0][1]))
            continue
        if f >= pts[-1][0]:
            motion.append(list(pts[-1][1]))
            continue
        seg = 0
        for i in range(len(pts) - 1):
            if pts[i][0] <= f <= pts[i + 1][0]:
                seg = i
                break
        f0, p_a = pts[seg]
        f1, p_b = pts[seg + 1]
        span = max(1, f1 - f0)
        t = (f - f0) / float(span)
        vals = []
        for axis in range(min(len(p_a), len(p_b))):
            a = p_a[axis]
            b = p_b[axis]
            c1 = a + (b - a) / 3.0
            c2 = a + 2.0 * (b - a) / 3.0
            vals.append(cubic_bezier_scalar(a, c1, c2, b, t))
        motion.append(vals)
    return motion


def infer_impl(req):
    """
    生成推理。采样入口由 gmr/model_config.json 的 sampler.module + sampler.sample 指定。

    sample 的契约是 sample(model, constraints, window, seed, config) -> list[list[float]]。

    延迟要求：交互式拖拽需 ~100-150ms。原生 DDPM 1000 步绝无可能，
    必须用 DDIM/LCM 少步采样或蒸馏模型。这是"是 rig 还是批处理"的分水岭。
    """
    constraints = req.get("constraints") or []
    if not isinstance(constraints, list) or not constraints:
        raise ValueError("constraints 必须是非空数组。")

    window = req.get("window")
    if isinstance(window, list) and len(window) == 2:
        f_start, f_end = int(window[0]), int(window[1])
    else:
        frames = [int(c["frame"]) for c in constraints if c.get("frame") is not None]
        if not frames:
            raise ValueError("未提供 window，且 constraints 中无 frame 字段，无法确定时间范围。")
        f_start, f_end = min(frames), max(frames)
    if f_end < f_start:
        raise ValueError("window 非法: [" + str(f_start) + ", " + str(f_end) + "]")

    seed = req.get("seed")
    if seed is None:
        seed = 0

    with STATE_LOCK:
        model = STATE["model"]
        loaded = STATE["loaded"]
        cfg = STATE["config"]
        sampler = STATE["sampler"]

    # 允许单次请求覆盖采样步数，便于在拖拽期用更少步数换低延迟
    if cfg and req.get("steps") is not None:
        cfg = json.loads(json.dumps({k: v for k, v in cfg.items() if k != "_meta"}))
        cfg.setdefault("sampler", {})["steps"] = int(req["steps"])

    t0 = time.time()
    if model is not None and sampler is not None:
        motion = sampler(model, constraints, [f_start, f_end], seed, cfg)
        if motion is None:
            raise ValueError("sampler.sample 返回了 None。契约要求返回 list[list[float]]。")
        motion = list(motion)
        backend = "model"
        joints = (loaded or {}).get("joints") or ((cfg or {}).get("skeleton") or {}).get("joints") or 1
        note = None
    else:
        motion = bezier_fallback(constraints, f_start, f_end)
        backend = "bezier_fallback"
        joints = 1
        if model is None and sampler is None:
            reason = "未载入模型且未配置采样入口"
        elif model is None:
            reason = "已配置采样入口但未载入模型（用 sidecar_load_model 装载）"
        else:
            reason = "已载入模型但未配置 sampler.sample"
        note = ("走三次贝塞尔插值兜底（" + reason + "）。"
                "这验证了链路但不是生成。配置 gmr/model_config.json 并载入模型后自动切换。")

    latency = int((time.time() - t0) * 1000)
    with STATE_LOCK:
        STATE["infer_count"] += 1
        STATE["last_latency_ms"] = latency

    out = {
        "model_id": (loaded or {}).get("model_id"),
        "backend": backend,
        "frames": len(motion),
        "joints": joints,
        "seed": seed,
        "window": [f_start, f_end],
        "latency_ms": latency,
        "motion": motion,
        "note": note,
    }

    # 数据量大时写文件而非塞进响应，避免污染 Agent 上下文
    if len(motion) > 200:
        out_dir = os.environ.get("GMR_MODELS_DIR") or os.getcwd()
        out_path = os.path.join(out_dir, "last_infer.json")
        try:
            with open(out_path, "w", encoding="utf-8") as f:
                json.dump({"motion": motion, "window": [f_start, f_end]}, f)
            out["output_file"] = out_path
            out["motion"] = motion[:3]
            out["note"] = (note or "") + " 完整数据已写入 output_file。"
        except Exception as e:
            out["write_warning"] = str(e)

    return out


class Handler(BaseHTTPRequestHandler):
    protocol_version = "HTTP/1.1"

    def log_message(self, fmt, *args):
        # 默认实现每条请求都刷 stderr；拖拽期每秒数十条会淹掉日志
        if os.environ.get("GMR_HTTP_VERBOSE") == "1":
            sys.stderr.write("[gmr-http] " + (fmt % args) + NL)

    def _send(self, code, payload):
        body = json.dumps(payload, ensure_ascii=False).encode("utf-8")
        self.send_response(code)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def _read_json(self):
        length = int(self.headers.get("Content-Length") or 0)
        if length <= 0:
            return {}
        raw = self.rfile.read(length)
        try:
            return json.loads(raw.decode("utf-8"))
        except Exception as e:
            raise ValueError("请求体不是合法 JSON: " + str(e))

    def do_GET(self):
        if self.path.rstrip("/") in ("/health", ""):
            with STATE_LOCK:
                payload = {
                    "status": "ok",
                    "loaded": STATE["loaded"],
                    "device": STATE["device"],
                    "started_at": STATE["started_at"],
                    "infer_count": STATE["infer_count"],
                    "last_latency_ms": STATE["last_latency_ms"],
                    "torch_available": torch_available(),
                    "backend": ("model" if (STATE["model"] is not None and STATE["sampler"] is not None)
                                else "bezier_fallback"),
                    "config_loaded": STATE["config"] is not None,
                    "config_path": ((STATE["config"] or {}).get("_meta") or {}).get("path"),
                    "sampler_ready": STATE["sampler"] is not None,
                    "config_error": STATE["config_error"],
                }
            self._send(200, payload)
        else:
            self._send(404, {"error": "未知路径 " + self.path
                             + "。可用: GET /health, POST /load_model, POST /infer, POST /unload"})

    def do_POST(self):
        route = self.path.rstrip("/")
        try:
            req = self._read_json()

            if route == "/load_model":
                spec = dict(req)
                dev = resolve_device(spec.get("device"))
                model = load_model_impl(spec)
                with STATE_LOCK:
                    STATE["model"] = model
                    STATE["device"] = dev
                    STATE["loaded"] = {
                        "model_id": spec.get("model_id"),
                        "kind": spec.get("kind"),
                        "format": spec.get("format"),
                        "path": spec.get("path"),
                        "joints": spec.get("joints"),
                        "fps": spec.get("fps"),
                        "window": spec.get("window"),
                        "up_axis": spec.get("up_axis"),
                        "feature_dim": spec.get("feature_dim"),
                        "loaded_at": now_iso(),
                    }
                warn = ""
                if model is None:
                    warn = ("已登记元数据但未真正载入权重（配置未启用，或 gmr/model_config.json "
                            "缺 model.loader），/infer 仍走贝塞尔兜底。详见 /health 的 config_error。")
                if not spec.get("up_axis"):
                    warn = warn + " 缺 up_axis：Blender 是 Z-up 而多数模型是 Y-up，缺此项会导致角色躺平。"
                resp = {"loaded": STATE["loaded"], "device": dev}
                if warn.strip():
                    resp["warning"] = warn.strip()
                self._send(200, resp)

            elif route == "/infer":
                self._send(200, infer_impl(req))

            elif route == "/unload":
                with STATE_LOCK:
                    STATE["model"] = None
                    STATE["loaded"] = None
                self._send(200, {"unloaded": True})

            elif route == "/reload_config":
                # 热重载配置表，免去改配置就要重启 sidecar、断开 Blender 连接
                cfg = load_gmr_config(req.get("path"), quiet=True)
                with STATE_LOCK:
                    self_err = STATE["config_error"]
                    ready = STATE["sampler"] is not None
                self._send(200, {
                    "reloaded": True,
                    "config_loaded": cfg is not None,
                    "config_path": ((cfg or {}).get("_meta") or {}).get("path"),
                    "sampler_ready": ready,
                    "config_error": self_err,
                    "note": "模型实例未受影响。若更换了 model.loader，需再调用 sidecar_load_model 重新装载。",
                })

            else:
                self._send(404, {"error": "未知路径 " + self.path})

        except NotImplementedError as e:
            self._send(501, {"error": str(e)})
        except (ValueError, FileNotFoundError) as e:
            self._send(400, {"error": str(e)})
        except Exception as e:
            traceback.print_exc()
            self._send(500, {"error": type(e).__name__ + ": " + str(e)})


def main():
    p = argparse.ArgumentParser(description="GMR 推理 sidecar")
    p.add_argument("--host", default="127.0.0.1")
    p.add_argument("--port", type=int, default=6091)
    p.add_argument("--model", default=None, help="启动时预载的权重路径")
    p.add_argument("--model-id", default=None)
    p.add_argument("--model-kind", default="betweener")
    p.add_argument("--joints", type=int, default=None)
    p.add_argument("--fps", type=int, default=None)
    p.add_argument("--up-axis", default=None)
    p.add_argument("--device", default="auto")
    p.add_argument("--config", default=None, help="模型配置表路径，默认 gmr/model_config.json")
    args = p.parse_args()

    STATE["started_at"] = now_iso()

    # 先加载配置表，再定设备——配置里的 runtime.device 应能参与决策
    cfg = load_gmr_config(args.config)
    STATE["device"] = mc.resolve_device(cfg, args.device)
    if cfg:
        print("[gmr-sidecar] " + mc.describe(cfg).replace(NL, NL + "[gmr-sidecar] "), flush=True)
        with STATE_LOCK:
            ready = STATE["sampler"] is not None
        if not ready:
            print("[gmr-sidecar] 警告：配置已启用但采样入口不可用，/infer 仍走贝塞尔兜底。", flush=True)

    print("[gmr-sidecar] 启动 " + args.host + ":" + str(args.port)
          + " device=" + STATE["device"] + " torch=" + str(torch_available()), flush=True)

    if args.model:
        try:
            spec = {
                "model_id": args.model_id,
                "path": args.model,
                "kind": args.model_kind,
                "joints": args.joints,
                "fps": args.fps,
                "up_axis": args.up_axis,
            }
            STATE["model"] = load_model_impl(spec)
            spec["loaded_at"] = now_iso()
            STATE["loaded"] = spec
            print("[gmr-sidecar] 预载完成: " + str(args.model), flush=True)
        except Exception as e:
            print("[gmr-sidecar] 预载失败（服务继续启动）: " + str(e), file=sys.stderr, flush=True)

    if STATE["model"] is None:
        print("[gmr-sidecar] 当前无模型，/infer 走三次贝塞尔兜底（S0 阶段，可验证链路）。", flush=True)

    srv = ThreadingHTTPServer((args.host, args.port), Handler)
    srv.daemon_threads = True
    try:
        print("[gmr-sidecar] 就绪，等待请求。", flush=True)
        srv.serve_forever()
    except KeyboardInterrupt:
        print("[gmr-sidecar] 收到中断，退出。", flush=True)
    finally:
        srv.server_close()


if __name__ == "__main__":
    main()