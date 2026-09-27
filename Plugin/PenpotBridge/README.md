# PenpotBridge 全栈集成指南

> **VCP <-> Penpot 自动化管线**  
> 将 Penpot 本地容器实例、MCP 协议服务端与浏览器前端插件打包进 `PenpotBridge` 生态，实现 Agent 对设计资产的高维感知与程序化操纵。

---

## 目录结构规划（推荐布局）

建议将 `docker` 与 `mcp` 统一归拢在 `PenpotBridge` 下或保持同级依赖：

```text
PenpotBridge/
├── docker/                     # 容器编排层 (Penpot 本体与服务组)
│   ├── mul/                    # 多用户模式 compose 配置
│   └── per/                    # 单人/个人工作区 compose 配置
├── mcp/                        # MCP 协议转接与浏览器插件
│   └── penpot-mcp/
│       ├── common/             # 共享类型与数据契约
│       ├── mcp-server/         # MCP 核心服务器 (Streamable HTTP :4401 / WS :4402)
│       └── penpot-plugin/      # 浏览器前端加载的 Dev 插件 (:4400)
├── PenpotBridge.js             # VCP 原生薄适配层接入入口
├── plugin-manifest.json        # VCP 插件契约描述清单
├── config.env                  # 运行时环境变量配置
└── package.json
```

---

## 第一阶段：启动 Penpot Docker 容器

进入单人工作区配置目录（或 multi 模式），启动容器集群：

```bash
cd docker/per
docker compose up -d
```

### 关键配置陷阱与避坑（必须注意！）
新版 `penpotapp/frontend:latest` 容器内部的 Nginx 监听在 **`8080`** 端口，而非传统的 `80`。  
若出现浏览器 `Connection reset by peer`，请检查 `docker-compose.yml`：

```yaml
penpot-frontend:
  image: penpotapp/frontend:latest
  ports:
    - "9001:8080" # 宿主 9001 必须映射到容器内 8080
  environment:
    - PENPOT_PUBLIC_URI=http://localhost:9001
```

启动完成后，浏览器访问 `http://localhost:9001` 注册或登录设计工作区。

---

## 第二阶段：启动 MCP 服务端与插件 Dev 预览

### 1. 编译并启动 MCP 协议服务端 (mcp-server)
MCP 服务端对外提供 **HTTP (:4401)** 与 **WebSocket (:4402)** 接口：

```bash
cd mcp/penpot-mcp/mcp-server

# 若遇 sharp 安装混源挂死，可用 curl 预先解压官方二进制包并使用 --ignore-scripts
npm run build

# 启动服务端 (建议监听 0.0.0.0 以避免 IPv6 ::1 绑定问题)
PENPOT_MCP_SERVER_LISTEN_ADDRESS=0.0.0.0 npm start
```

### 2. 编译并启动浏览器前端插件服务器 (penpot-plugin)
该服务为 Penpot 提供 Manifest 加载清单：

```bash
cd mcp
git clone https://github.com/penpot/penpot-mcp.git
cd penpot-mcp/penpot-plugin
npm install --ignore-scripts
npm run dev
```
启动成功后，Vite 将在 `http://localhost:4400` 托管插件清单及产物。

---

## 第三阶段：浏览器端挂载插件与全链路握手

1. **进入设计文件**：在浏览器打开 `http://localhost:9001`，新建或打开一个项目设计画板。
2. **加载本地插件**：
   - 点击左下角插件中心（Plugins），或使用快捷键 `Ctrl + Alt + P`。
   - 选择 **Load plugin / Install plugin**。
   - 输入开发清单地址：
     ```text
     http://localhost:4400/manifest.json
     ```
3. **建立连接**：
   - 打开刚加载的 **Penpot MCP Plugin**。
   - 点击面板中的 **"Connect to MCP server"** 按钮。
   - **保持插件窗口处于打开状态**（关闭窗口会导致 WebSocket 4402 断开）。
4. **验证状态**：
   - 终端执行 `ss -tnp | grep 4402` 即可看到 Chromium 与 Node 建立了稳定的 `ESTABLISHED` 双向连接。

---

## 第四阶段：VCP 插件调用与设计资产操纵

PenpotBridge 屏蔽了繁琐的底座通信，Agent 可以通过标准 VCP 指令与画板交互：

### 1. 查看高维 API 与设计指南
<<<[TOOL_REQUEST_EXP]>>>
tool_name:「始exp」PenpotBridge「末exp」,
command:「始exp」overview「末exp」
<<<[END_TOOL_REQUEST_EXP]>>>

### 2. 探测当前画板树结构与页面列表
<<<[TOOL_REQUEST_EXP]>>>
tool_name:「始exp」PenpotBridge「末exp」,
command:「始exp」list_pages「末exp」
<<<[END_TOOL_REQUEST_EXP]>>>

### 3. 创建画板矩形 (Rectangle)
<<<[TOOL_REQUEST_EXP]>>>
tool_name:「始exp」PenpotBridge「末exp」,
command:「始exp」create_rect「末exp」,
x:「始exp」100「末exp」,
y:「始exp」100「末exp」,
width:「始exp」200「末exp」,
height:「始exp」80「末exp」,
name:「始exp」对策按钮「末exp」,
fill:「始exp」#4A90E2「末exp」
<<<[END_TOOL_REQUEST_EXP]>>>

### 4. 逃生舱：执行原生 Penpot Plugin API 脚本
<<<[TOOL_REQUEST_EXP]>>>
tool_name:「始exp」PenpotBridge「末exp」,
command:「始exp」exec「末exp」,
code:「始exp」const b = penpot.createBoard(); b.name = '战斗对策板'; b.resize(400, 300); return { id: b.id };「末exp」
<<<[END_TOOL_REQUEST_EXP]>>>

---

## 架构通信图

```text
[ VCP Core / Agent ]
        │ stdio (JSON-RPC)
        ▼
[ PenpotBridge.js (薄适配层) ]
        │ Streamable HTTP (:4401/mcp)
        ▼
[ mcp-server (Node.js) ]
        │ WebSocket (:4402)
        ▼
[ Penpot MCP Plugin (Chromium) ]
        │ Window PostMessage / Plugin Context
        ▼
[ Penpot Web Workspace (:9001) ] ── Docker 映射 ──> [ Nginx (:8080) / Backend ]
```
