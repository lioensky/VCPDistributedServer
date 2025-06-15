// VCPDistributedServer.js
const dotenv = require('dotenv');
const WebSocket = require('ws');
const path = require('path');
const pluginManager = require('./Plugin.js');

dotenv.config({ path: 'config.env' });

const DEBUG_MODE = (process.env.DebugMode || "False").toLowerCase() === "true";

class DistributedServer {
    constructor() {
        this.mainServerUrl = process.env.Main_Server_URL;
        this.vcpKey = process.env.VCP_Key;
        this.serverName = process.env.ServerName || 'Unnamed-Distributed-Server';
        this.ws = null;
        this.reconnectInterval = 5000; // 初始重连间隔5秒
        this.maxReconnectInterval = 60000; // 最大重连间隔60秒
    }

    async initialize() {
        console.log(`[${this.serverName}] Initializing...`);
        pluginManager.setProjectBasePath(__dirname);
        await pluginManager.loadPlugins();
        this.connect();
    }

    connect() {
        if (!this.mainServerUrl || !this.vcpKey) {
            console.error('[Error] Main_Server_URL or VCP_Key is not defined in config.env. Cannot connect.');
            return;
        }

        const connectionUrl = `${this.mainServerUrl}/vcp-distributed-server/VCP_Key=${this.vcpKey}`;
        console.log(`[${this.serverName}] Attempting to connect to main server at ${this.mainServerUrl}`);

        this.ws = new WebSocket(connectionUrl);

        this.ws.on('open', () => {
            console.log(`[${this.serverName}] Successfully connected to main server.`);
            this.reconnectInterval = 5000; // Reset reconnect interval on successful connection
            this.registerTools();
        });

        this.ws.on('message', (message) => {
            this.handleMainServerMessage(message);
        });

        this.ws.on('close', () => {
            console.log(`[${this.serverName}] Disconnected from main server. Attempting to reconnect in ${this.reconnectInterval / 1000}s...`);
            this.scheduleReconnect();
        });

        this.ws.on('error', (error) => {
            console.error(`[${this.serverName}] WebSocket error:`, error.message);
            // 'close' event will be triggered next, which handles reconnection.
        });
    }

    scheduleReconnect() {
        setTimeout(() => this.connect(), this.reconnectInterval);
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
            if (DEBUG_MODE) console.log(`[${this.serverName}] No local tools found to register.`);
        }
    }

    async handleMainServerMessage(message) {
        try {
            const parsedMessage = JSON.parse(message);
            if (DEBUG_MODE) console.log(`[${this.serverName}] Received message from main server:`, parsedMessage.type);

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

        if (DEBUG_MODE) console.log(`[${this.serverName}] Executing tool '${toolName}' for request ID: ${requestId}`);

        let responsePayload;
        try {
            // Use the new processToolCall method to handle argument formatting
            const result = await pluginManager.processToolCall(toolName, toolArgs);
            
            let parsedResult;
            try {
                // The result from the plugin is expected to be a JSON string.
                parsedResult = JSON.parse(result);
            } catch (e) {
                // If not JSON, wrap it.
                parsedResult = { original_plugin_output: result };
            }

            responsePayload = {
                type: 'tool_result',
                data: {
                    requestId,
                    status: 'success',
                    result: parsedResult
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
        if (DEBUG_MODE) console.log(`[${this.serverName}] Sent result for request ID: ${requestId}`);
    }

    sendMessage(payload) {
        if (this.ws && this.ws.readyState === WebSocket.OPEN) {
            this.ws.send(JSON.stringify(payload));
        } else {
            console.error(`[${this.serverName}] Cannot send message, WebSocket is not open.`);
        }
    }
}

const server = new DistributedServer();
server.initialize();