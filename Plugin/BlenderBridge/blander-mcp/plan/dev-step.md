# 详细开发步骤

> 以 requirements.md 为准，按里程碑逐项列出待实现任务与验收标准。
> 每个任务对应 `src/mcp/blmcp/tools/` 下一对文件：
> `<capability>.py` + `<capability>_toolcode.py`。

---

## M0：基础设施（贯穿全程）

### REQ-00：连通性验证

- [x] 提供 `ping` 类工具，AI 可主动验证 Blender 是否在线
- [x] 返回 Blender 版本号（`bpy.app.version_string`）

**验收**：AI 调用后获得版本字符串；Blender 未启动时得到明确的连接失败错误。

---

### REQ-01：结构化错误信息

- [x] 所有工具的错误返回统一包含四个字段：
  - `error_code`：机器可读错误代码（字符串常量）
  - `message`：人类可读描述
  - `current_state`：当前可用状态快照（如现有对象列表）
  - `hint`：下一步建议，供 AI 自我纠正

**验收**：调用任一工具传入无效参数，返回结构完整的四字段错误对象，
AI 无需人工介入即可根据 `hint` 重试。

---

### REQ-02：场景状态查询

- [x] 查询场景中所有对象（名称、类型、位置）
- [x] 查询帧范围（`frame_start`、`frame_end`）和当前帧（`frame_current`）

**验收**：空场景和有对象的场景均能返回正确结构；帧信息与 Blender UI 一致。

---

## M1：Grease Pencil 矢量动画

### REQ-03：GP 对象与图层管理

- [x] 创建 GP 对象（返回实际名称，处理 `.001` 后缀）
- [x] 在指定 GP 对象上创建图层（指定图层名）
- [x] 删除指定图层
- [x] 查询指定 GP 对象的图层列表

**验收**：
- 创建同名对象两次，第二个名称自动带后缀且不报错
- 查询图层列表返回创建顺序与名称

---

### REQ-04：笔触绘制

- [x] 在指定 GP 对象、指定图层、指定帧上绘制坐标序列笔触（`list[tuple[float, float, float]]`）
- [x] 支持**替换**模式：清空该帧已有笔触后写入
- [x] 支持**追加**模式：在该帧追加新笔触
- [x] 预制形状快速生成：
  - [x] 直线（起点、终点、点数）— `gp_shape_draw shape="line"`
  - [x] 矩形（中心、宽、高）— `gp_shape_draw shape="rect"`
  - [x] 圆（中心、半径、点数）— `gp_shape_draw shape="circle"`

**验收**：
- 替换后该帧只有一条笔触
- 追加后笔触数量叠加
- 预制圆形首尾坐标吻合（闭合）

---

### REQ-05：GP 材质与颜色

- [x] 创建 GP 专用材质，设置描边颜色（RGBA）和填充色（RGBA）
- [x] 将已有材质分配给指定 GP 对象

**验收**：材质颜色在 Blender 材质面板中可见；分配后对象材质槽更新。

---

### REQ-06：图层动画

- [x] 对指定 GP 对象的指定图层透明度（`opacity`）在指定帧插入关键帧
- [x] 读取指定图层已有的透明度关键帧列表（帧号 + 值）

**验收**：
- 插入两个关键帧后，播放区间内透明度渐变
- 读取返回的帧号与插入时一致

---

### REQ-07：渲染输出（M1 范围）

- [x] 渲染**当前帧**为图片，输出到指定路径
- [x] 渲染**帧序列**并合成为视频文件，输出到指定路径
- [x] 支持设置：输出路径、分辨率（宽 × 高）、帧率

**验收**：
- 单帧渲染后文件存在且可打开
- 帧序列渲染后视频文件存在，时长与帧数/帧率吻合
- 分辨率与设置值一致

**M1 整体验收**：AI 能完成「创建 GP 对象 → 绘制形状 → 设置颜色 → 插入动画关键帧 →
渲染为视频」全流程，全程不调用 `execute_blender_code`。

---

## M2：关键帧动画

### REQ-08：基础 3D 对象创建

- [x] 创建常见几何体：立方体、球体、平面、圆柱
- [x] 创建时可指定对象名称和初始位置（`location: tuple[float, float, float]`）

**验收**：创建后对象出现在场景中，名称和位置与参数一致。

---

### REQ-09：变换关键帧

- [x] 对指定对象的位置 / 旋转 / 缩放在指定帧插入关键帧
- [x] 读取指定对象指定属性的 F-Curve 数据（帧号 + 值列表）
- [x] 插入关键帧时可指定插值模式：`BEZIER` / `LINEAR` / `CONSTANT`

**验收**：
- 插入两个 LINEAR 关键帧后，F-Curve 读取返回对应帧号和值
- 插值模式在 Blender Graph Editor 中与设置值一致

---

### REQ-10：摄像机动画

- [x] 对摄像机位置插入关键帧（指定帧、位置坐标）
- [x] 对摄像机目标点插入关键帧（通过 Track-To 约束或 Empty 对象）

**验收**：插入关键帧后播放，摄像机在指定帧运动到正确位置。

**M2 整体验收**：AI 能完成「创建几何体 → 设置位置关键帧 → 设置摄像机关键帧 →
渲染为视频」全流程。

---

## M3：程序动画 & 材质

### REQ-11：修改器应用

- [x] 对指定对象添加修改器（波浪 `WAVE`、细分 `SUBSURF` 等），可设置参数
- [x] 读取指定对象的修改器列表及各修改器参数

**验收**：
- 添加细分修改器后，`get_object_detail_summary` 能看到修改器条目
- 参数读取值与添加时传入值一致

---

### REQ-12：Driver 绑定

- [x] 为指定对象的指定属性绑定 Driver，表达式为数学公式字符串
- [x] 绑定后可读取 Driver 表达式（验证写入成功）

**验收**：绑定 `sin(frame/10)` 到 Z 位置后，播放时对象随帧上下运动。

---

### REQ-13：Geometry Nodes 操作

- [x] 查询指定对象的 Geometry Nodes 节点图结构（节点名称、类型、参数）
- [x] 向指定对象应用预制节点图（波浪变形、噪声置换等）
- [x] 修改指定节点的指定参数值
- [x] 为指定节点参数在指定帧插入关键帧

**验收**：
- 应用预制节点图后查询返回正确节点列表
- 修改参数后读取新值与设置值一致
- 节点参数关键帧在 Graph Editor 中可见

---

### REQ-14：材质摘要查询

- [x] 查询场景中所有材质的名称及基础属性（颜色、类型）
- [x] 查询指定对象当前使用的材质列表

**验收**：新建材质后查询结果中包含该材质；对象更换材质后查询结果更新。

---

### REQ-15：材质赋予

- [x] 将场景中已有材质分配给指定对象（指定材质槽索引）

**验收**：赋予后对象材质槽显示正确材质名称；可覆盖已有槽也可追加新槽。

**M3 整体验收**：AI 能完成「添加修改器 → 绑定 Driver → 应用 Geometry Nodes →
查询并修改材质」全流程，无需 `execute_blender_code`。

---

## M4：资产导入 & 角色动画

### REQ-16：资产导入

- [x] 从外部文件导入对象：FBX、GLTF/GLB、OBJ
- [x] 从另一个 `.blend` 文件通过 Library Link 引入资产（对象、集合）

**验收**：
- 导入后对象出现在场景中，名称与源文件一致
- Library Link 对象在 Outliner 中显示为外部链接状态

---

### REQ-17：Armature 动画

- [x] 将预制 Action 应用到指定 Armature 对象
- [x] 对 IK 目标（Empty 对象）在指定帧插入位置关键帧

**验收**：
- 应用 Action 后播放，骨骼按 Action 运动
- IK 目标关键帧插入后，播放时末端骨骼跟随目标移动

**M4 整体验收**：AI 能完成「导入角色资产 → 应用 Action → 设置 IK 关键帧 →
渲染为视频」全流程。

---

## 非功能需求（贯穿全程验收）

### NFR-01：工具可靠性

- [x] `gp_stroke_draw` REPLACE × 10：每次返回 `stroke_count=1`，无残留
- [x] `gp_stroke_draw` APPEND × 10：笔触数正确累加 1→10，无静默失败
- [x] `gp_shape_draw` circle REPLACE × 10：`point_count` 每次一致，无漂移
- [x] `object_keyframe_insert` 同帧 × 10：无重复关键帧，无静默失败
- [x] `object_keyframe_insert` 不同帧 × 10：F-Curve 累积恰好 10 个关键帧

### NFR-02：错误自愈

- [x] 所有工具错误响应包含四字段（`error_code` / `message` / `current_state` / `hint`）
- [x] `current_state` 非空，包含 AI 自我纠正所需的可用选项列表
- [x] `hint` 为有意义的非空字符串（长度 > 5）
- [x] 修复 6 处 toolcode bug：`asset_import` / `blend_library_link` / `gp_shape_draw` /
      `object_modifier_add` / `object_driver_add` / `object_keyframe_insert`
      的部分 error 路径 `current_state={}` 改为提供有用信息
- [x] `blend_library_link` 参数验证顺序优化：`INVALID_ASSET_TYPE` 先于 `FILE_NOT_FOUND`
- [x] 覆盖所有里程碑工具的代表性错误路径（GP / 动画 / 修改器 / GeoNodes / 资产导入 / 骨架）

### NFR-03：单 Blender 实例

- [x] `connection.py` 新增 `_blender_lock = threading.Lock()`，序列化所有 `send_code` 调用
- [x] 锁忙时立即返回四字段 `BLENDER_BUSY` 错误（不阻塞）
- [x] `finally` 块确保锁在连接异常时也能正确释放
- [x] `mcp_client.py` 升级为 per-request queue 路由，支持并发请求 ID 匹配
- [x] 单元测试（`TestNFR03Unit`）：持锁时返回 BUSY、REQ-01 合规、两线程并发场景、
      ConnectionError 后锁释放、顺序调用时锁可用
