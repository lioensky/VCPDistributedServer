# Pydantic 数据类型规范（Claude Code Rule）

## 目标

统一 MCP Server、Blender 桥接层、JSON 数据处理的类型标准。

核心原则：**Schema is the source of truth. `dict` is forbidden at boundaries.**

---

## 1. 数据分层

```
[External Input]  ← Blender socket / MCP 调用方
→ DTO Layer       ← Pydantic Models（唯一入口）
→ Domain Layer
→ Service Layer
```

规则：
- DTO 必须存在于所有外部边界
- 外部数据禁止直接进入业务层
- `dict` 不可跨层传递

---

## 2. MCP Tool 规范

MCP tool 的参数和返回值必须有明确类型，返回结构用 Pydantic 模型描述：

```python
# 正确
class SceneCreateResult(BaseModel):
    success: bool
    scene_state_delta: SceneStateDelta

async def scene_create(name: str = "Scene", fps: int = 24) -> SceneCreateResult: ...

# 禁止
async def scene_create(data: dict) -> dict: ...
```

---

## 3. JSON / Dict 规范

```python
# 推荐：强类型
class SceneObject(BaseModel):
    name: str
    type: str
    location: list[float]

# 嵌套必须建模
class SceneState(BaseModel):
    objects: list[SceneObject]
    frame_start: int
    frame_end: int
    frame_current: int
```

---

## 4. List 规范

```python
# 禁止
items: list[dict]

# 正确
items: list[SceneObject]
```

---

## 5. Validator 规范

`@field_validator` 只在 DTO 层使用，用于外部数据清洗：

```python
class SceneObject(BaseModel):
    location: list[float]

    @field_validator("location")
    @classmethod
    def check_location(cls, v: list[float]) -> list[float]:
        if len(v) != 3:
            raise ValueError("location must have exactly 3 elements")
        return v
```

---

## 6. 动态数据边界

以下场景允许使用 `dict[str, Any]`，但必须隔离，不得流入业务层：

- Blender socket 原始响应（在 `BlenderClient` 内部解析后立即转为模型）
- 第三方 webhook 原始 payload

```python
# BlenderClient 内部隔离
raw: dict[str, Any] = json.loads(data.decode())
return BlenderResponse.model_validate(raw)  # 出口必须是模型
```

---

## 7. 禁止行为

- `dict` 作为函数参数或返回值（外部边界）
- `list[dict]`
- `Any` 未隔离使用
- `json.loads` 后直接传入业务逻辑
