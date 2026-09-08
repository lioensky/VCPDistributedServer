# Blender Animation MCP — 开发参考手册

> 给 Blender 新手看的关键概念、常见陷阱、调试方法。

---

## 一、Addon 安装与开发

### 开发阶段用 symlink，不要每次打 zip

Blender 5.1+ 使用 Extensions 系统，extension id 为 `mcp`，链接名必须与之一致。

**macOS**

```bash
ln -s /path/to/blander-mcp/src/addon/blender_mcp_addon \
  ~/Library/Application\ Support/Blender/5.1/extensions/user_default/mcp
```

**Windows**（管理员 PowerShell）

```powershell
New-Item -ItemType SymbolicLink `
  -Path "$env:APPDATA\Blender Foundation\Blender\5.1\extensions\user_default\mcp" `
  -Target "C:\path\to\blander-mcp\src\addon\blender_mcp_addon"
```

创建链接后重启 Blender，在 **Edit > Preferences > Add-ons** 中搜索并启用 **MCP**。

### Blender Python Console 快速测试

在 Blender → Scripting 标签页 → 底部 Console 中直接运行 bpy 代码：

```python
[o.name for o in bpy.data.objects]                       # 场景对象列表
[l.name for l in bpy.data.objects["MyGP"].data.layers]  # GP 图层列表
```

### Addon 日志查看

从命令行启动 Blender，`print()` 输出到该终端：

```bash
# macOS
/Applications/Blender.app/Contents/MacOS/Blender

# Windows
"C:\Program Files\Blender Foundation\Blender 5.1\blender.exe"
```

---

## 二、进程通信关键知识

### 为什么必须用 bpy.app.timers？

bpy API 不是线程安全的。在 TCP 子线程里直接调用 bpy 会 crash。正确模式：

```
TCP 子线程
    │ 收到指令
    ▼
_command_queue.put(command)   ← 线程安全的 Queue

bpy.app.timers（主线程，每 50ms 触发）
    │ 轮询队列 → 执行 bpy 操作
    ▼
将结果放回响应队列

TCP 子线程
    │ 读取响应
    ▼
发送给 MCP Server
```

### TCP 通信数据格式

Addon 使用 null byte（`\x00`）作为消息分隔符：

```python
# 发送
payload = json.dumps({"code": "..."}).encode() + b"\x00"
socket.sendall(payload)

# 接收（读取直到 null byte）
data = b""
while True:
    chunk = socket.recv(4096)
    data += chunk
    if b"\x00" in data:
        break
result = json.loads(data.rstrip(b"\x00"))
```

### 超时处理

每次 MCP Server 调用 Blender 设 30 秒超时：

```python
socket.settimeout(30)
```

---

## 三、Grease Pencil API 速查（GPv3 / Blender 5.1+）

### 数据层级

```python
gp_obj  = bpy.data.objects["gp_canvas"]   # Object
gp_data = gp_obj.data                      # bpy.types.GreasePencil（GPv3）

# 图层
layer = gp_data.layers.new("outline")      # 创建
layer = gp_data.layers.get("outline")      # 获取（不存在返回 None）
layer.opacity = 0.5                        # 不透明度
layer.hide = True                          # 隐藏

# 帧（GPv3 新 API）
frame = layer.frames.new(1)                # 在第 1 帧创建新帧
frame = layer.get_frame_at(1)             # 获取已有帧
# 注意：frames 集合没有 .get() 方法，用 get_frame_at() 替代

# 绘图（Drawing）—— GPv3 新概念，一帧对应一个 drawing
drawing = frame.drawing                    # bpy.types.GreasePencilDrawing

# 笔触（GPv3 新 API，不再用 frame.strokes.new()）
drawing.add_strokes([3])                   # 添加一个有 3 个点的笔触
# 总点数 / 总笔触数
n_pts    = drawing.attributes.domain_size("POINT")
n_curves = drawing.attributes.domain_size("CURVE")

# 设置点位置（attributes API）
pos_attr = drawing.attributes["position"]
pos_attr.data[0].vector = (0.0, 0.0, 0.0)   # 第 0 个点

# 设置点粗细（radius，对象空间单位）
radius_attr = drawing.attributes["radius"]
radius_attr.data[0].value = 0.01

# 设置笔触材质（CURVE 域）
mat_attr = drawing.attributes["material_index"]
mat_attr.data[0].value = 0    # 第 0 条笔触，材质槽 0

# 删除所有笔触（replace 模式推荐做法：删帧再重建）
layer.frames.remove(frame.frame_number)
frame = layer.frames.new(frame_number)
drawing = frame.drawing
```

### GP 材质

```python
mat = bpy.data.materials.new("my_mat")
bpy.data.materials.create_gpencil_data(mat)
mat.grease_pencil.color      = (0.0, 0.0, 0.0, 1.0)   # 描边色（RGBA，线性）
mat.grease_pencil.fill_color = (1.0, 0.0, 0.0, 1.0)   # 填充色（RGBA，线性）
# 注意：show_fill / show_stroke 在 Blender 5.1 中已废弃（将在 6.0 移除）
# 填充可见性改由 fill_color[3]（alpha）控制，alpha=0 即隐藏填充

gp_obj.data.materials.append(mat)

# 检查对象槽中是否已有该材质（幂等分配）
existing = [s.material for s in gp_obj.material_slots if s.material]
if mat not in existing:
    gp_obj.data.materials.append(mat)
```

### 坐标系

Blender 右手坐标系：X 右、Y 前（屏幕内）、Z 上。
Grease Pencil 2D 动画通常在 XZ 平面作画（Y=0），摄像机从 -Y 方向看。

### 关键帧动画

```python
layer.opacity = 1.0
layer.keyframe_insert(data_path="opacity", frame=1)

layer.opacity = 0.0
layer.keyframe_insert(data_path="opacity", frame=60)
```

---

## 四、MCP Server 开发注意事项

### Tool 描述很重要

AI 完全依赖 `@mcp.tool()` 的 docstring 决定如何调用。

```python
# 好
async def create_gp_layer(object_name: str, layer_name: str = "Layer") -> str:
    """
    在指定的 Grease Pencil 对象上创建新图层。

    Returns the actual layer name created (may differ if name already exists).
    """

# 差
async def create_gp_layer(object_name: str, layer_name: str) -> str:
    """创建图层"""
```

### 错误信息必须对 AI 友好

```python
# 好
{
    "status": "error",
    "message": "GP object 'canvas' not found.",
    "hint": "Call create_gp_object first, or use one of: ['gp_obj1']"
}

# 差
{"error": "KeyError: 'canvas'"}
```

---

## 五、常见问题

### GP 对象创建了但看不见

`stroke.display_mode` 没有设置为 `'3DSPACE'`。

### Blender crash 而不是报错

在非主线程调用了 bpy。所有 bpy 调用必须在 `bpy.app.timers` 回调里。

### MCP Server 调用超时

1. 检查 Blender Addon 是否已启用（TCP Server 是否在监听）
2. 用手动 TCP 脚本绕过 Claude 直接测试 Addon
3. 检查 Blender 主线程是否卡在长时间操作（如渲染）

### GP 颜色显示偏差

Blender 内部使用线性颜色空间，输入值会被当作 linear 处理。
纯黑 `(0,0,0,1)` 和纯白 `(1,1,1,1)` 不受影响，中间色会有偏差。

---

## 六、渲染 API 速查（Blender 5.1）

### 单帧渲染

```python
scene = bpy.context.scene
rd = scene.render

# 临时覆盖分辨率
orig_x, orig_y = rd.resolution_x, rd.resolution_y
rd.resolution_x, rd.resolution_y = 1920, 1080
rd.resolution_percentage = 100   # 确保实际等于指定值

# 设置输出路径（write_still 会在渲染完成后写文件）
orig_filepath = rd.filepath
rd.filepath = "/tmp/frame.png"

# 非交互（后台）模式
bpy.ops.render.render(write_still=True)

# 交互模式（异步，需用 bpy.app.timers 轮询）
bpy.ops.render.render('INVOKE_DEFAULT', write_still=True)

# 恢复
rd.filepath = orig_filepath
rd.resolution_x, rd.resolution_y = orig_x, orig_y
```

### 动画序列 → 视频（Blender 5.1 新 API）

```python
rd = scene.render
image_settings = rd.image_settings

# Blender 5.1+：media_type 属性
image_settings.media_type = 'VIDEO'   # 'IMAGE' / 'MULTI_LAYER_IMAGE' / 'VIDEO'

# ffmpeg 编解码（无论新旧 API 均有效）
rd.ffmpeg.format      = 'MPEG4'
rd.ffmpeg.codec       = 'H264'
rd.ffmpeg.audio_codec = 'NONE'

rd.filepath = "/tmp/output.mp4"
scene.frame_start = 1
scene.frame_end   = 60

bpy.ops.render.render(animation=True)          # 后台模式
# bpy.ops.render.render('INVOKE_DEFAULT', animation=True)  # 交互模式

# 检查渲染是否完成（交互模式轮询）
bpy.app.is_job_running('RENDER')   # True = 仍在渲染
```

### 兼容性写法（同时支持旧版与 5.1）

```python
if hasattr(image_settings, "media_type"):
    image_settings.media_type = 'VIDEO'
else:
    image_settings.file_format = 'FFMPEG'
```

---

## 八、上游代码结构与更新方法

`src/mcp/blmcp/` 的内容来自**三个独立来源**，更新时需要分别处理。

### 来源说明

```
src/mcp/blmcp/
├── __init__.py        ┐
├── tools/             ├─ 来源①：blender_mcp 上游仓库（经本项目适配）
├── tools_helpers/     ┘
└── data/
    ├── api/           ── 来源②：Blender Python API 文档（RST）
    └── manual/        ── 来源③：Blender 用户手册（RST）
```

`data/` 下的文件通过辅助脚本从外部同步，不属于上游仓库的代码。

---

### 本项目与上游的差异

更新前必须了解哪些文件是我们自己加的/改过的，避免被上游覆盖。

**本项目新增（上游不存在，直接保留）：**

| 文件 | 功能 |
|------|------|
| `tools/_template_tool_error.py` | REQ-01 结构化错误模板 |
| `tools/get_scene_state.py / _toolcode.py` | REQ-02 场景状态查询 |
| `tools/gp_object_create.py / _toolcode.py` | REQ-03 GP 对象创建 |
| `tools/gp_layer_create.py / _toolcode.py` | REQ-03 GP 图层创建 |
| `tools/gp_layer_delete.py / _toolcode.py` | REQ-03 GP 图层删除 |
| `tools/gp_layers_list.py / _toolcode.py` | REQ-03 GP 图层列表 |
| `tools/gp_stroke_draw.py / _toolcode.py` | REQ-04 笔触绘制（自由坐标） |
| `tools/gp_shape_draw.py / _toolcode.py` | REQ-04 预制形状（rect/circle） |
| `tools/gp_material_create.py / _toolcode.py` | REQ-05 GP 材质创建 |
| `tools/gp_material_assign.py / _toolcode.py` | REQ-05 GP 材质分配 |
| `tools/gp_layer_opacity_set.py / _toolcode.py` | REQ-06 图层透明度关键帧 |
| `tools/gp_layer_keyframes_list.py / _toolcode.py` | REQ-06 读取透明度关键帧 |
| `tools/render_frame.py / _toolcode.py` | REQ-07 单帧渲染为图片 |
| `tools/render_animation.py / _toolcode.py` | REQ-07 帧序列渲染为视频 |

**本项目改过（需手动 diff 再合并）：**

| 文件 | 改动原因 |
|------|----------|
| `tools/get_object_detail_summary_toolcode.py` | REQ-01 统一错误结构 |
| `tools/jump_to_tab_by_name_toolcode.py` | REQ-01 统一错误结构 |
| `tools/jump_to_tab_by_space_type_toolcode.py` | REQ-01 统一错误结构 |
| `tools/jump_to_view3d_object_by_name_toolcode.py` | REQ-01 统一错误结构 |
| `tools/jump_to_view3d_object_data_by_name_toolcode.py` | REQ-01 统一错误结构 |

---

### 更新来源①：核心代码

上游目录结构与本项目有差异（upstream: `mcp/blmcp/` → 本项目: `src/mcp/blmcp/`）。

```bash
# 1. 克隆上游（--depth 节省时间；已有则 git -C upstream_tmp pull）
git clone --depth=20 https://projects.blender.org/lab/blender_mcp.git upstream_tmp

# 2. 查看上游最近变更，了解改了什么
git -C upstream_tmp log --oneline -15

# 3. 同步"未改动"的文件（可直接覆盖）
cp upstream_tmp/mcp/blmcp/__init__.py           src/mcp/blmcp/
cp upstream_tmp/mcp/blmcp/tools_helpers/*.py    src/mcp/blmcp/tools_helpers/

# 对 tools/ 下上游有、我们未改动的文件逐个覆盖：
# cp upstream_tmp/mcp/blmcp/tools/ping.py       src/mcp/blmcp/tools/
# cp upstream_tmp/mcp/blmcp/tools/ping_toolcode.py  src/mcp/blmcp/tools/
# ...（按需）

# 4. 对"改过"的文件，先 diff 再手动合并
diff upstream_tmp/mcp/blmcp/tools/get_object_detail_summary_toolcode.py \
     src/mcp/blmcp/tools/get_object_detail_summary_toolcode.py

# 5. 修复 import 路径（上游使用 blmcp，本项目相同，通常无需修改）
#    如发现 from src.mcp.blmcp 前缀，批量替换：
#    grep -r "src\.mcp\.blmcp" src/mcp/blmcp/

# 6. 清理临时目录
rm -rf upstream_tmp
```

---

### 更新来源②：API 文档

需要本地 Blender 源码，构建后用脚本同步。

```bash
# 克隆 Blender 源码（体积大，只需一次）
git clone --depth=1 https://projects.blender.org/blender/blender.git blender_src

# 在 Blender 源码目录构建 Python API 文档
cd blender_src
make docs_py
# 产物默认在 doc/python_api/

# 同步到本项目
python src/_misc/update_reference_api.py blender_src/doc/python_api/
```

---

### 更新来源③：用户手册

```bash
git clone --depth=1 https://projects.blender.org/blender/blender-manual.git blender_manual

python src/_misc/update_reference_manual.py blender_manual/
```

---

### 恢复同步脚本

如果 `src/_misc/` 下的脚本丢失，可从 git 历史找回：

```bash
git show 6294711:references/blender_mcp/_misc/update_reference_api.py \
  > src/_misc/update_reference_api.py

git show 6294711:references/blender_mcp/_misc/update_reference_manual.py \
  > src/_misc/update_reference_manual.py
```

---

## 七、版本兼容性（Blender 5.1 基准）

| 组件 | 版本 | 备注 |
|------|------|------|
| Blender | **5.1**（基准） | GPv3 API，Extensions 系统 |
| Python（Blender 内置） | 3.11 | Addon 用此版本，无法更改 |
| Python（MCP Server） | 3.10+ | blmcp 要求 |
| blmcp | 1.0.0 | 官方参考实现 |
| uv | 最新 | 包管理器 |

**已知 Blender 5.1 API 变更：**

| 变更项 | 旧 API（4.x） | 新 API（5.1） |
|--------|--------------|--------------|
| GP 对象类型 | `'GPENCIL'` | `'GREASEPENCIL'` |
| GP 数据创建 | `bpy.data.grease_pencils.new()` | 同上（未变） |
| GP 笔触创建 | `frame.strokes.new()` | `drawing.add_strokes([n])` |
| GP 填充可见 | `mat.grease_pencil.show_fill = True` | alpha > 0（`show_fill` 废弃） |
| 视频渲染格式 | `image_settings.file_format = 'FFMPEG'` | `image_settings.media_type = 'VIDEO'` |

> 升级 Blender 版本时，来源①②③均需同步更新，仅更新核心代码不够。

---

## 九、参考链接

| 资源 | 地址 |
|------|------|
| Blender Python API 文档 | https://docs.blender.org/api/current/ |
| bpy PyPI 包 | https://pypi.org/project/bpy/ |
| Blender MCP Server 页面 | https://www.blender.org/lab/mcp-server/ |
| blender-mcp 源码仓库 | https://projects.blender.org/lab/blender_mcp |
| Blender 用户手册仓库 | https://projects.blender.org/blender/blender-manual |
| Blender 源码仓库 | https://projects.blender.org/blender/blender |