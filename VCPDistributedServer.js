// VCPDistributedServer.js
const WebSocket = require('ws');
const express = require('express');
const http = require('http');
const path = require('path');
const fs = require('fs').promises;
const fsSync = require('fs');
const dotenv = require('dotenv');
const os = require('os');
const mime = require('mime-types');
const pluginManager = require('./Plugin.js');

// 加载全局配置
dotenv.config({ path: 'config.env' });

const DEBUG_MODE = (process.env.DebugMode || "False").toLowerCase() === "true";

class DistributedServer {
    constructor() {
        this.mainServerUrl = process.env.Main_Server_URL;
        this.vcpKey = process.env.VCP_Key;
        this.serverName = process.env.ServerName || 'Unnamed-Distributed-Server';
        this.port = 0; // 默认0表示随机选择一个可用端口
        this.debugMode = DEBUG_MODE;
        this.ws = null;
        this.app = express(); // 创建 Express 应用
        this.server = http.createServer(this.app); // 创建 HTTP 服务器
        this.reconnectInterval = 5000; // 初始重连间隔5秒
        this.maxReconnectInterval = 60000; // 最大重连间隔60秒
        this.reconnectTimeoutId = null; // 跟踪重连超时
        this.stopped = false; // 防止手动停止后重连
        this.staticPlaceholderUpdateInterval = null; // 静态占位符更新定时器
    }

    async initialize() {
        console.log(`[${this.serverName}] Initializing...`);

        // 加载服务器特定配置
        const serverConfigPath = path.join(__dirname, 'config.env');
        try {
            if (fsSync.existsSync(serverConfigPath)) {
                const serverEnv = dotenv.parse(fsSync.readFileSync(serverConfigPath));
                if (serverEnv.DIST_SERVER_PORT) {
                    const newPort = parseInt(serverEnv.DIST_SERVER_PORT, 10);
                    if (!isNaN(newPort)) {
                        this.port = newPort;
                        console.log(`[${this.serverName}] Port loaded from config.env: ${this.port}`);
                    }
                }
            }
        } catch (e) {
            console.error(`[${this.serverName}] Error reading server config.env:`, e);
        }

        // 设置项目基础路径
        pluginManager.setProjectBasePath(__dirname);
        await pluginManager.loadPlugins();

        // 初始化服务类插件
        await pluginManager.initializeServices(this.app, null, __dirname);

        // 启动 HTTP 服务器
        this.server.listen(this.port, '0.0.0.0', () => {
            this.port = this.server.address().port; // 获取实际监听的端口
            console.log(`[${this.serverName}] HTTP server listening on 0.0.0.0:${this.port}`);
            // 在 HTTP 服务器启动后，再连接到主服务器
            this.connect();
        });
    }

    connect() {
        if (this.stopped) {
            console.log(`[${this.serverName}] Server is stopped, not connecting.`);
            return;
        }
        if (!this.mainServerUrl || !this.vcpKey) {
            console.error(`[${this.serverName}] Error: Main_Server_URL or VCP_Key is not defined in config.env. Cannot connect.`);
            return;
        }

        const connectionUrl = `${this.mainServerUrl.replace(/^http/, 'ws')}/vcp-distributed-server/VCP_Key=${this.vcpKey}`;
        console.log(`[${this.serverName}] Attempting to connect to main server at ${connectionUrl}`);

        this.ws = new WebSocket(connectionUrl);

        this.ws.on('open', async () => {
            console.log(`[${this.serverName}] Successfully connected to main server.`);
            this.reconnectInterval = 5000; // Reset reconnect interval on successful connection
            this.registerTools();
            await this.reportIPAddress();
            
            // 设置静态占位符定期推送
            this.setupStaticPlaceholderUpdates();
        });

        this.ws.on('message', (message) => {
            this.handleMainServerMessage(message);
        });

        this.ws.on('close', () => {
            console.log(`[${this.serverName}] Disconnected from main server.`);
            // 清理静态占位符更新定时器
            this.clearStaticPlaceholderUpdates();
            this.scheduleReconnect();
        });

        this.ws.on('error', (error) => {
            console.error(`[${this.serverName}] WebSocket error:`, error.message);
            // 'close' event will be triggered next, which handles reconnection.
        });
    }

    scheduleReconnect() {
        if (this.stopped) {
            console.log(`[${this.serverName}] Stop called, cancelling reconnection.`);
            return;
        }
        console.log(`[${this.serverName}] Attempting to reconnect in ${this.reconnectInterval / 1000}s...`);
        // 清理静态占位符更新定时器
        this.clearStaticPlaceholderUpdates();
        // Clear any existing timeout to avoid multiple reconnect loops
        if (this.reconnectTimeoutId) {
            clearTimeout(this.reconnectTimeoutId);
        }
        this.reconnectTimeoutId = setTimeout(() => this.connect(), this.reconnectInterval);
        // Exponential backoff
        this.reconnectInterval = Math.min(this.reconnectInterval * 2, this.maxReconnectInterval);
    }

    registerTools() {
        const manifests = pluginManager.getAllPluginManifests();
        if (manifests.length > 0) {
            const payload = {
                type: 'register_tools',
                data: {
                    serverName: this.serverName,
                    tools: manifests
                }
            };
            this.sendMessage(payload);
            console.log(`[${this.serverName}] Sent registration for ${manifests.length} tools to the main server.`);
        } else {
            if (this.debugMode) console.log(`[${this.serverName}] No local tools found to register.`);
        }
    }

    async reportIPAddress() {
        const { default: fetch } = await import('node-fetch');
        const networkInterfaces = os.networkInterfaces();
        const ipv4Addresses = [];
        let publicIp = null;

        for (const interfaceName in networkInterfaces) {
            const interfaces = networkInterfaces[interfaceName];
            for (const iface of interfaces) {
                if (iface.family === 'IPv4' && !iface.internal) {
                    ipv4Addresses.push(iface.address);
                }
            }
        }

        try {
            const response = await fetch('https://api.ipify.org?format=json');
            if (response.ok) {
                const data = await response.json();
                publicIp = data.ip;
            } else {
                console.error(`[${this.serverName}] Failed to fetch public IP, status: ${response.status}`);
            }
        } catch (e) {
            console.error(`[${this.serverName}] Could not fetch public IP:`, e.message);
        }
        
        const payload = {
            type: 'report_ip',
            data: {
                serverName: this.serverName,
                localIPs: ipv4Addresses,
                publicIP: publicIp,
                httpPort: this.port
            }
        };
        this.sendMessage(payload);
        console.log(`[${this.serverName}] Reported IP addresses to main server: Local: ${ipv4Addresses.join(', ')}, Public: ${publicIp || 'N/A'}, HTTP Port: ${this.port}`);
    }

    // 设置静态占位符定期更新
    setupStaticPlaceholderUpdates() {
        // 每30秒推送一次静态占位符值
        this.staticPlaceholderUpdateInterval = setInterval(() => {
            this.pushStaticPlaceholderValues();
        }, 30000); // 30秒
        
        // 立即推送一次（延迟2秒等待静态插件初始加载）
        setTimeout(() => {
            this.pushStaticPlaceholderValues();
        }, 2000);
        
        if (this.debugMode) console.log(`[${this.serverName}] Static placeholder updates scheduled every 30 seconds.`);
    }

    // 清理静态占位符更新定时器
    clearStaticPlaceholderUpdates() {
        if (this.staticPlaceholderUpdateInterval) {
            clearInterval(this.staticPlaceholderUpdateInterval);
            this.staticPlaceholderUpdateInterval = null;
            if (this.debugMode) console.log(`[${this.serverName}] Static placeholder update interval cleared.`);
        }
    }

    // 推送静态占位符值到主服务器
    pushStaticPlaceholderValues() {
        const placeholderValues = pluginManager.getAllPlaceholderValues();
        if (placeholderValues.size === 0) {
            return;
        }

        const payload = {
            type: 'update_static_placeholders',
            data: {
                serverName: this.serverName,
                placeholders: Object.fromEntries(placeholderValues)
            }
        };
        
        this.sendMessage(payload);
        if (this.debugMode) {
            console.log(`[${this.serverName}] Pushed ${placeholderValues.size} static placeholder values to main server.`);
            for (const [key, value] of placeholderValues) {
                console.log(`  - ${key}: ${value.substring(0, 100)}${value.length > 100 ? '...' : ''}`);
            }
        }
    }

    async handleMainServerMessage(message) {
        try {
            const parsedMessage = JSON.parse(message);
            if (this.debugMode) console.log(`[${this.serverName}] Received message from main server:`, parsedMessage.type);

            if (parsedMessage.type === 'execute_tool') {
                await this.handleToolExecutionRequest(parsedMessage.data);
            }
        } catch (e) {
            console.error(`[${this.serverName}] Error parsing message from main server:`, e);
        }
    }

    async handleToolExecutionRequest(data) {
        const { requestId, toolName, toolArgs } = data;
        if (!requestId || !toolName) {
            console.error(`[${this.serverName}] Invalid tool execution request received.`);
            return;
        }

        if (this.debugMode) console.log(`[${this.serverName}] Executing tool '${toolName}' for request ID: ${requestId}`);

        let responsePayload;
        try {
            // --- 处理内部文件请求 ---
            if (toolName === 'internal_request_file') {
                const { fileUrl } = toolArgs;
                if (!fileUrl || !fileUrl.startsWith('file://')) {
                    throw new Error(`Invalid or missing fileUrl parameter for internal_request_file.`);
                }

                try {
                    const { fileURLToPath } = require('url');
                    const filePath = fileURLToPath(fileUrl);

                    const fileBuffer = await fs.readFile(filePath);
                    const mimeType = mime.lookup(filePath) || 'application/octet-stream';
                    
                    responsePayload = {
                        type: 'tool_result',
                        data: {
                            requestId,
                            status: 'success',
                            result: {
                                status: 'success',
                                fileData: fileBuffer.toString('base64'),
                                mimeType: mimeType
                            }
                        }
                    };
                } catch (e) {
                    if (e.code === 'ENOENT') {
                        throw new Error(`File not found on distributed server: ${fileUrl}`);
                    } else if (e.code === 'ERR_INVALID_FILE_URL_PATH') {
                        throw new Error(`Invalid file URL path on distributed server: ${fileUrl}`);
                    } else {
                        throw new Error(`Error reading file on distributed server (${fileUrl}): ${e.message}`);
                    }
                }
                this.sendMessage(responsePayload);
                if (this.debugMode) console.log(`[${this.serverName}] Sent file content for request ID: ${requestId}`);
                return; // 处理完毕，直接返回
            }
            // --- 结束：处理内部文件请求 ---

            const result = await pluginManager.processToolCall(toolName, toolArgs);
            let finalResult;

            // --- 默认处理所有插件 ---
            if (typeof result === 'object' && result !== null) {
                // Result is already an object from a direct call (e.g., hybrid service)
                finalResult = result;
            } else {
                // Result is a string from stdio, needs parsing
                try {
                    // --- Robust JSON Parsing ---
                    // The plugin might output debug info (like from dotenv) to stdout before the JSON.
                    // We need to find the actual JSON string.
                    const jsonStartIndex = result.indexOf('{');
                    const jsonEndIndex = result.lastIndexOf('}');
                    
                    if (jsonStartIndex === -1 || jsonEndIndex === -1) {
                        // If no JSON object is found, treat it as a raw string.
                        throw new SyntaxError("No JSON object found in plugin output.");
                    }

                    const jsonString = result.substring(jsonStartIndex, jsonEndIndex + 1);
                    const parsedPluginResult = JSON.parse(jsonString);
                    // --- End of Robust JSON Parsing ---

                    if (parsedPluginResult.status === 'success') {
                        finalResult = parsedPluginResult.result;
                        // --- VCP Protocol Enhancement ---
                        // If the plugin response has special action fields,
                        // merge them into the final result object so they can be handled downstream.
                        if (parsedPluginResult._specialAction) {
                            if (typeof finalResult !== 'object' || finalResult === null) {
                                finalResult = {}; // Ensure finalResult is an object
                            }
                            finalResult._specialAction = parsedPluginResult._specialAction;
                            finalResult.payload = parsedPluginResult.payload;
                        }
                    } else {
                        throw new Error(parsedPluginResult.error || 'Plugin reported an error without a message.');
                    }
                } catch (e) {
                    if (e instanceof SyntaxError) {
                        finalResult = result; // Legacy plugin returning a raw string
                    } else {
                        throw e; // Other error
                    }
                }
            }

            responsePayload = {
                type: 'tool_result',
                data: {
                    requestId,
                    status: 'success',
                    result: finalResult
                }
            };
        } catch (error) {
            console.error(`[${this.serverName}] Error executing tool '${toolName}':`, error.message);
            responsePayload = {
                type: 'tool_result',
                data: {
                    requestId,
                    status: 'error',
                    error: error.message || 'An unknown error occurred.'
                }
            };
        }

        this.sendMessage(responsePayload);
        if (this.debugMode) console.log(`[${this.serverName}] Sent result for request ID: ${requestId}`);
    }

    sendMessage(payload) {
        if (this.ws && this.ws.readyState === WebSocket.OPEN) {
            this.ws.send(JSON.stringify(payload));
        } else {
            console.error(`[${this.serverName}] Cannot send message, WebSocket is not open.`);
        }
    }

    async stop() {
        console.log(`[${this.serverName}] Stopping server...`);
        this.stopped = true;
        
        // 清理静态占位符更新定时器
        this.clearStaticPlaceholderUpdates();
        
        if (this.reconnectTimeoutId) {
            clearTimeout(this.reconnectTimeoutId);
            this.reconnectTimeoutId = null;
        }
        
        // 关闭插件管理器
        pluginManager.shutdownAllPlugins().catch(err => {
            console.error(`[${this.serverName}] Error during plugin shutdown:`, err);
        });
        
        if (this.ws) {
            // Remove listeners to prevent reconnection logic from firing on manual close
            this.ws.removeAllListeners('close');
            this.ws.removeAllListeners('error');
            if (this.ws.readyState === WebSocket.OPEN) {
                this.ws.close(1000, 'Client initiated disconnect');
            }
            this.ws = null;
        }

        // 关闭 HTTP 服务器
        if (this.server) {
            this.server.close(() => {
                console.log(`[${this.serverName}] HTTP server closed.`);
            });
        }

        console.log(`[${this.serverName}] Server stopped.`);
    }
}

// 独立启动
const server = new DistributedServer();
server.initialize();

// 优雅关闭
process.on('SIGINT', async () => {
    console.log('\n[DistributedServer] Received SIGINT, shutting down gracefully...');
    await server.stop();
    process.exit(0);
});

process.on('SIGTERM', async () => {
    console.log('\n[DistributedServer] Received SIGTERM, shutting down gracefully...');
    await server.stop();
    process.exit(0);
});