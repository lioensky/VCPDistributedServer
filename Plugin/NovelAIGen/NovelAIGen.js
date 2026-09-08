#!/usr/bin/env node
/*
 * NovelAIGen
 * 版本: 2.1.0
 * 职责: NovelAI 六端点多渠道、全参数网关。
 * 作者: VCP-Assistant
 * 重构: CodeCC & infinite-vector
 */
import axios from "axios";
import fs from "fs/promises";
import path from "path";
import crypto from "crypto";
import { v4 as uuidv4 } from "uuid";
import yauzl from "yauzl";
import { HttpsProxyAgent } from "https-proxy-agent";
import { HttpProxyAgent } from "http-proxy-agent";

// ==================== 段 01 · 文件头 + import + 环境变量 ====================
const env = process.env;
const NOVELAI_API_KEY = env.NOVELAI_API_KEY || "";
const NOVELAI_BASE_URL = env.NOVELAI_BASE_URL || "https://image.novelai.net";
const NOVELAI_ACCOUNT_URL =
  env.NOVELAI_ACCOUNT_URL || "https://api.novelai.net";
const MULTI_CHANNEL =
  String(env.MULTI_CHANNEL || "false").toLowerCase() === "true";
const NOVELAI_CHANNELS = env.NOVELAI_CHANNELS || "";
const NOVELAI_PATH_PREFIX = (env.NOVELAI_PATH_PREFIX || "").replace(/\/$/, "");
const VIBE_UNSUPPORTED_PREFIXES =
  env.VIBE_UNSUPPORTED_PREFIXES !== undefined
    ? env.VIBE_UNSUPPORTED_PREFIXES
    : "";
const MODEL_ALIASES = env.MODEL_ALIASES || "";
const INPAINT_MODELS = env.INPAINT_MODELS || "";
const INPAINT_FALLBACK_CHAIN = env.INPAINT_FALLBACK_CHAIN || "";
const DEFAULT_MODEL = env.DEFAULT_MODEL || "v4.5";
const DEFAULT_STEPS = Number(env.DEFAULT_STEPS || 23);
const DEFAULT_SCALE = Number(env.DEFAULT_SCALE || 5);
const DEFAULT_SAMPLER = env.DEFAULT_SAMPLER || "k_euler_ancestral";
const DEFAULT_NOISE_SCHEDULE = env.DEFAULT_NOISE_SCHEDULE || "karras";
const DEFAULT_UC =
  env.DEFAULT_UC ||
  "lowres, artistic error, film grain, scan artifacts, worst quality, bad quality, jpeg artifacts, very displeasing, chromatic aberration, dithering, halftone, screentone, multiple views, logo, too many watermarks, negative space, blank page";
const RESOLUTION_PRESETS = env.RESOLUTION_PRESETS || "";
const MAX_RETRIES = Number(env.MAX_RETRIES || 2);
const RETRY_BASE_DELAY_MS = Number(env.RETRY_BASE_DELAY_MS || 2000);
const MAX_IMAGE_SIZE_MB = Number(env.MAX_IMAGE_SIZE_MB || 8);
const ENUM_PROBE = String(env.ENUM_PROBE || "true").toLowerCase() === "true";
const NOVELAI_PROXY = env.NovelAIProxy || "";
const DEBUG_MODE = String(env.DebugMode || "false").toLowerCase() === "true";
const PROJECT_BASE_PATH = env.PROJECT_BASE_PATH || "";
const SERVER_PORT = env.SERVER_PORT || "";
const IMAGESERVER_IMAGE_KEY = env.IMAGESERVER_IMAGE_KEY || "";
const VAR_HTTP_URL = env.VarHttpUrl || "";
const VAR_HTTPS_URL = env.VarHttpsUrl || "";

// ==================== 段 02 · 常量表与枚举候选池 ====================
const ENDPOINTS = Object.freeze({
  GENERATE: "/ai/generate-image",
  ENCODE_VIBE: "/ai/encode-vibe",
  AUGMENT: "/ai/augment-image",
  UPSCALE: "/ai/upscale",
  SUGGEST_TAGS: "/ai/generate-image/suggest-tags",
  SUBSCRIPTION: "/user/subscription",
});
const ACTION = Object.freeze({
  GENERATE: "generate",
  IMG2IMG: "img2img",
  INFILL: "infill",
});
// V5 标识符来源：YesNovelAI (nai.rinko.ai) GET /v1/models 实证，2026-08-29。
// 官方直连是否接受同一组 ID 尚未验证；若官方拒绝，用 MODEL_ALIASES 覆盖。
const BUILTIN_MODEL_ALIASES = {
  v5: "nai-diffusion-5-full",
  v5c: "nai-diffusion-5-curated",
  "v4.5": "nai-diffusion-4-5-full",
  "v4.5c": "nai-diffusion-4-5-curated",
  v4: "nai-diffusion-4-full",
  v4c: "nai-diffusion-4-curated",
  v3: "nai-diffusion-3",
  // furry 有两种写法：前者来自 novelai-python SDK 枚举，后者来自中转站
  // /v1/models。两者可能分别对应不同渠道，都保留。
  furry: "nai-diffusion-furry-3",
  furry3: "nai-diffusion-3-furry",
};

// 注：nai-diffusion-4-5-full-inpainting 与 nai-diffusion-5-*-inpainting
// 仅在部分中转站的 /v1/models 中出现，官方直连是否提供未经验证。
// 为避免官方用户从"降级可用"退化为"直接报错"，此处不内置 4-5-full 的映射；
// 需要时通过 INPAINT_MODELS 配置项添加，例如：
//   INPAINT_MODELS=nai-diffusion-4-5-full=nai-diffusion-4-5-full-inpainting
const BUILTIN_INPAINT_MODELS = {
  "nai-diffusion-4-5-curated": "nai-diffusion-4-5-curated-inpainting",
  "nai-diffusion-4-full": "nai-diffusion-4-full-inpainting",
  "nai-diffusion-4-curated": "nai-diffusion-4-curated-inpainting",
  "nai-diffusion-3": "nai-diffusion-3-inpainting",
  "nai-diffusion-3-furry": "nai-diffusion-3-furry-inpainting",
  "nai-diffusion-furry-3": "nai-diffusion-furry-3-inpainting",
};

const BUILTIN_INPAINT_FALLBACK = [
  ["nai-diffusion-4-5-curated", "nai-diffusion-4-5-curated-inpainting"],
  ["nai-diffusion-4-full", "nai-diffusion-4-full-inpainting"],
  ["nai-diffusion-4-curated", "nai-diffusion-4-curated-inpainting"],
  ["nai-diffusion-3", "nai-diffusion-3-inpainting"],
];
// 站点/官方共用的 HTTP 语义提示，用于把裸状态码翻译成可读原因
const STATUS_HINTS = Object.freeze({
  400: "参数错误 / 模型不支持 / 尺寸不合法",
  401: "Token 无效、过期或已禁用",
  402: "余额不足（Gems / Anlas）",
  403: "该 Token 无此模型权限",
  405: "此路径不接受该方法；若为中转站请检查 PATH_PREFIX 配置",
  413: "请求体或图片超出大小限制",
  429: "限速或额度限制",
  502: "上游响应无效或 Key 不可用",
  503: "上游排队超时或不可用",
  504: "网关超时（上游或前置 CDN 未在限时内响应）",
});
const DEFAULT_RESOLUTIONS = [
  "512x768",
  "768x512",
  "640x640",
  "832x1216",
  "1216x832",
  "1024x1024",
  "1024x1536",
  "1536x1024",
  "1472x1472",
  "1088x1920",
  "1920x1088",
];
const AUGMENT_REQ_TYPES = [
  "emotion",
  "colorize",
  "lineart",
  "sketch",
  "declutter",
  "bg-removal",
];
const ENUM_CANDIDATES = {
  action_infill: ["infill", "inpainting", "infill_v2"],
  augment_bgremoval: ["bg-removal", "bg_removal", "removebg"],
};
const BASE_PARAMETERS = {
  n_samples: 1,
  ucPreset: 0,
  qualityToggle: true,
  params_version: 3,
  prefer_brownian: true,
  add_original_image: false,
  autoSmea: false,
  cfg_rescale: 0,
  controlnet_strength: 1,
  deliberate_euler_ancestral_bug: false,
  dynamic_thresholding: false,
  legacy: false,
  legacy_uc: false,
  legacy_v3_extend: false,
  normalize_reference_strength_multiple: true,
  skip_cfg_above_sigma: null,
  use_coords: false,
};

// ==================== 段 03 · 基础工具函数 ====================
function log(...args) {
  if (DEBUG_MODE) console.error("[NovelAIGen]", ...args);
}
function redact(value, key = "") {
  if (value === null || value === undefined) return value;
  if (/token|key|authorization/i.test(key)) return "<redacted>";
  if (typeof value === "string") {
    const compact = value.replace(/\s/g, "");
    if (value.length > 200 && /^[A-Za-z0-9+/=_-]+$/.test(compact))
      return `<base64:${value.length}>`;
    return value;
  }
  if (Array.isArray(value)) return value.map((item) => redact(item));
  if (typeof value === "object")
    return Object.fromEntries(
      Object.entries(value).map(([k, v]) => [k, redact(v, k)]),
    );
  return value;
}
function parseKvList(str, sep1 = ";", sep2 = "=") {
  const out = {};
  if (!str) return out;
  for (const group of String(str).split(sep1)) {
    const i = group.indexOf(sep2);
    if (i < 0) continue;
    const k = group.slice(0, i).trim();
    const v = group.slice(i + sep2.length).trim();
    if (k) out[k] = v;
  }
  return out;
}
function toPosixRelative(...segments) {
  return segments.join("/").split("\\").join("/");
}
function assertPathInside(baseDir, targetPath) {
  const base = path.resolve(baseDir);
  const target = path.resolve(targetPath);
  if (target !== base && !target.startsWith(`${base}${path.sep}`))
    throw new Error("目标路径越出允许目录");
  return target;
}
function stripDataUriPrefix(input) {
  return String(input || "").replace(/^data:[^;,]+;base64,/i, "");
}
function guessMimeFromBuffer(buffer) {
  if (
    buffer
      ?.subarray(0, 8)
      .equals(Buffer.from([137, 80, 78, 71, 13, 10, 26, 10]))
  )
    return "image/png";
  if (buffer?.subarray(0, 3).equals(Buffer.from([255, 216, 255])))
    return "image/jpeg";
  if (
    buffer?.subarray(0, 4).toString() === "RIFF" &&
    buffer.subarray(8, 12).toString() === "WEBP"
  )
    return "image/webp";
  if (buffer?.subarray(0, 3).toString() === "GIF") return "image/gif";
  return "image/png";
}
function clampNumber(value, min, max, fallback) {
  const n = Number(value);
  return Number.isFinite(n) ? Math.min(max, Math.max(min, n)) : fallback;
}
function sleep(ms) {
  return new Promise((resolve) => setTimeout(resolve, ms));
}
function parseResolution(value) {
  const allowed = RESOLUTION_PRESETS
    ? RESOLUTION_PRESETS.split(",")
        .map((x) => x.trim())
        .filter(Boolean)
    : DEFAULT_RESOLUTIONS;
  const resolution = value || allowed[0];
  if (!/^\d+x\d+$/i.test(resolution) || !allowed.includes(resolution))
    throw new Error(
      `不支持的分辨率 ${resolution}，可选：${allowed.join(", ")}`,
    );
  const [width, height] = resolution.toLowerCase().split("x").map(Number);
  return { width, height, resolution };
}
function parseFreeSize(value, fallbackWidth = 1024, fallbackHeight = 1024) {
  const m = /^(\d+)x(\d+)$/i.exec(String(value || "").trim());
  if (m) return { width: Number(m[1]), height: Number(m[2]) };
  return { width: fallbackWidth, height: fallbackHeight };
}
function asJson(value, fallback = null) {
  try {
    return typeof value === "string" ? JSON.parse(value) : value;
  } catch {
    return fallback;
  }
}
function truncate(value, n = 500) {
  const s = String(value ?? "");
  return s.length > n ? `${s.slice(0, n)}...` : s;
}
function describeResponseError(error) {
  const status = error?.response?.status;
  const hint = STATUS_HINTS[status] ? ` [${STATUS_HINTS[status]}]` : "";
  const head = status ? `HTTP ${status}${hint} ` : "";
  const data = error?.response?.data;
  if (data === undefined || data === null)
    return head + (error?.message || String(error));
  try {
    if (Buffer.isBuffer(data)) return head + truncate(data.toString("utf8"), 300);
    if (data instanceof ArrayBuffer)
      return head + truncate(Buffer.from(data).toString("utf8"), 300);
    if (typeof data === "string") return head + truncate(data, 300);
    return head + truncate(JSON.stringify(data), 300);
  } catch {
    return head + (error?.message || "无法解析的错误响应");
  }
}

// ==================== 段 04 · 渠道层 ====================
// 渠道语法：URL|KEY|MODELS|CAPS|PATH_PREFIX
// PATH_PREFIX 用于中转站的原生协议前缀，例如 YesNovelAI 的 /native。
// 留空即官方直连行为，完全向后兼容。
function parseChannels() {
  const channels = [];
  if (MULTI_CHANNEL && NOVELAI_CHANNELS) {
    for (const item of NOVELAI_CHANNELS.split(";")) {
      const [url, key, models = "", caps = "", prefix = ""] = item.split("|");
      if (!url || !key) continue;
      channels.push({
        url: url.replace(/\/$/, ""),
        key,
        models: models
          ? models
              .split(",")
              .map((x) => x.trim())
              .filter(Boolean)
          : [],
        caps: caps
          ? caps
              .split(",")
              .map((x) => x.trim())
              .filter(Boolean)
          : [],
        prefix: prefix.trim().replace(/\/$/, ""),
      });
    }
  }
  if (!channels.length && NOVELAI_API_KEY)
    channels.push({
      url: NOVELAI_BASE_URL.replace(/\/$/, ""),
      key: NOVELAI_API_KEY,
      models: [],
      caps: [],
      prefix: NOVELAI_PATH_PREFIX,
    });
  console.error(
    `[NovelAIGen] channels=${channels.length} ${channels
      .map((c) => c.url + (c.prefix || ""))
      .join(", ")}`,
  );
  return channels;
}
const CHANNELS = parseChannels();
function channelSupports(channel, capability) {
  return !channel.caps.length || channel.caps.includes(capability);
}
function buildChannelPlan(capability, requestedModel) {
  const plan = [];
  for (const channel of CHANNELS) {
    if (!channelSupports(channel, capability)) continue;
    let models;
    if (!channel.models.length) {
      models = [requestedModel];
    } else if (!requestedModel) {
      models = channel.models;
    } else {
      const matched = channel.models.filter(
        (m) => m === requestedModel || resolveAlias(m) === requestedModel,
      );
      models = matched.length ? matched : [];
    }
    for (const model of models)
      plan.push({
        url: channel.url,
        key: channel.key,
        model,
        prefix: channel.prefix || "",
      });
  }
  for (let i = plan.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [plan[i], plan[j]] = [plan[j], plan[i]];
  }
  return plan;
}

// ==================== 段 05 · 模型解析层 ====================
function mergedAliases() {
  return { ...BUILTIN_MODEL_ALIASES, ...parseKvList(MODEL_ALIASES) };
}
function resolveAlias(value) {
  const aliases = mergedAliases();
  return Object.prototype.hasOwnProperty.call(aliases, value)
    ? aliases[value]
    : value;
}
function inpaintMap() {
  return { ...BUILTIN_INPAINT_MODELS, ...parseKvList(INPAINT_MODELS) };
}
function fallbackChain() {
  if (!INPAINT_FALLBACK_CHAIN) return BUILTIN_INPAINT_FALLBACK;
  return INPAINT_FALLBACK_CHAIN.split(";")
    .map((x) => x.split(">").map((y) => y.trim()))
    .filter((x) => x.length === 2);
}
function resolveModel(input, purpose = "base") {
  const requested = input || DEFAULT_MODEL;
  const aliases = mergedAliases();
  let model;
  if (/^(nai-|safe-)/i.test(requested)) model = requested;
  else if (Object.prototype.hasOwnProperty.call(aliases, requested)) {
    if (aliases[requested] === null || aliases[requested] === "")
      throw new Error(
        `模型别名 ${requested} 的标识符尚未确认，请在 MODEL_ALIASES 中配置，或直接传入原始标识符`,
      );
    model = aliases[requested];
  } else
    throw new Error(
      `未知模型别名 ${requested}，可用别名：${Object.keys(aliases).join(", ")}`,
    );
  if (purpose === "base") return { model, note: null };
  const mapped = inpaintMap()[model];
  if (mapped) return { model: mapped, note: null };
  for (const [base, variant] of fallbackChain()) {
    const available = CHANNELS.some(
      (channel) => !channel.models.length || channel.models.includes(variant),
    );
    if (base && variant && available)
      return {
        model: variant,
        note: `模型 ${model} 无对应 inpainting 变体，已降级为 ${variant}`,
      };
  }
  throw new Error(
    `模型 ${model} 无可用 inpainting 变体，可用模型：${Object.values(inpaintMap()).join(", ")}`,
  );
}
// 本地拦截名单改为配置驱动。默认空串表示不拦截——让上游用自己的错误码说话。
// 若确认某系模型不支持 Vibe，填入 VIBE_UNSUPPORTED_PREFIXES（逗号分隔前缀）。
function assertVibeSupported(model) {
  const prefixes = String(VIBE_UNSUPPORTED_PREFIXES)
    .split(",")
    .map((x) => x.trim())
    .filter(Boolean);
  if (!prefixes.length) return;
  if (prefixes.some((prefix) => model.startsWith(prefix)))
    throw new Error(
      `模型 ${model} 命中本地拦截名单 VIBE_UNSUPPORTED_PREFIXES（当前值：${VIBE_UNSUPPORTED_PREFIXES}）。若该渠道已支持 Vibe Transfer，请调整该配置项。`,
    );
}

function listAvailableModels() {
  return { aliases: mergedAliases(), inpainting: inpaintMap() };
}

// ==================== 段 06 · 输入管道层 ====================
function parseImageArrayInput(value) {
  if (Array.isArray(value)) return value.filter(Boolean);
  if (typeof value === "string" && value.trim().startsWith("[")) {
    const parsed = asJson(value, null);
    if (Array.isArray(parsed)) return parsed.filter(Boolean);
  }
  return value ? [value] : [];
}
function collectImageInputs(args) {
  const values = [];
  const add = (value) => values.push(...parseImageArrayInput(value));
  for (const key of [
    "image",
    "Image",
    "image_url",
    "source_image",
    "image_base64",
  ])
    if (args[key]) add(args[key]);
  const numbered = Object.keys(args)
    .filter((k) => /^(image|image_url|image_base64)_\d+$/i.test(k))
    .sort((a, b) => {
      const na = Number(a.match(/\d+$/)?.[0] ?? 0);
      const nb = Number(b.match(/\d+$/)?.[0] ?? 0);
      return na - nb || a.localeCompare(b);
    });
  for (const key of numbered) add(args[key]);
  return [...new Set(values.map(String))];
}
function checkImageSize(buffer) {
  const mb = buffer.length / 1024 / 1024;
  if (mb > MAX_IMAGE_SIZE_MB)
    throw new Error(
      `图片大小 ${mb.toFixed(2)}MB 超过上限 ${MAX_IMAGE_SIZE_MB}MB`,
    );
}
async function processImageInput(input) {
  if (/^data:/i.test(input)) {
    const raw = Buffer.from(stripDataUriPrefix(input), "base64");
    checkImageSize(raw);
    return input;
  }
  let buffer, mime;
  if (/^https?:\/\//i.test(input)) {
    const response = await axios.get(input, {
      responseType: "arraybuffer",
      timeout: 30000,
      ...buildAgents(),
    });
    buffer = Buffer.from(response.data);
    mime =
      response.headers["content-type"]?.split(";")[0] ||
      guessMimeFromBuffer(buffer);
  } else {
    const local = path.isAbsolute(input)
      ? input
      : path.resolve(PROJECT_BASE_PATH, input);
    buffer = await fs.readFile(local);
    mime =
      {
        ".jpg": "image/jpeg",
        ".jpeg": "image/jpeg",
        ".webp": "image/webp",
        ".gif": "image/gif",
      }[path.extname(local).toLowerCase()] || "image/png";
  }
  checkImageSize(buffer);
  return `data:${mime};base64,${buffer.toString("base64")}`;
}
function toNaiImageField(dataUri) {
  return stripDataUriPrefix(dataUri);
}
function parseCharacterPrompts(args) {
  let list = asJson(args.characters, null);
  if (!Array.isArray(list)) {
    list = [];
    const nums = [
      ...new Set(
        Object.keys(args)
          .map((k) => k.match(/^char_(\d+)(?:_|$)/)?.[1])
          .filter(Boolean),
      ),
    ].sort((a, b) => Number(a) - Number(b));
    for (const n of nums)
      list.push({
        prompt: args[`char_${n}`] || args[`char_${n}_prompt`] || "",
        uc: args[`char_${n}_uc`],
        x: args[`char_${n}_x`],
        y: args[`char_${n}_y`],
      });
  }
  return list
    .filter((x) => x && x.prompt !== undefined)
    .map((x) => ({
      char_caption: String(x.prompt || ""),
      char_uc: String(x.uc || ""),
      centers: (Array.isArray(x.centers)
        ? x.centers
        : [{ x: x.x, y: x.y }]
      ).map((p) => ({
        x: clampNumber(p.x, 0, 1, 0.5),
        y: clampNumber(p.y, 0, 1, 0.5),
      })),
    }));
}

// ==================== 段 07 · Payload 构造层 ====================
function buildBaseParameters(args) {
  const { width, height } = parseResolution(
    args.resolution || args.size || args.image_size,
  );
  return {
    ...BASE_PARAMETERS,
    width,
    height,
    steps: clampNumber(args.steps, 1, 50, DEFAULT_STEPS),
    scale: clampNumber(args.scale, 0, 20, DEFAULT_SCALE),
    sampler: args.sampler || DEFAULT_SAMPLER,
    noise_schedule: args.noise_schedule || DEFAULT_NOISE_SCHEDULE,
    seed: Number.isFinite(Number(args.seed))
      ? Number(args.seed)
      : Math.floor(Math.random() * 4294967296),
    n_samples: clampNumber(args.n_samples, 1, 4, 1),
    cfg_rescale: clampNumber(args.cfg_rescale, 0, 1, 0),
    negative_prompt:
      args.uc || args.negative_prompt || args.undesired_content || DEFAULT_UC,
  };
}
function buildV4Prompt(basePrompt, charCaptions) {
  const useCoords = charCaptions.some((x) =>
    x.centers.some((p) => p.x !== 0.5 || p.y !== 0.5),
  );
  return {
    caption: {
      base_caption: basePrompt || "",
      char_captions: charCaptions.map((x) => ({
        char_caption: x.char_caption,
        centers: x.centers,
      })),
    },
    use_coords: useCoords,
    use_order: true,
  };
}
function buildV4NegativePrompt(uc, charCaptions) {
  return {
    caption: {
      base_caption: uc || DEFAULT_UC,
      char_captions: charCaptions.map((x) => ({
        char_caption: x.char_uc || "",
        centers: x.centers,
      })),
    },
    legacy_uc: false,
  };
}
async function buildVibeFields(vibeEntries) {
  if (vibeEntries.length > 16)
    throw new Error("Vibe Transfer 最多支持 16 个参考图");
  const images = await Promise.all(
    vibeEntries.map((x) => processImageInput(x.image)),
  );
  return {
    reference_image_multiple: images.map(toNaiImageField),
    reference_information_extracted_multiple: vibeEntries.map((x) =>
      Number(x.informationExtracted ?? x.information_extracted ?? 1),
    ),
    reference_strength_multiple: vibeEntries.map((x) =>
      Number(x.strength ?? 0.6),
    ),
  };
}
async function buildGeneratePayload(args, model) {
  const chars = parseCharacterPrompts(args);
  const p = buildBaseParameters(args);
  p.v4_prompt = buildV4Prompt(args.prompt, chars);
  p.v4_negative_prompt = buildV4NegativePrompt(
    args.uc || args.negative_prompt,
    chars,
  );
  p.characterPrompts = [];
  p.inpaintImg2ImgStrength = 1;
  if (args.vibe)
    Object.assign(p, await buildVibeFields(asJson(args.vibe, args.vibe) || []));
  return {
    action: ACTION.GENERATE,
    model,
    input: args.prompt || "",
    parameters: p,
  };
}
async function buildImg2ImgPayload(args, model, imageDataUri) {
  const payload = await buildGeneratePayload(args, model);
  payload.action = ACTION.IMG2IMG;
  payload.parameters.image = toNaiImageField(imageDataUri);
  payload.parameters.strength = clampNumber(args.strength, 0.01, 0.99, 0.7);
  payload.parameters.noise = clampNumber(args.noise, 0, 0.99, 0);
  return payload;
}
async function buildInfillPayload(
  args,
  model,
  imageDataUri,
  maskDataUri,
  actionValue = ACTION.INFILL,
) {
  const payload = await buildGeneratePayload(args, model);
  payload.action = actionValue;
  payload.parameters.image = toNaiImageField(imageDataUri);
  payload.parameters.mask = toNaiImageField(maskDataUri);
  payload.parameters.add_original_image = args.add_original_image === true;
  payload.parameters.strength = clampNumber(args.strength, 0.01, 0.99, 0.7);
  payload.parameters.noise = clampNumber(args.noise, 0, 0.99, 0);
  return payload;
}
async function buildUpscalePayload(args, imageDataUri, width, height) {
  const size = parseFreeSize(args.resolution || args.size);
  return {
    image: toNaiImageField(imageDataUri),
    width: Number(args.width) || width || size.width,
    height: Number(args.height) || height || size.height,
    scale: [2, 4].includes(Number(args.scale)) ? Number(args.scale) : 4,
  };
}
async function buildAugmentPayload(
  reqType,
  imageDataUri,
  width,
  height,
  extra = {},
) {
  const size = parseFreeSize(extra.resolution || extra.size);
  const p = {
    req_type: reqType,
    image: toNaiImageField(imageDataUri),
    width: Number(extra.width) || width || size.width,
    height: Number(extra.height) || height || size.height,
  };
  if (reqType === "emotion")
    Object.assign(p, { emotion: extra.emotion, prompt: extra.prompt });
  if (reqType === "colorize") p.defry = Number(extra.defry || 0);
  return p;
}
async function buildEncodeVibePayload(
  imageDataUri,
  informationExtracted,
  model,
) {
  return {
    image: toNaiImageField(imageDataUri),
    information_extracted: Number(informationExtracted ?? 1),
    model,
  };
}

// ==================== 段 08 · 传输层 ====================
function buildAgents() {
  if (!NOVELAI_PROXY) return { httpAgent: undefined, httpsAgent: undefined };
  return {
    httpAgent: new HttpProxyAgent(NOVELAI_PROXY),
    httpsAgent: new HttpsProxyAgent(NOVELAI_PROXY),
  };
}
async function requestOnce(url, payload, key, options = {}) {
  const method = options.method || "POST";
  const config = {
    method,
    url,
    data: method === "GET" ? undefined : payload,
    params: options.params,
    responseType: options.responseType || "arraybuffer",
    timeout: options.timeout || 180000,
    headers: {
      Authorization: `Bearer ${key}`,
      "Content-Type": "application/json",
    },
    ...buildAgents(),
  };
  if (DEBUG_MODE && method !== "GET") log("request", url, redact(payload));
  return axios(config);
}
async function requestWithRetry(url, payload, key, options = {}) {
  let last;
  for (let attempt = 0; attempt <= MAX_RETRIES; attempt++) {
    try {
      return await requestOnce(url, payload, key, options);
    } catch (error) {
      last = error;
      const status = error.response?.status;
      // 504 由前置网关（Cloudflare 等）返回，不在上游文档的错误码表内，
      // 但属于典型瞬时故障，应与 502/503 同等对待。
      if (
        ![429, 500, 502, 503, 504].includes(status) ||
        attempt === MAX_RETRIES
      )
        throw error;
      await sleep(RETRY_BASE_DELAY_MS * Math.pow(3, attempt));
    }
  }
  throw last;
}
async function dispatch(
  capability,
  requestedModelInput,
  purpose,
  payloadBuilder,
  options = {},
) {
  const resolved =
    requestedModelInput === null
      ? { model: null, note: null }
      : resolveModel(requestedModelInput, purpose);
  const plan = buildChannelPlan(capability, resolved.model);
  if (!plan.length) throw new Error(`没有支持 ${capability} 的可用渠道`);
  const failures = [];
  for (const candidate of plan) {
    try {
      const payload = await payloadBuilder(candidate.model);
      const requestUrl = `${candidate.url}${candidate.prefix || ""}${options.endpoint}`;
      const response = await requestWithRetry(
        requestUrl,
        payload,
        candidate.key,
        options,
      );
      return {
        response,
        model: candidate.model,
        note: resolved.note,
        channelUrl: candidate.url,
        requestUrl,
      };
    } catch (error) {
      failures.push(
        `${candidate.url}${candidate.prefix || ""} / ${candidate.model || "-"}: ${describeResponseError(error)}`,
      );
    }
  }
  throw new Error(`全部渠道请求失败：\n${failures.join("\n")}`);
}
async function dispatchWithEnumProbe(
  enumKey,
  capability,
  modelInput,
  purpose,
  payloadBuilderFactory,
  options = {},
) {
  const candidates = ENUM_PROBE ? ENUM_CANDIDATES[enumKey] || [null] : [null];
  const failures = [];
  for (const value of candidates) {
    try {
      const result = await dispatch(
        capability,
        modelInput,
        purpose,
        (model) => payloadBuilderFactory(model, value),
        options,
      );
      if (value)
        console.error(
          `[ENUM_PROBE] ${enumKey} 命中值: ${value}，建议固化到配置`,
        );
      return result;
    } catch (error) {
      failures.push(`${value || "default"}: ${error.message}`);
      const message = String(error.message);
      const looksLikeEnumRejection =
        /\b400\b/.test(message) ||
        /infill|inpainting|bg.?removal|req_type|invalid\s+action/i.test(message);
      if (!ENUM_PROBE || !looksLikeEnumRejection) throw error;
    }
  }
  throw new Error(`枚举候选耗尽：${failures.join("\n")}`);
}

// ==================== 段 09 · 响应解析层 ====================
async function extractImagesFromZip(zipBuffer) {
  return new Promise((resolve, reject) => {
    const images = [];
    let settled = false;
    yauzl.fromBuffer(zipBuffer, { lazyEntries: true }, (err, zip) => {
      if (err) return reject(new Error(`读取 ZIP 失败: ${err.message}`));
      zip.readEntry();
      zip.on("entry", (entry) => {
        if (
          /\/$/.test(entry.fileName) ||
          !/\.(png|jpe?g|webp|gif)$/i.test(entry.fileName)
        )
          return zip.readEntry();
        zip.openReadStream(entry, (e, stream) => {
          if (e) return reject(e);
          const chunks = [];
          stream.on("data", (c) => chunks.push(c));
          stream.on("error", reject);
          stream.on("end", () => {
            const buffer = Buffer.concat(chunks);
            images.push({ buffer, mimeType: guessMimeFromBuffer(buffer) });
            zip.readEntry();
          });
        });
      });
      zip.on("end", () => {
        if (settled) return;
        settled = true;
        images.length
          ? resolve(images)
          : reject(new Error("NovelAI ZIP 响应为空，未找到图片"));
      });
      zip.on("error", reject);
    });
  });
}
function decodeImageValue(value) {
  if (typeof value !== "string") return null;
  const m = value.match(/^data:(image\/[^;]+);base64,(.+)$/i);
  if (m) return { buffer: Buffer.from(m[2], "base64"), mimeType: m[1] };
  if (/^[A-Za-z0-9+/=]{100,}$/.test(value))
    return { buffer: Buffer.from(value, "base64"), mimeType: "image/png" };
  return null;
}
function parseJsonImageResponse(parsed) {
  const out = [];
  const add = (x) => {
    if (typeof x === "string" && /^https?:\/\//i.test(x)) return;
    const y = decodeImageValue(x);
    if (y) out.push(y);
  };
  for (const x of parsed?.images || []) add(x.image || x.b64 || x.url);
  for (const x of parsed?.data || []) add(x.b64_json || x.url);
  for (const x of parsed?.content || [])
    if (x.type === "image_url") add(x.image_url?.url || x.url);
  const text = JSON.stringify(parsed);
  for (const x of text.match(/data:image\/[^;]+;base64,[A-Za-z0-9+/=]+/g) || [])
    add(x);
  return out;
}
async function parseImageResponse(response) {
  const type = String(response.headers?.["content-type"] || "").toLowerCase();
  const buffer = Buffer.from(response.data);
  if (type.includes("zip") || type.includes("octet-stream"))
    return extractImagesFromZip(buffer);
  if (type.includes("application/json")) {
    const parsed = JSON.parse(buffer.toString("utf8"));
    const images = parseJsonImageResponse(parsed);
    if (!images.length) throw new Error("JSON 响应中未找到图片");
    return images;
  }
  if (type.includes("image/"))
    return [{ buffer, mimeType: type.split(";")[0] }];
  if (type.includes("msgpack"))
    throw new Error(
      `响应为 MessagePack 格式（${type}），当前版本未实现解析。该渠道的此端点可能仅提供 MessagePack 输出，请改用其他端点或渠道。`,
    );
  const text = buffer.toString("utf8");
  throw new Error(`未知响应类型 ${type}: ${truncate(text, 500)}`);
}

// ==================== 段 10 · 输出层 ====================
function extensionForMime(mime) {
  return (
    { "image/jpeg": "jpg", "image/webp": "webp", "image/gif": "gif" }[mime] ||
    "png"
  );
}
function buildAccessibleUrl(relativePath) {
  const base = (VAR_HTTPS_URL || `${VAR_HTTP_URL}:${SERVER_PORT}`).replace(
    /\/$/,
    "",
  );
  return `${base}/pw=${IMAGESERVER_IMAGE_KEY}/images/${relativePath}`;
}
async function saveImages(images, subDir = "novelaigen") {
  const dir = assertPathInside(
    PROJECT_BASE_PATH,
    path.resolve(PROJECT_BASE_PATH, "image", subDir),
  );
  await fs.mkdir(dir, { recursive: true });
  const saved = [];
  for (const image of images) {
    const fileName = `${uuidv4()}.${extensionForMime(image.mimeType)}`;
    const localPath = assertPathInside(dir, path.resolve(dir, fileName));
    await fs.writeFile(localPath, image.buffer);
    const serverPath = `image/${subDir}/${fileName}`;
    saved.push({
      fileName,
      serverPath,
      localPath,
      accessibleUrl: buildAccessibleUrl(toPosixRelative(subDir, fileName)),
    });
  }
  return saved;
}
function buildSuccessResult(
  savedImages,
  meta = {},
  showBase64 = false,
  imageBuffers = [],
) {
  const lines = [
    `NovelAI ${meta.command || "操作"}成功，共 ${savedImages.length} 张图片`,
    `模型: ${meta.model || "-"} | 尺寸: ${meta.size || "-"} | 采样器: ${meta.sampler || "-"} | 步数: ${meta.steps || "-"} | scale: ${meta.scale || "-"} | seed: ${meta.seed ?? "-"} | 数量: ${savedImages.length}`,
  ];
  if (meta.note) lines.push(`提示: ${meta.note}`);
  savedImages.forEach((x, i) =>
    lines.push(
      `图片 ${i + 1}: ${x.accessibleUrl} | ${x.serverPath} | ${x.fileName}`,
    ),
  );
  lines.push("请使用返回的 URL 生成 <img> 标签展示图片。");
  const content = [{ type: "text", text: lines.join("\n") }];
  if (showBase64)
    imageBuffers.forEach((x) =>
      content.push({
        type: "image_url",
        image_url: {
          url: `data:${x.mimeType};base64,${x.buffer.toString("base64")}`,
        },
      }),
    );
  return {
    content,
    details: {
      serverPath: savedImages.map((x) => x.serverPath),
      fileName: savedImages.map((x) => x.fileName),
      imageUrls: savedImages.map((x) => x.accessibleUrl),
      prompt: truncate(meta.prompt),
      command: meta.command,
      model: meta.model,
      size: meta.size,
      seed: meta.seed,
      imageCount: savedImages.length,
      note: meta.note || null,
    },
  };
}

// ==================== 段 11 · 命令 handler 层 ====================
function normalizeArgs(rawArgs) {
  const args = { ...rawArgs };
  const raw = String(
    args.command || args.commandIdentifier || "",
  ).toLowerCase();
  const map = {
    generate: "generate",
    txt2img: "generate",
    t2i: "generate",
    novelaigenerateimage: "generate",
    img2img: "img2img",
    i2i: "img2img",
    edit: "img2img",
    inpaint: "inpaint",
    infill: "inpaint",
    novelaiinpaint: "inpaint",
    upscale: "upscale",
    enhance: "upscale",
    augment: "augment",
    director: "augment",
    encode_vibe: "encode_vibe",
    vibe: "encode_vibe",
    suggest_tags: "suggest_tags",
    tags: "suggest_tags",
    subscription: "subscription",
    account: "subscription",
    anlas: "subscription",
  };
  args.command =
    map[raw] ||
    (args.mask
      ? "inpaint"
      : collectImageInputs(args).length
        ? "img2img"
        : "generate");
  args.prompt = args.prompt || args.Prompt || args.text;
  args.resolution = args.resolution || args.size || args.image_size;
  args.uc = args.uc || args.negative_prompt || args.undesired_content;
  return args;
}
async function saveGenerationResult(result, args, showBase64, command) {
  const images = await parseImageResponse(result.response);
  const saved = await saveImages(images);
  return buildSuccessResult(
    saved,
    {
      command,
      model: result.model,
      note: result.note,
      prompt: args.prompt,
      size: args.resolution,
      seed: asJson(args.seed, args.seed),
      sampler: args.sampler || DEFAULT_SAMPLER,
      steps: args.steps || DEFAULT_STEPS,
      scale: args.scale || DEFAULT_SCALE,
    },
    showBase64,
    images,
  );
}
async function handleGenerate(args, showBase64) {
  if (args.vibe) assertVibeSupported(resolveModel(args.model, "base").model);
  const result = await dispatch(
    "gen",
    args.model,
    "base",
    (model) => buildGeneratePayload(args, model),
    { endpoint: ENDPOINTS.GENERATE },
  );
  return saveGenerationResult(result, args, showBase64, "generate");
}
async function handleImg2Img(args, showBase64) {
  const input = collectImageInputs(args)[0];
  if (!input) throw new Error("img2img 缺少 image 参数");
  const image = await processImageInput(input);
  const result = await dispatch(
    "i2i",
    args.model,
    "base",
    (model) => buildImg2ImgPayload(args, model, image),
    { endpoint: ENDPOINTS.GENERATE },
  );
  return saveGenerationResult(result, args, showBase64, "img2img");
}
async function handleInpaint(args, showBase64) {
  const input = collectImageInputs(args)[0];
  if (!input || !args.mask)
    throw new Error("inpaint 必须同时提供 image 与 mask");
  const image = await processImageInput(input),
    mask = await processImageInput(args.mask);
  const result = await dispatchWithEnumProbe(
    "action_infill",
    "infill",
    args.model,
    "inpainting",
    (model, action) => buildInfillPayload(args, model, image, mask, action),
    { endpoint: ENDPOINTS.GENERATE },
  );
  return saveGenerationResult(result, args, showBase64, "inpaint");
}
async function handleUpscale(args, showBase64) {
  const input = collectImageInputs(args)[0];
  if (!input) throw new Error("upscale 缺少 image 参数");
  const image = await processImageInput(input);
  const result = await dispatch(
    "upscale",
    null,
    "base",
    () => buildUpscalePayload(args, image),
    { endpoint: ENDPOINTS.UPSCALE },
  );
  return saveGenerationResult(result, args, showBase64, "upscale");
}
async function handleAugment(args, showBase64) {
  const req = args.req_type || args.reqType || "emotion";
  if (!AUGMENT_REQ_TYPES.includes(req))
    throw new Error(
      `未知 augment req_type ${req}，可选：${AUGMENT_REQ_TYPES.join(", ")}`,
    );
  const input = collectImageInputs(args)[0];
  if (!input) throw new Error("augment 缺少 image 参数");
  const image = await processImageInput(input);
  const factory = (model, value) =>
    buildAugmentPayload(value || req, image, undefined, undefined, args);
  const result =
    req === "bg-removal"
      ? await dispatchWithEnumProbe(
          "augment_bgremoval",
          "augment",
          null,
          "base",
          factory,
          { endpoint: ENDPOINTS.AUGMENT },
        )
      : await dispatch("augment", null, "base", () => factory(null, req), {
          endpoint: ENDPOINTS.AUGMENT,
        });
  return saveGenerationResult(result, args, showBase64, "augment");
}
async function handleEncodeVibe(args) {
  const input = collectImageInputs(args)[0];
  if (!input) throw new Error("encode_vibe 缺少 image 参数");
  const image = await processImageInput(input);
  const raw = toNaiImageField(image),
    info = Number(args.informationExtracted ?? args.information_extracted ?? 1),
    model = resolveModel(args.model, "base").model;
  assertVibeSupported(model);
  const dir = assertPathInside(
    PROJECT_BASE_PATH,
    path.resolve(PROJECT_BASE_PATH, "image", "novelaigen", "vibes"),
  );
  await fs.mkdir(dir, { recursive: true });
  const file = path.resolve(
    dir,
    `${crypto
      .createHash("sha256")
      .update(raw + info)
      .digest("hex")
      .slice(0, 16)}.json`,
  );
  try {
    const cached = JSON.parse(await fs.readFile(file, "utf8"));
    return {
      content: [
        {
          type: "text",
          text: `Vibe 编码命中缓存，未消耗 Anlas: ${toPosixRelative("image", "novelaigen", "vibes", path.basename(file))}`,
        },
      ],
      details: { cacheHit: true, vibeFilePath: file, vibe: cached },
    };
  } catch {}
  const result = await dispatch(
    "vibe",
    model,
    "base",
    (m) => buildEncodeVibePayload(image, info, m),
    { endpoint: ENDPOINTS.ENCODE_VIBE },
  );
  const data = JSON.parse(Buffer.from(result.response.data).toString("utf8"));
  await fs.writeFile(file, JSON.stringify(data, null, 2));
  return {
    content: [{ type: "text", text: `Vibe 编码完成，已保存 ${file}` }],
    details: { cacheHit: false, vibeFilePath: file, vibe: data },
  };
}
async function handleSuggestTags(args) {
  const result = await dispatch("tags", null, "base", () => null, {
    endpoint: ENDPOINTS.SUGGEST_TAGS,
    method: "GET",
    responseType: "json",
    params: { prompt: args.prompt || "" },
  });
  return {
    content: [{ type: "text", text: JSON.stringify(result.response.data) }],
    details: { command: "suggest_tags" },
  };
}
// 官方账户 API 在独立 host（api.novelai.net）；中转站在同 host 加前缀。
// 按渠道是否配置 prefix 分流，并逐渠道汇总结果。
async function handleSubscription() {
  if (!CHANNELS.length) throw new Error("订阅查询需要至少一个已配置渠道");
  const results = [];
  const failures = [];
  for (const channel of CHANNELS) {
    const base = channel.prefix
      ? `${channel.url}${channel.prefix}`
      : NOVELAI_ACCOUNT_URL.replace(/\/$/, "");
    const url = `${base}${ENDPOINTS.SUBSCRIPTION}`;
    try {
      const response = await requestWithRetry(url, null, channel.key, {
        method: "GET",
        responseType: "json",
      });
      results.push({ channel: channel.url, url, data: response.data });
    } catch (error) {
      failures.push(`${url}: ${describeResponseError(error)}`);
    }
  }
  if (!results.length)
    throw new Error(`全部渠道订阅查询失败：\n${failures.join("\n")}`);
  const lines = results.map(
    (x) => `渠道 ${x.channel}\n${JSON.stringify(x.data, null, 2)}`,
  );
  if (failures.length)
    lines.push(`以下渠道查询失败：\n${failures.join("\n")}`);
  return {
    content: [{ type: "text", text: lines.join("\n\n") }],
    details: { command: "subscription", accounts: results, failures },
  };
}

// ==================== 段 12 · main 入口 ====================
function outputAndExit(payload, code = 0) {
  const text = JSON.stringify(payload);
  process.stdout.write(text, () => process.exit(code));
}
async function main() {
  let raw = "";
  for await (const chunk of process.stdin) raw += chunk;
  if (!raw.trim())
    return outputAndExit(
      { status: "error", error: "NovelAI Plugin Error: 未收到 stdin 输入" },
      1,
    );
  let args;
  try {
    args = normalizeArgs(JSON.parse(raw));
    if (
      !PROJECT_BASE_PATH ||
      !SERVER_PORT ||
      !IMAGESERVER_IMAGE_KEY ||
      !VAR_HTTP_URL
    )
      throw new Error(
        "缺少 PROJECT_BASE_PATH、SERVER_PORT、IMAGESERVER_IMAGE_KEY 或 VarHttpUrl",
      );
    if (!CHANNELS.length)
      throw new Error("未配置 NOVELAI_API_KEY 或有效的多渠道");
    const showBase64 = args.showbase64 === "true" || args.showbase64 === true;
    const handlers = {
      generate: handleGenerate,
      img2img: handleImg2Img,
      inpaint: handleInpaint,
      upscale: handleUpscale,
      augment: handleAugment,
      encode_vibe: handleEncodeVibe,
      suggest_tags: handleSuggestTags,
      subscription: handleSubscription,
    };
    if (!handlers[args.command]) throw new Error(`未知命令 ${args.command}`);
    outputAndExit({
      status: "success",
      result: await handlers[args.command](args, showBase64),
    });
  } catch (error) {
    let text = error.message || String(error);
    if (error.response?.data)
      text += ` - API Response: ${describeResponseError(error)}`;
    outputAndExit(
      { status: "error", error: `NovelAI Plugin Error: ${text}` },
      1,
    );
  }
}
main();
