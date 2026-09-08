# Python 泛型 & 类型安全规范（Claude Code Rule）

核心目标：用 `Generic` + `TypeVar` 替代 `Any`，保证 IDE 和 AI 可推导所有类型。

---

## 1. Any 使用边界

业务层（DTO / Domain / Service）完全禁止 `Any`。

```python
# 禁止
data: Any

# 正确：用具体类型或 TypeVar
data: SceneObject
data: T
```

`dict[str, Any]` 仅允许在边界层使用，且必须立即转为模型，不得流入业务层：

```python
# 允许：第三方 API / Blender socket 原始响应
raw: dict[str, Any] = json.loads(data.decode())
return BlenderResponse.model_validate(raw)  # 出口必须是模型
```

---

## 2. TypeVar 与 Generic 基础

```python
from typing import Generic, TypeVar

T = TypeVar("T")

class Repository(Generic[T]):
    def find(self, id: str) -> T: ...
    def save(self, entity: T) -> None: ...
```

`TypeVar` 命名约定：单字母大写（`T`、`K`、`V`），或描述性名称加 `_T` 后缀（`Item_T`）。

---

## 3. 泛型 Result / Response 包装器

统一返回结构，用泛型约束 `data` 字段，避免 `data: Any` 或 `data: dict`：

```python
from pydantic import BaseModel
from typing import Generic, TypeVar

T = TypeVar("T")

class Result(BaseModel, Generic[T]):
    success: bool
    data: T | None = None
    error: str | None = None

# 使用：data 字段类型完全可推导
def get_scene() -> Result[SceneGetStateResult]: ...
def ping() -> Result[PingResult]: ...
```

禁止退化为非泛型版本：

```python
# 禁止
class Result(BaseModel):
    success: bool
    data: dict       # 丢失类型信息
    error: str | None
```

---

## 4. List / Dict 规范

```python
# 正确
objects: list[SceneObject]
headers: dict[str, str]

# 禁止
objects: list[dict]
objects: list[Any]
headers: dict[Any, Any]
```

已知结构的 `dict` 必须建模；仅键或值类型未知时才用 `dict[str, Any]`，
且只能出现在边界层。

---

## 5. 泛型 DTO / Event

当同一容器结构承载多种 payload 类型时，用 `Generic` 建模，而非退化为 `dict`：

```python
class BlenderEvent(BaseModel, Generic[T]):
    tool: str
    payload: T

# 具体化
SceneEvent = BlenderEvent[SceneCreateResult]
PingEvent = BlenderEvent[PingResult]
```

---

## 6. 禁止行为

- `Any` 出现在 DTO / Domain / Service 任一层
- `list[dict]` 或 `list[Any]`
- `data: dict` 作为已知结构的字段类型
- `json.loads` 结果直接传入业务逻辑（不经 `model_validate`）
- 泛型包装器退化：`Result` 的 `data` 字段声明为 `Any` 或 `dict`
