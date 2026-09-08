# GMR — Generative Motion Rig 复刻地基

BlenderBridge 的可选扩展模块（ex）。为复刻 Disney Research 的生成式动作绑定工作流打地基。

**删除整个 `gmr/` 目录，BlenderBridge 的 6 个原生子命令照常工作。** 主体只有一处 try-require，不构成硬依赖。

---

## 来龙去脉

2026 年 8 月，读到 Disney Research | Studios 与 ETH Zurich 的这篇论文：

> **A Generative Motion Rig for Artist-Driven Motion Authoring**
> Jakob Buhmann, Dhruv Agrawal, Dominik Borer, Luca Vögeli, Robert W. Sumner, Martin Guay
> SIGGRAPH Talks '26 · DOI [10.1145/3799818.3812088](https://doi.org/10.1145/3799818.3812088) · Open Access
> 官方页面：<https://studios.disneyresearch.com/2026/07/16/a-generative-motion-rig-for-artist-driven-motion-authoring>

它做的事，一句话讲清：**把动作生成模型包装成一套 Blender 里的 Rig，让动画师像调传统控制器一样去调 AI 动作。** 不是又做一个"一键生成动作"的按钮，而是让生成能力长进既有的创作流程里。

论文提出的 **generative keyframing** 工作流有四个控制维度：稀疏姿势（sparse poses）、控制手柄（handles）、窗口长度（window length）、噪声采样（noise sampling）。艺术家拖动神经动作曲线（NMC, Neural Motion Curves）上的控制点，模型实时重新生成整段动作。

### 读完之后的判断

论文本身是 3 页 Talk，模型权重没有公开：

| 论文用的 | 状态 | 我们的替代 |
|---|---|---|
| **IBMM**（Implicit Bézier Motion Model, MIG 2025）| 未开源 | **CondMDI**（Flexible Motion In-betweening with Diffusion, 2024）——论文原文自己点名"our framework is compatible with other generative motion engines"并引用了它 |
| **ML-Poser**（基于 ProtoRes, ICLR 2022 的神经 IK）| 权重未公开 | 第一版直接用 **Blender 原生 IK** 顶替，省掉一整个模型 |

但真正的结论是：**这篇论文最值钱的部分不需要一行 PyTorch。**

generative keyframing 的交互手感、生成层与传统层的双层取舍、以及"从 GMR 切回传统 Rig 时只传当前帧、绝不烘焙全序列"这个洞察——全都是纯 `bpy` 的设计智慧。模型是可替换的零件。

所以这个模块的定位是：**先把地基和管道打好，模型晚点接。**

---

## 架构：三条不同频率的回路

这是整个设计里最重要的一个决定。

```
慢回路（秒级）      VCP → BlenderBridge → blender-mcp:6090 → Blender Add-on
                   Agent 语义编排：读场景、布约束、批量摆关键帧、查 bpy 文档、截图看结果

快回路（~100ms）    Blender GMR Add-on → sidecar:6091          【不经过 VCP】
                   拖拽手柄时的实时推理

管理回路（秒级）    VCP → BlenderBridge → gmr ex → sidecar:6091
                   起停 sidecar、装载模型、单次试跑
```

### 为什么快回路必须绕开 blender-mcp

BlenderBridge 的 README 自己写明了两条约束：

- `BLENDER_BUSY`：上游 blender-mcp **只支持单并发**
- `REQUEST_TIMEOUT_MS=60000`：双跳链路的超时量级

而 GMR 的手感要求是拖拽到画面更新 **~100ms**，且拖拽期间每秒产生几十次事件。把这种回路塞进 `VCP → HTTP → blender-mcp → TCP → Add-on` 的双跳单并发管道，结果一定是请求堆积 + 全链路锁死。

所以 **sidecar 与 blender-mcp 是并列关系，不是串联**。

### BlenderBridge 的角色重定位

从"唯一通道"变成**导演席**。它在这个架构里恰好非常适合这个角色，因为现有的三个域给了 Agent 别的桥接给不了的能力：

- `screenshot` + `render` —— **视觉反馈闭环**，Agent 能"看见"生成的动作并据此调整约束
- `docs` —— 开发期直接查 `bpy` API 与手册，不靠记忆猜已改名的接口
- `exec` —— 整个慢回路的载体

### 一个刻意的设计决策：不给上游打补丁

MCP 工具列表来自 blender-mcp 服务端，GMR add-on 注册的 operator **不会**自动变成 MCP 工具。两条路：

- ✗ fork blender-mcp 加 `gmr_*` 工具 —— 破坏 README 已立的"上游零补丁，`git pull` 永不冲突"原则
- ✓ **GMR add-on 暴露稳定的 `gmr.*` 模块 API，Agent 经现有 `execute_blender_code` 调用**

这让 `exec` 域从"逃生舱"升格为正式的 Agent 语义通道，59 个现有工具一个都不用动。

---

## 约束的单一真相源

让三条回路优雅共存的枢纽：**约束不存在内存里、不存在 sidecar 里，而是以自定义属性挂在 Blender 场景对象上。**

```
Empty "GMR_handle_foot_L"
  ["gmr_type"]        = "sparse"        # sparse | fullbody
  ["gmr_joint"]       = "foot_L"
  ["gmr_frame"]       = 30
  ["gmr_seed"]        = 8471223         # 噪声种子
Scene
  ["gmr_window"]      = [12, 96]        # 时间评估边界
  ["gmr_base_action"] = "mocap_jump"    # 编辑模式的 inpainting 底座
```

于是两条回路只是**同一份文档的两个编辑器**：动画师拖 Empty 改它，Agent 通过 `exec` 也改它，add-on 的 `depsgraph` handler 一视同仁地监听并重新生成。**根本没有第二份状态，所以没有同步问题。**

白送三个好处：

1. 随 `.blend` 存盘，重开文件约束还在
2. seed 落盘即可复现 —— 对应论文强调的 noise resampling 变体可追溯
3. Agent 能读到**完整创作意图**，而不只是结果动作

---

## 目录结构

```
BlenderBridge/
├── BlenderBridge.js               桥接本体（仅一处 try-require 挂载 GMR）
├── build_addon.py                 Add-on 打包脚本（纯标准库，无需装 Blender）
├── blander-mcp/                   上游 blender_mcp 本体（随插件附带）
├── gmr/                           ← 本模块
│   ├── index.js                   统一入口与命令分发（主体唯一 require 的文件）
│   ├── config.js                  配置解析，所有路径可经环境变量覆盖
│   ├── registry.js                模型注册表（含骨架契约元数据）
│   ├── jobs.js                    训练任务管理（detached spawn + 落盘状态机）
│   ├── sidecar.js                 推理进程的客户端与生命周期管理
│   ├── model_config.example.json  模型配置模板（复制为 model_config.json 使用）
│   ├── 模型接入说明.md              六个函数契约、排错清单、安全须知
│   ├── python/
│   │   ├── model_config.py        配置加载与校验器（可独立运行排错）
│   │   ├── train.py               训练主流程（读配置表）
│   │   └── sidecar.py             推理服务（读配置表）
│   └── README.md                  本文件
└── gmr_data/                      运行时数据（首次调用自动创建）
    ├── models/                    checkpoint + registry.json
    ├── jobs/                      <jobId>.json 状态 / .log 日志 / .done 完成标记
    └── datasets/                  数据集
```

---

## 命令一览（15 个）

用 `gmr_help` 可随时取得完整参数说明。

### 总览

| 命令 | 说明 |
|---|---|
| `gmr_status` | 模型数、任务数、sidecar 可达性、脚本就绪状态 |
| `gmr_help` | 完整命令说明、架构要点、约束契约、注意事项 |

### 模型仓库

| 命令 | 参数 |
|---|---|
| `import_model` | `source`(必需,绝对路径) `name` `kind` `copy` `meta` |
| `list_models` | `kind`(可选,过滤) |
| `update_model` | `model_id`(必需) + `joints`/`fps`/`window`/`up_axis`/`feature_dim`/`notes` |
| `remove_model` | `model_id`(必需) `delete_file`(可选) |

`kind` 取值对应论文服务端的两个模块：`betweener`（ML-Betweener 类）、`poser`（ML-Poser 类）、`other`。

### 训练任务

| 命令 | 参数 |
|---|---|
| `train` | `dataset`(必需) `name` `kind` `script` `epochs` `batch_size` `lr` `window` `device` `seed` `resume_from` `extra_args` |
| `list_jobs` | `status`(可选) |
| `job_status` | `job_id`(必需) `tail_bytes`(可选) |
| `cancel_job` | `job_id`(必需) |

### 推理服务

| 命令 | 参数 |
|---|---|
| `sidecar_start` | `model_id`(可选,预载) `device` `script` |
| `sidecar_stop` | — |
| `sidecar_status` | — |
| `sidecar_load_model` | `model_id`(必需) `device`(可选) |
| `infer` | `constraints`(必需) `window` `seed` `steps` `model_id` `base_motion` |

调用示例：

```
<<<[TOOL_REQUEST]>>>
tool_name:「始」BlenderBridge「末」,
command:「始」gmr_status「末」
<<<[END_TOOL_REQUEST]>>>
```

---

## 当前状态：地基已成，模型待接

### 已经能跑的

- ✅ 命令分发与主体挂载（15 个命令全部注册，未命中原生命令时自动路由）
- ✅ 模型注册表：导入、列举、元数据补齐、注销，含原子写入与指纹识别
- ✅ 训练任务状态机：detached spawn、日志尾部读取、SIGTERM 取消、done 文件解析、成功后自动登记模型
- ✅ sidecar 生命周期：起停、pid 文件、健康检查、热装载模型
- ✅ **无模型时 `/infer` 走三次贝塞尔插值兜底** —— 不装 PyTorch 也能验证整条链路

最后一条是刻意的：它对应论文第一阶段"用传统插值顶替 ML-Betweener"的做法。

### 接模型：填配置表，不改代码

初版在 Python 里留了 5 处 `TODO` 要求使用者改我们的骨架代码。现已改为**配置驱动**——那 5 处变成 `gmr/model_config.json` 里的 5 组 `module` + 函数名：

| 原 TODO | 现在的配置项 | 契约 |
|---|---|---|
| `build_model()` | `model.factory` | `factory(config, device) -> model` |
| `train_one_epoch()` | `training.trainStep` | `step(model, batch, optimizer, config) -> dict` |
| `save_checkpoint()` | `checkpoint.saver` | `saver(model, path, meta) -> None` |
| `load_model_impl()` | `model.loader` | `loader(config, ckpt_path, device) -> model` |
| `infer_impl()` | `sampler.sample` | `sample(model, constraints, window, seed, config) -> list[list[float]]` |

三步接入：

```bash
cp model_config.example.json model_config.json   # ① 复制模板
$EDITOR model_config.json                        # ② 填 enabled=true / sysPath / 函数名
python3 python/model_config.py --resolve         # ③ 校验并解析全部入口
```

**完整说明见「模型接入说明.md」**，含六个函数的示例实现、部分配置的行为、热重载、排错清单。

这样改的好处：骨架代码保持稳定，`git pull` 不冲突；换模型时改配置而非删代码。

### 还完全没写的

**GMR add-on 本身。** 这是快回路的客户端，也是论文交互范式的载体，需要在 Blender 里实现：

- NMC 视口绘制（`gpu` 模块 + `SpaceView3D.draw_handler_add`）
- Empty handle 拖拽监听（`depsgraph_update_post` + 防抖 + 丢弃过期请求）
- 生成层 / 传统层双层结构与 Rig 切换
- IK 锁脚（对付生成模型必然出现的足部滑动）
- Undo 栈整合（`bl_options = {'REGISTER','UNDO'}`）

---

## 配置

全部可选，未设置时用括号内默认值。写进 BlenderBridge 的 `config.env` 即可。

```
GMR_ROOT=<插件目录>/gmr_data      # 数据根目录
GMR_MODELS_DIR=<GMR_ROOT>/models
GMR_JOBS_DIR=<GMR_ROOT>/jobs
GMR_DATASETS_DIR=<GMR_ROOT>/datasets

GMR_PYTHON=python3                # 强烈建议指向装有 PyTorch 的独立 venv
GMR_SIDECAR_HOST=127.0.0.1
GMR_SIDECAR_PORT=6091             # 与 blender-mcp 的 6090 并列
GMR_SIDECAR_URL=http://127.0.0.1:6091/

GMR_REQUIRE_SAFE_FORMAT=false     # true 则只允许 safetensors/onnx/npz
GMR_LOG_TAIL_BYTES=4096
GMR_INFER_TIMEOUT_MS=30000
GMR_HEALTH_TIMEOUT_MS=3000
GMR_HTTP_VERBOSE=0                # sidecar 是否记录每条 HTTP 请求
```

---

## 安全须知

**PyTorch checkpoint 走 pickle 反序列化，加载不受信任的文件等同于任意代码执行。** 基于这一点做了三个约束：

1. **`import_model` 拒绝 URL**，只接受本地路径。请先手动下载并核验来源。
2. `registry.js` 的 `SAFE_FORMATS` 只列 `safetensors` / `onnx` / `npz`。导入其它格式会返回明确警告，`GMR_REQUIRE_SAFE_FORMAT=true` 可硬性拦截。
3. **原地登记（`copy=false`）的模型拒绝删除文件。** 那些文件在你自己的目录里，防误删原始资产。

另外：训练与推理都是 `spawn` 数组参数、不用 `shell:true`，避免命令注入。

---

## 三个容易踩的坑

### 1. bpy 非线程安全 —— 违反即随机崩溃

推理在子线程或子进程，但结果**必须经 `bpy.app.timers.register()` marshal 回主线程**才能写 `bpy.data`。直接在后台线程改场景数据会导致随机 segfault，而且极难复现。

### 2. up_axis 弄错会让角色躺平

多数动作模型是 **Y-up**，Blender 是 **Z-up**。`registry.js` 把 `up_axis` 列为骨架契约的一部分，缺失时导入会警告——不是形式主义，是真的会得到一个躺在地上的角色。

### 3. 延迟是"rig"与"批处理"的分水岭

交互式拖拽需要 **~100-150ms**。原生 DDPM 1000 步采样绝无可能达到，必须用 DDIM / LCM 少步采样或蒸馏模型。`sidecar.js` 在单次推理超过 300ms 时会主动返回性能警告。

论文能做成交互式 rig，这一步一定动了刀。

---

## 施工路线

| 阶段 | 内容 | 验收 |
|---|---|---|
| **S0** | 零依赖交互骨架：原生 IK 顶替 ML-Poser、贝塞尔顶替 ML-Betweener | 能拖 Empty、能画 NMC、能双层切换、能 undo。**此时论文 80% 的交互框架已成型，且完全跑在 Blender 内** |
| **S1** | sidecar 命令行跑通 CondMDI | 给几个稀疏 pose → 输出合理 BVH。这步失败就别进 Blender，否则两处 bug 缠在一起没法排 |
| **S2** | 接线 + 攻延迟 | 拖拽到更新压进 ~150ms |
| **S3** | 接慢回路：`gmr.*` API + 并发仲裁锁 | Agent 能布约束、截图看结果、迭代调整 |

**S0 优先的理由**：论文最值钱的部分一行 PyTorch 都不需要。做完 S0 就有了完整交互框架且零外部依赖，之后把插值函数换成模型调用，只是一个函数签名的事。

S3 完成后，能力已经超出论文本身——**论文里没有 Agent 参与创作这一层。**

---

## 一个原架构没有、加了 GMR 才诞生的问题

**并发仲裁。** 用户正在 modal 拖拽手柄时，Agent 从慢回路发来的 `exec` 会撞车。需要一个模式锁，让 Agent 调用返回 busy 而非静默改坏状态。

这在纯 BlenderBridge 时代不存在，因为那时只有一条回路。

---

## 诚实标注

以下尚未实机验证，动手前建议用 BlenderBridge 的 `docs` 域确认：

- Blender 5.2 的 **Action Slots / 分层 action 数据模型**是否可用（记忆中 4.4 引入）。若可用，"生成层 / 传统层"就有原生载体，不必手搓 NLA hack
- `gpu` 模块在 5.x 的接口名（如 `gpu.shader.from_builtin` 的内置 shader 名曾在 4.0 改过）
- sidecar 侧的 CUDA 环境
- CondMDI 与 IBMM 的控制粒度是否等价

`model_config.py` / `train.py` / `sidecar.py` 已通过 `py_compile`，5 个 JS 文件与桥接本体已通过 `node --check`，命令分发经真实插件调用端到端跑通（`gmr_help` / `gmr_status` 均正常返回）。

但**真实训练与真实推理均未验证**——那需要一个实际的模型配置与 PyTorch 环境。已验证的是配置加载器的降级路径与校验逻辑，以及无模型时的贝塞尔兜底。