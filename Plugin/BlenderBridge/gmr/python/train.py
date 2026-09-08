#!/usr/bin/env python3
"""
GMR 训练脚本。配置驱动，不需要改本文件即可接入模型。

【与旧版的区别】
旧版留了 3 处 TODO（build_model / train_one_epoch / save_checkpoint），要求使用者
直接改本文件。现在这三处全部由 gmr/model_config.json 描述：填表指定 module 与函数名，
本脚本负责 import 并按契约调用。骨架代码保持稳定，git pull 不冲突。

【与 jobs.js 之间的契约（改动需同步）】
  1. 命令行参数：--dataset --out-dir --job-id --done-file --kind
     以及可选的 --epochs --batch-size --lr --window --device --seed --resume-from
  2. 退出前必须写 --done-file 指向的 JSON。这是 Node 侧状态机的唯一真相，
     因为父进程 detached 后拿不到 exit code。
  3. done 文件字段：
       exit_code    int，0 表示成功
       finished_at  ISO8601
       checkpoint   产出的权重路径，成功时 Node 会自动登记进模型注册表
       meta         骨架契约 {joints, fps, window, up_axis, feature_dim}
       metrics      任意训练指标
       error        失败原因
  4. meta.up_axis 极其重要。模型多为 Y-up 而 Blender 是 Z-up，搞错会让角色躺平。
     该值由 model_config.json 的 skeleton.upAxis 提供。
  5. stdout/stderr 已被 jobs.js 重定向到 jobs/<id>.log，直接 print 即可。

【降级路径】
未配置 model_config.json 或 enabled=false 时走 dry-run：模拟训练、产出占位
checkpoint。用途是验证 Node 侧状态机、日志读取、SIGTERM 取消、done 解析、
自动登记这整条链路，且不需要 PyTorch。

【SIGTERM 处理】
cancel_job 发的是 SIGTERM。捕获后保存当前 checkpoint、写 done 文件再退出，
以免取消训练就丢掉全部进度。
"""

import argparse
import json
import os
import signal
import sys
import time
import traceback
from datetime import datetime, timezone

# 与本文件同目录，直接 import
import model_config as mc

NL = chr(10)

# 全局中断标志。信号处理器里只置位，不做重活。
_INTERRUPTED = False


def _on_signal(signum, frame):
    global _INTERRUPTED
    _INTERRUPTED = True
    print("[gmr] 收到信号 " + str(signum) + "，将在当前 epoch 结束后保存并退出。", flush=True)


def now_iso():
    return datetime.now(timezone.utc).astimezone().isoformat()


def write_done(done_file, exit_code, checkpoint=None, meta=None, metrics=None, error=None):
    """写 done 文件。先写临时文件再 rename，避免 Node 读到半截 JSON。"""
    payload = {
        "exit_code": int(exit_code),
        "finished_at": now_iso(),
    }
    if checkpoint:
        payload["checkpoint"] = os.path.abspath(checkpoint)
    if meta:
        payload["meta"] = meta
    if metrics:
        payload["metrics"] = metrics
    if error:
        payload["error"] = str(error)[:2000]

    tmp = done_file + ".tmp"
    try:
        parent = os.path.dirname(done_file)
        if parent:
            os.makedirs(parent, exist_ok=True)
        with open(tmp, "w", encoding="utf-8") as f:
            json.dump(payload, f, ensure_ascii=False, indent=2)
        os.replace(tmp, done_file)
        print("[gmr] 已写 done 文件: " + done_file, flush=True)
    except Exception as e:
        # 写不出 done 文件时 Node 会判定为"进程消失但无 done"，属于可诊断的失败
        print("[gmr] 严重：无法写 done 文件: " + str(e), file=sys.stderr, flush=True)


def parse_args():
    p = argparse.ArgumentParser(description="GMR 动作生成模型训练（配置驱动）")
    p.add_argument("--dataset", required=True, help="数据集目录或文件")
    p.add_argument("--out-dir", required=True, help="checkpoint 输出目录")
    p.add_argument("--job-id", required=True, help="任务 ID，由 Node 侧生成")
    p.add_argument("--done-file", required=True, help="完成标记文件路径")
    p.add_argument("--kind", default="betweener", choices=["betweener", "poser", "other"])
    p.add_argument("--config", default=None, help="模型配置表路径，默认 gmr/model_config.json")
    p.add_argument("--epochs", type=int, default=None)
    p.add_argument("--batch-size", type=int, default=None)
    p.add_argument("--lr", type=float, default=None)
    p.add_argument("--window", type=int, default=None)
    p.add_argument("--device", default="auto")
    p.add_argument("--seed", type=int, default=None)
    p.add_argument("--resume-from", default=None, help="从已有 checkpoint 续训")
    return p.parse_args()


def merge_hparams(args, cfg):
    """
    合并超参。优先级：命令行 > 配置表 > 内置默认。

    命令行优先是刻意的——Agent 通过 train 命令传参时应能覆盖配置表，
    便于同一份配置跑不同规模的实验。
    """
    tr = (cfg or {}).get("training") or {}
    skel = (cfg or {}).get("skeleton") or {}

    def pick(cli_val, cfg_val, default):
        if cli_val is not None:
            return cli_val
        if cfg_val is not None:
            return cfg_val
        return default

    return {
        "epochs": pick(args.epochs, tr.get("epochs"), 10),
        "batch_size": pick(args.batch_size, tr.get("batchSize"), 32),
        "lr": pick(args.lr, tr.get("lr"), 1e-4),
        "window": pick(args.window, skel.get("window"), 64),
        "seed": pick(args.seed, (cfg or {}).get("runtime", {}).get("seed"), 0),
        "weight_decay": tr.get("weightDecay", 0.0),
        "grad_clip": tr.get("gradClip"),
        "save_every": tr.get("saveEveryEpochs", 1),
        "optimizer": tr.get("optimizer", "AdamW"),
    }


def build_optimizer(model, hp, cfg):
    """
    按配置名构造优化器。
    模型为 None（dry-run）或无 torch 时返回 None，训练步自行处理。
    """
    if model is None:
        return None
    try:
        import torch
    except ImportError:
        print("[gmr] 未安装 PyTorch，跳过优化器构造。", flush=True)
        return None
    name = str(hp.get("optimizer") or "AdamW")
    params = [p for p in model.parameters() if p.requires_grad] if hasattr(model, "parameters") else None
    if not params:
        print("[gmr] 模型无可训练参数，跳过优化器构造。", flush=True)
        return None
    cls = getattr(torch.optim, name, None)
    if cls is None:
        raise ValueError("torch.optim 中没有优化器 '" + name + "'（来自 training.optimizer）。")
    kwargs = {"lr": hp["lr"]}
    if hp.get("weight_decay"):
        kwargs["weight_decay"] = hp["weight_decay"]
    return cls(params, **kwargs)


def dry_run_step(epoch):
    """降级路径的模拟训练步。用于验证状态机，不产生真实权重。"""
    time.sleep(1.0)
    return {"loss": round(1.0 / (epoch + 1), 6), "dry_run": True}


def dry_run_save(out_dir, args, hp, epoch):
    """降级路径的占位 checkpoint。"""
    os.makedirs(out_dir, exist_ok=True)
    ckpt = os.path.join(out_dir, "checkpoint.json")
    with open(ckpt, "w", encoding="utf-8") as f:
        json.dump({
            "placeholder": True,
            "job_id": args.job_id,
            "kind": args.kind,
            "epoch": epoch,
            "window": hp["window"],
            "note": "dry-run 占位文件，不含真实权重。配置 gmr/model_config.json 并设 enabled=true 后走真实训练。",
        }, f, ensure_ascii=False, indent=2)
    return ckpt


# ---------- 主流程 ----------


def main():
    args = parse_args()
    signal.signal(signal.SIGTERM, _on_signal)
    signal.signal(signal.SIGINT, _on_signal)

    ckpt = None
    metrics = {}
    meta = None

    try:
        # 配置加载失败应立即失败，不要带着半截配置跑几小时
        cfg = mc.load_config(args.config)
        device = mc.resolve_device(cfg, args.device)
        hp = merge_hparams(args, cfg)
        meta = mc.skeleton_meta(cfg)

        print("[gmr] job=" + args.job_id + " kind=" + args.kind + " device=" + device, flush=True)
        print("[gmr] " + mc.describe(cfg).replace(NL, NL + "[gmr] "), flush=True)
        print("[gmr] dataset=" + args.dataset, flush=True)
        print("[gmr] out_dir=" + args.out_dir, flush=True)
        print("[gmr] epochs=" + str(hp["epochs"])
              + " batch=" + str(hp["batch_size"])
              + " lr=" + str(hp["lr"])
              + " window=" + str(hp["window"])
              + " seed=" + str(hp["seed"]), flush=True)

        if not os.path.exists(args.dataset):
            raise FileNotFoundError("数据集不存在: " + args.dataset)

        # 按配置解析五个入口。任一缺失即降级为 dry-run，而非半真半假地跑。
        f_factory = mc.resolve(cfg, "model", "factory")
        f_loader = mc.resolve(cfg, "model", "loader")
        f_data = mc.resolve(cfg, "dataset", "loader")
        f_step = mc.resolve(cfg, "training", "trainStep")
        f_save = mc.resolve(cfg, "checkpoint", "saver")

        real_mode = bool(cfg and f_step and (f_factory or f_loader))
        if not real_mode:
            print("[gmr] 进入 dry-run 模式。", flush=True)
            if cfg:
                missing = []
                if not f_factory and not f_loader:
                    missing.append("model.factory 或 model.loader")
                if not f_step:
                    missing.append("training.trainStep")
                print("[gmr] 原因：配置已启用但缺少 " + "、".join(missing) + "。", flush=True)
            print("[gmr] dry-run 会走完整状态机并产出占位 checkpoint，用于验证链路而非真实训练。", flush=True)

        # 固定随机种子，让实验可复现
        if hp["seed"]:
            try:
                import random
                random.seed(hp["seed"])
                import torch
                torch.manual_seed(hp["seed"])
            except ImportError:
                pass

        model = None
        optimizer = None
        dataloader = None

        if real_mode:
            if args.resume_from:
                if not f_loader:
                    raise ValueError("指定了 --resume-from 但配置缺少 model.loader，无法载入已有权重。")
                print("[gmr] 从 checkpoint 续训: " + args.resume_from, flush=True)
                model = f_loader(cfg, args.resume_from, device)
            else:
                if not f_factory:
                    raise ValueError("配置缺少 model.factory，无法构造模型（若要续训请传 --resume-from）。")
                model = f_factory(cfg, device)
            if model is None:
                raise ValueError("model.factory / model.loader 返回了 None。请检查其实现是否返回模型实例。")

            optimizer = build_optimizer(model, hp, cfg)

            if f_data:
                dataloader = f_data(args.dataset, cfg)
                if dataloader is None:
                    raise ValueError("dataset.loader 返回了 None。请检查其实现是否返回可迭代对象。")
            else:
                print("[gmr] 警告：未配置 dataset.loader，trainStep 将收到 batch=None，需自行取数据。", flush=True)

        history = []
        for epoch in range(hp["epochs"]):
            if _INTERRUPTED:
                print("[gmr] 在 epoch " + str(epoch) + " 前被中断。", flush=True)
                break

            if real_mode:
                epoch_metrics = run_epoch(model, optimizer, dataloader, f_step, cfg, hp, epoch)
            else:
                epoch_metrics = dry_run_step(epoch)

            history.append(epoch_metrics)
            print("[gmr] epoch " + str(epoch + 1) + "/" + str(hp["epochs"])
                  + " " + json.dumps(epoch_metrics, ensure_ascii=False), flush=True)

            # 按 saveEveryEpochs 存盘，取消训练时不至于全丢
            should_save = ((epoch + 1) % max(1, int(hp["save_every"])) == 0) or (epoch + 1 == hp["epochs"])
            if should_save or _INTERRUPTED:
                if real_mode and f_save:
                    os.makedirs(args.out_dir, exist_ok=True)
                    fname = ((cfg.get("checkpoint") or {}).get("filename")) or "model.safetensors"
                    target = os.path.join(args.out_dir, fname)
                    save_meta = dict(meta or {})
                    save_meta["epoch"] = epoch
                    save_meta["job_id"] = args.job_id
                    f_save(model, target, save_meta)
                    ckpt = target
                elif real_mode and not f_save:
                    print("[gmr] 警告：未配置 checkpoint.saver，本轮权重未保存。", flush=True)
                else:
                    ckpt = dry_run_save(args.out_dir, args, hp, epoch)

        metrics = {
            "epochs_completed": len(history),
            "history": history[-20:],
            "interrupted": _INTERRUPTED,
            "mode": "real" if real_mode else "dry_run",
        }
        if meta is not None:
            meta = dict(meta)
            meta["window"] = hp["window"]

        if _INTERRUPTED:
            # 被取消也算有产出，但明确标为非正常完成
            write_done(args.done_file, 1, checkpoint=ckpt, meta=meta, metrics=metrics,
                       error="训练被信号中断（cancel_job）。已保存最后一个 checkpoint。")
            return 1

        if ckpt is None:
            write_done(args.done_file, 1, meta=meta, metrics=metrics,
                       error="训练结束但没有产出 checkpoint。请检查 checkpoint.saver 配置。")
            return 1

        write_done(args.done_file, 0, checkpoint=ckpt, meta=meta, metrics=metrics)
        print("[gmr] 训练完成。", flush=True)
        return 0

    except Exception as e:
        traceback.print_exc()
        write_done(args.done_file, 1, checkpoint=ckpt, meta=meta, metrics=metrics,
                   error=type(e).__name__ + ": " + str(e))
        return 1


def run_epoch(model, optimizer, dataloader, f_step, cfg, hp, epoch):
    """
    真实训练的一个 epoch。

    trainStep 的契约是 step(model, batch, optimizer, config) -> dict。
    梯度裁剪与 optimizer.step() 由 trainStep 内部负责——因为不同模型的
    反向传播时机差异很大（如 diffusion 的多步损失），框架不该越权代管。
    本函数只负责遍历、汇总与中断检查。
    """
    totals = {}
    count = 0
    batches = dataloader if dataloader is not None else [None]

    for batch in batches:
        if _INTERRUPTED:
            print("[gmr] epoch 内检测到中断，提前结束本轮。", flush=True)
            break
        step_metrics = f_step(model, batch, optimizer, cfg)
        count += 1
        if isinstance(step_metrics, dict):
            for k, v in step_metrics.items():
                if isinstance(v, (int, float)):
                    totals[k] = totals.get(k, 0.0) + float(v)
        log_every = ((cfg.get("training") or {}).get("logEverySteps")) or 0
        if log_every and count % int(log_every) == 0:
            avg_now = {k: round(v / count, 6) for k, v in totals.items()}
            print("[gmr]   step " + str(count) + " " + json.dumps(avg_now, ensure_ascii=False), flush=True)

    if count == 0:
        return {"warning": "本轮没有任何 batch 被处理", "steps": 0}
    out = {k: round(v / count, 6) for k, v in totals.items()}
    out["steps"] = count
    return out


if __name__ == "__main__":
    sys.exit(main())