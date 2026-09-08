#!/usr/bin/env python3
"""
GMR 模型配置加载器。

作用：把原先散落在 train.py / sidecar.py 里的 5 处 TODO 收敛成一份 JSON 配置表。
接入模型不再需要改 Python 源码，只需填 gmr/model_config.json。

【为什么这样做】
原先的 5 处 TODO 要求使用者直接改我们的骨架代码。这有两个问题：
  1. 每次 git pull 都可能冲突；
  2. 换模型时得先把上一个模型的代码删掉，而不是改一行配置。
改为配置驱动后，骨架代码保持稳定，模型接入变成"填表 + 提供符合契约的函数"。

【契约】
配置里每个 module/函数名对，都会被解析成一个可调用对象。各自签名：

  model.factory      factory(config, device) -> model
  model.loader       loader(config, checkpoint_path, device) -> model
  dataset.loader     loader(path, config) -> Iterable
  training.trainStep step(model, batch, optimizer, config) -> dict
  checkpoint.saver   saver(model, path, meta) -> None
  sampler.sample     sample(model, constraints, window, seed, config) -> list[list[float]]

其中 config 是完整配置字典，便于被调函数读取自己那一节的参数。

【未配置时】
model_config.json 不存在或 enabled=false 时，load_config() 返回 None。
调用方据此走降级路径：train.py 走 dry-run，sidecar.py 走贝塞尔兜底。
此时不需要 PyTorch，整条链路仍可验证。
"""

import importlib
import json
import os
import sys

NL = chr(10)

CONFIG_FILENAME = "model_config.json"
EXAMPLE_FILENAME = "model_config.example.json"


def gmr_dir():
    """返回 gmr/ 目录的绝对路径。本文件在 gmr/python/ 下。"""
    return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def config_path(explicit=None):
    if explicit:
        return os.path.abspath(explicit)
    env = os.environ.get("GMR_MODEL_CONFIG")
    if env:
        return os.path.abspath(env)
    return os.path.join(gmr_dir(), CONFIG_FILENAME)


def strip_comment_keys(obj):
    """
    递归移除以下划线开头的键。

    配置示例里用 _说明 / _警告 等键承载文档，它们对程序无意义。
    保留在文件里对人有用，但不该混进传给模型的 config。
    """
    if isinstance(obj, dict):
        return {k: strip_comment_keys(v) for k, v in obj.items() if not str(k).startswith("_")}
    if isinstance(obj, list):
        return [strip_comment_keys(v) for v in obj]
    return obj


def _validate(cfg, path):
    """启动期校验。只查结构与必填项，不尝试 import——import 失败留给 resolve() 报更精确的错。"""
    errors = []

    skel = cfg.get("skeleton") or {}
    if not skel:
        errors.append("缺少 skeleton 节。Blender 侧 retarget 依赖它。")
    else:
        if not skel.get("joints"):
            errors.append("skeleton.joints 未填（关节数）。")
        up = skel.get("upAxis")
        if not up:
            errors.append("skeleton.upAxis 未填。Blender 是 Z-up 而多数模型是 Y-up，缺此项会导致角色躺平。")
        elif str(up).upper() not in ("X", "Y", "Z"):
            errors.append('skeleton.upAxis 应为 "X" / "Y" / "Z"，当前为 "' + str(up) + '"。')

    # 各节的 module 与函数名必须成对出现，缺一半是最容易犯的错
    pairs = [
        ("model", ["factory", "loader"]),
        ("dataset", ["loader"]),
        ("training", ["trainStep"]),
        ("checkpoint", ["saver"]),
        ("sampler", ["sample"]),
    ]
    for section, fnkeys in pairs:
        node = cfg.get(section)
        if node is None:
            continue
        if not isinstance(node, dict):
            errors.append(section + " 必须是对象。")
            continue
        has_any_fn = any(node.get(k) for k in fnkeys)
        if has_any_fn and not node.get("module"):
            errors.append(section + " 指定了函数名但缺 module，无法定位代码。")

    if errors:
        msg = "配置校验失败 (" + path + "):"
        for e in errors:
            msg += NL + "  - " + e
        raise ValueError(msg)


def _apply_sys_path(cfg, quiet):
    """把 runtime.sysPath 插入 sys.path 头部，使 import 能找到上游仓库。"""
    runtime = cfg.get("runtime") or {}
    paths = runtime.get("sysPath") or []
    if isinstance(paths, str):
        paths = [paths]
    for p in paths:
        ap = os.path.abspath(os.path.expanduser(str(p)))
        if not os.path.isdir(ap):
            print("[gmr-config] 警告：runtime.sysPath 中的目录不存在，已跳过: " + ap,
                  file=sys.stderr, flush=True)
            continue
        if ap not in sys.path:
            sys.path.insert(0, ap)
            if not quiet:
                print("[gmr-config] sys.path += " + ap, flush=True)


def load_config(explicit=None, quiet=False):
    """
    读取并校验配置。

    返回 dict（已剥离注释键、已注入 _meta），或 None 表示未启用。
    校验失败会抛 ValueError——宁可在启动时明确失败，也不要带着半截配置跑训练。
    """
    path = config_path(explicit)
    if not os.path.exists(path):
        if not quiet:
            print("[gmr-config] 未找到 " + path, flush=True)
            print("[gmr-config] 将使用降级路径（训练走 dry-run / 推理走贝塞尔兜底）。", flush=True)
            print("[gmr-config] 如需接入真实模型，参考 " + os.path.join(gmr_dir(), EXAMPLE_FILENAME), flush=True)
        return None

    try:
        with open(path, "r", encoding="utf-8") as f:
            raw = json.load(f)
    except json.JSONDecodeError as e:
        raise ValueError("配置文件不是合法 JSON: " + path + NL + "  " + str(e))
    except OSError as e:
        raise ValueError("无法读取配置文件 " + path + ": " + str(e))

    if not isinstance(raw, dict):
        raise ValueError("配置文件顶层必须是 JSON 对象: " + path)

    if not raw.get("enabled"):
        if not quiet:
            print("[gmr-config] " + path + " 中 enabled=false，使用降级路径。", flush=True)
        return None

    cfg = strip_comment_keys(raw)
    cfg["_meta"] = {"path": path, "gmrDir": gmr_dir()}

    _validate(cfg, path)
    _apply_sys_path(cfg, quiet)
    return cfg


# ---------- 入口解析与辅助 ----------


def resolve(cfg, section, fnkey, required=False):
    """
    按配置解析出一个可调用对象。

    找不到时：required=True 抛错，否则返回 None 让调用方降级。
    错误消息刻意写得具体——接模型时最耗时的就是判断"到底是路径不对还是函数名不对"。
    """
    if not cfg:
        return None
    node = cfg.get(section) or {}
    module_name = node.get("module")
    fn_name = node.get(fnkey)
    if not module_name or not fn_name:
        if required:
            raise ValueError(
                "配置缺少 " + section + ".module 或 " + section + "." + fnkey + "，无法解析该入口。"
            )
        return None

    try:
        mod = importlib.import_module(module_name)
    except ImportError as e:
        hint = ""
        runtime = cfg.get("runtime") or {}
        if not runtime.get("sysPath"):
            hint = NL + "  提示：未配置 runtime.sysPath。若模型代码在独立仓库中，需把仓库根目录加进去。"
        raise ValueError(
            "无法 import 模块 '" + module_name + "'（来自 " + section + ".module）: " + str(e) + hint
        )

    fn = getattr(mod, fn_name, None)
    if fn is None:
        available = [n for n in dir(mod) if not n.startswith("_")][:20]
        raise ValueError(
            "模块 '" + module_name + "' 中没有 '" + fn_name + "'（来自 " + section + "." + fnkey + "）。"
            + NL + "  该模块可见的名字: " + ", ".join(available)
        )
    if not callable(fn):
        raise ValueError("'" + module_name + "." + fn_name + "' 不可调用。")
    return fn


def skeleton_meta(cfg):
    """
    提取骨架契约，格式与 registry.js 的 meta 字段对齐，
    便于训练完成后写入 done 文件自动登记模型。
    """
    if not cfg:
        return {
            "joints": None,
            "fps": None,
            "window": None,
            "up_axis": None,
            "feature_dim": None,
            "notes": "未配置 model_config.json，此为降级路径产物，不含真实权重。",
        }
    skel = cfg.get("skeleton") or {}
    return {
        "joints": skel.get("joints"),
        "fps": skel.get("fps"),
        "window": skel.get("window"),
        "up_axis": skel.get("upAxis"),
        "feature_dim": skel.get("featureDim"),
        "notes": "由 " + str((cfg.get("_meta") or {}).get("path")) + " 生成。",
    }


def resolve_device(cfg, cli_pref=None):
    """
    设备选择优先级：命令行 > 配置 > auto 探测。
    torch 缺失时降级 cpu，使骨架在无 PyTorch 环境也能跑通链路。
    """
    pref = cli_pref
    if not pref or pref == "auto":
        pref = ((cfg or {}).get("runtime") or {}).get("device") or "auto"
    if pref and pref != "auto":
        return pref
    try:
        import torch
        return "cuda" if torch.cuda.is_available() else "cpu"
    except ImportError:
        return "cpu"


def describe(cfg):
    """供 CLI 打印的简报。"""
    if not cfg:
        return "未启用模型配置（降级路径）"
    skel = cfg.get("skeleton") or {}
    lines = [
        "配置: " + str((cfg.get("_meta") or {}).get("path")),
        "名称: " + str(cfg.get("name")) + "  类型: " + str(cfg.get("kind")),
        "骨架: joints=" + str(skel.get("joints"))
        + " fps=" + str(skel.get("fps"))
        + " window=" + str(skel.get("window"))
        + " upAxis=" + str(skel.get("upAxis"))
        + " featureDim=" + str(skel.get("featureDim")),
    ]
    sampler = cfg.get("sampler") or {}
    if sampler:
        lines.append("采样: type=" + str(sampler.get("type"))
                     + " steps=" + str(sampler.get("steps")))
    return NL.join(lines)


if __name__ == "__main__":
    # 直接运行本文件即可校验配置，接模型时用它先排错
    import argparse

    p = argparse.ArgumentParser(description="校验 GMR 模型配置表")
    p.add_argument("--config", default=None)
    p.add_argument("--resolve", action="store_true",
                   help="同时尝试 import 并解析全部入口（需要模型代码就位）")
    a = p.parse_args()
    try:
        cfg = load_config(a.config)
    except ValueError as e:
        print(str(e), file=sys.stderr)
        sys.exit(1)
    print(describe(cfg))
    if cfg and a.resolve:
        print("")
        targets = [
            ("model", "factory"), ("model", "loader"),
            ("dataset", "loader"), ("training", "trainStep"),
            ("checkpoint", "saver"), ("sampler", "sample"),
        ]
        failed = 0
        for sec, key in targets:
            try:
                fn = resolve(cfg, sec, key)
                mark = "OK   " if fn else "-    "
                detail = (" -> " + getattr(fn, "__name__", "?")) if fn else " (未配置)"
                print(mark + sec + "." + key + detail)
            except ValueError as e:
                failed += 1
                print("FAIL " + sec + "." + key)
                print("     " + str(e).replace(NL, NL + "     "))
        sys.exit(1 if failed else 0)