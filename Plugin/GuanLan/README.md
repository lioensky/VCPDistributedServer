# 📊 GuanLan - A股智能数据引擎

> **为 AI-Agent 打造的 A股量化感知器官。** 让你的 Agent 在对话流中一句话完成查行情、扫异动、跑回测、看持仓、测压力——不需要打开 VNpy 终端，不需要写 Backtrader 脚本，不需要登录同花顺。

**版本** v4.0.0 | **作者** 观澜 & 冬竹子（翔） | **协议** CC BY-NC-SA 4.0

---

## 🎯 这是什么？

GuanLan 是一个 [VCPToolBox](https://github.com/lioensky/VCPToolBox) 插件，赋予 AI-Agent 专业级 A股投研分析能力。

它不是一个量化交易框架，不接实盘——这是**安全设计而非缺陷**。它的定位是**Agent 的量化感知层**：在对话中实时获取行情、技术面、基本面、资金面、事件异动、市场情绪等全维度数据，辅助用户做出更理性的投资决策。

### 与市面产品的区别

| 维度 | VNpy / QMT | QuantConnect / Backtrader | 同花顺 / 东方财富 | **GuanLan** |
|------|-----------|--------------------------|-----------------|-------------|
| 定位 | 实盘量化交易框架 | 专业回测平台 | 行情终端 | **Agent量化感知器官** |
| 交互方式 | Python API / CTP | Python 脚本 | GUI 点击 | **自然语言对话** |
| 实盘交易 | ✅ 支持 | ❌ | 仅信号 | ❌（安全设计） |
| 回测引擎 | ✅ 专业级 | ✅ Walk-Forward | ❌ | ✅ 轻量级（4策略） |
| AI 集成 | 需自行开发 | 需自行开发 | ❌ | **原生 Agent 工具** |
| 数据容灾 | 单源 | 单源 | 单源 | **双引擎自动切换** |
| 部署成本 | 高（C++底层） | 中（云端） | 安装即用 | **pip install 即用** |

**核心差异**：VNpy 是给人写的，GuanLan 是给 Agent 用的。用户只需要对 Agent 说"分析一下紫金矿业"，Agent 自动调用 `full_analysis` 拉取四维度数据并给出明确建议。

---

## ✨ 核心特性

### 1. DataHub 双引擎容灾（无单点故障）

三层数据架构，每个关键函数都有 fallback：

```
新浪财经API（实时行情/K线，秒级响应）
    ↓ 失败时
Tushare HTTP API（基本面/资金流向/板块/指数）
    ↓ 失败时
AKShare 容灾层（自动接管，5个降级函数覆盖全部关键维度）
```

这不是简单的 try/except——每个容灾函数**重新解析数据格式**，确保降级后字段语义一致。主流框架通常只支持单一数据源，GuanLan 在 A股数据源频繁变更的环境下实现了真正的生产级高可用。

### 2. 真实A股费率引擎（v3.2+）

内置与真实券商对齐的费率计算模型，盈亏复盘精准到分：
- **佣金**：支持配置（股票/ETF分别设置，默认万2.5，最低5元）
- **印花税**：千1（仅卖出收取，ETF免收）
- **过户费**：万0.1（仅沪市收取）
买入时手续费自动摊入持仓成本价，卖出时自动计算净到手金额，胜率和盈亏比统计与实盘完全一致。

### 3. filelock 跨进程并发安全（v3.2+）

`@synchronized_data` 装饰器 + FileLock，保护状态读写函数。当多个 Agent 并发调用 `position_add` 和 `position_close` 时，文件锁自动串行化，彻底杜绝 JSON 读写竞态（Race Condition）。同时支持 `position_update` 秒级更新止损/目标价（插件原生命令，不触发系统文件审批拦截）。

### 4. 38 个专业命令（覆盖投研全链路）

| 分类 | 命令 | 核心能力 |
|------|------|---------|
| **基础行情** | `realtime_quote` / `batch_quotes` / `stock_info` / `sector_ranking` | 秒级行情、批量查询、PE/PB/市值、行业板块涨跌排名 |
| **技术分析** | `kline_indicators` / `full_analysis` / `valuation_percentile` | MA/MACD/RSI/布林带/KDJ/OBV/ATR/WR/CCI、四维度综合分析、PE/PB历史分位数 |
| **资金分析** | `capital_flow` | 主力/超大单/大单/中单/小单 5层资金流向（ETF不覆盖） |
| **持仓管理** | `position_add` / `position_close` / `position_update` / `position_show` / `portfolio_summary` | 建仓/平仓/减仓/更新止损目标、真实费率算盈亏、全仓位概览 |
| **交易记录** | `trade_history` / `trade_stats` / `trade_stats_monthly` | 完整流水、胜率统计、按月盈亏比 |
| **账户资金** | `account_set` / `account_show` | 总资本/可用资金管理 |
| **自选股** | `watchlist_add` / `watchlist_remove` / `watchlist_show` | 自选股增删查 |
| **异动扫描** | `scan_anomalies` / `daily_report` | 7类技术异动 + 持仓监控 + 盘后日报 |
| **事件扫描** | `scan_events` / `lhb_detail` / `block_trade` / `share_unlock` / `earnings_forecast` | 龙虎榜/大宗交易/限售解禁/业绩预告 4类事件异动 |
| **舆情分析** | `sentiment_scan` / `sentiment_rank` | 5维度情绪聚合 + 全市场人气排名TOP100 |
| **压力测试** | `stress_test` | 5历史极端场景 + 自定义跌幅 |
| **板块轮动** | `sector_rotation` | 31行业 5/10/20日动量，6类信号分类 |
| **市场温度计** | `market_temperature` | 涨跌停+涨跌比+换手率+成交额 → 0-100评分 |
| **ATR止损** | `update_trailing_stops` | 基于ATR(14)×2.5的跟踪止损，只上移不下移 |
| **策略回测** | `backtest` | MA交叉/MACD/RSI/布林 4策略，输出年化/回撤/夏普/胜率 |
| **选股框架** | `stock_screen` / `market_check` | 大盘环境判断 + **五风格组分路由选股(v4.0)** + 三问 + 禁买清单 + 版本戳 |

### 5. A股特性深度适配

- **龙虎榜/大宗交易/限售解禁/业绩预告**：A股信息驱动市场的核心事件类型，主流海外平台无直接竞品
- **ETF 专项数据流**：自动识别 ETF 代码，切换至东财实时快照（含折价率/IOPV/净份额）
- **申万一级行业分类**：板块轮动追踪基于申万 31 个一级行业，非东财概念板块

---

## 📦 安装与配置

### 1. 依赖安装

```bash
pip install -r requirements.txt
```

建议额外安装 `pandas-ta`（KDJ/OBV/ATR 等扩展指标）：
```bash
pip install pandas-ta
```
> 未安装 pandas-ta 时自动降级为纯 numpy 计算，不影响基础功能。

### 2. 数据源配置（可选）

**开箱即用**：新浪行情 API + AKShare 完全免费，无需任何配置即可使用大部分功能。

**启用高级功能**（精确 PE/PB、主力资金流向、板块轮动历史数据）：
1. 复制 `config.env.example` 为 `config.env`
2. 在 [Tushare](https://tushare.pro/) 注册（免费）获取 Token
3. 填入配置：
   ```env
   TUSHARE_TOKEN=你的Token
   
   # 佣金费率（用于精确计算盈亏，默认万2.5）
   BROKER_COMMISSION_STOCK=0.00025
   BROKER_COMMISSION_ETF=0.00025
   ```
> 未配置 Token 时，相关功能自动降级到 AKShare 容灾层。
> 未配置佣金费率时，默认使用万2.5，印花税和过户费按国家统一标准自动计算。

### 3. 在 VCPToolBox 中配置与使用

为了让 Agent 知道如何调用插件，需将压缩包内的 `GuanLanToolBox.txt`（工具说明文件）注入到 Agent 的系统提示词中：

1. **放置工具说明**：将 `GuanLanToolBox.txt` 放入 VCPToolBox 的 `TVStxt/` 目录（或您存放全局工具说明的目录）。
2. **注册折叠工具箱**：在 VCPToolBox 后端管理面板的折叠工具箱管理页面中新增条目，或直接在 VCPToolBox 根目录的 `toolbox_map.json` 中添加指向该文件的配置：`"VCPGuanLanToolBox": "GuanLanToolBox.txt"`。

> **提示**：`GuanLanToolBox.txt` 包含 GuanLan、TradingAgents-CN 和 DigitalOracle 三个工具的完整调用说明。如果您只使用 GuanLan 插件，Agent 会自动跳过不存在的工具调用，不影响正常使用。如果您同时部署了推荐的投研环境，则可以享受完整的投研工具链体验。
3. **Agent 设定注入**：在您的 Agent 设定文件（如 `Agent/YourAgent.txt`）的“————工具箱————”区域，添加占位符：`{{VCPGuanLanToolBox}}`。

完成上述配置后，Agent 即可在对话中根据用户的自然语言意图自动调用相关指令。

#### 💬 使用示例

**场景1：个股综合分析**
> 用户："分析一下紫金矿业"
> Agent 自动调用 `full_analysis` → 整合行情+技术面+基本面+资金面 → 输出明确建议（偏多/偏空/观望 + 入场价 + 止损线 + 信心度）

**场景2：盘中异动监控**
> 用户："今天自选股有什么异动？"
> Agent 自动调用 `scan_anomalies` → 扫描7类技术异动 + 持仓止损/目标触发 → 返回severity分级警报

**场景3：策略回测验证**
> 用户："茅台用RSI策略回测一下去年表现"
> Agent 自动调用 `backtest`（strategy=rsi, 2024全年）→ 输出年化收益率/最大回撤/夏普比率/胜率/交易明细

**场景4：风控压力测试**
> 用户："如果再来一次2015股灾，我的持仓会亏多少？"
> Agent 自动调用 `stress_test`（scenario=crash_2015）→ 用行业Beta模型估算每只持仓的压力损失

**场景5：板块轮动追踪**
> 用户："最近哪些行业资金在流入？"
> Agent 自动调用 `sector_rotation` → 31个申万行业5/10/20日动量分析 → 返回加速流入/持续上行/超跌反弹等信号分类

**场景6：持仓管理与复盘**
> 用户："买入200股紫金矿业，成本28.9，止损27，目标31"
> Agent 自动调用 `position_add` → 扣减可用资金 + 写入交易记录
> 用户："我的持仓情况怎么样？"
> Agent 自动调用 `portfolio_summary` → 实时盈亏 + 距止损/目标距离 + ATR动态止损参考线 + 总资产
> 用户："这个月交易复盘一下"
> Agent 自动调用 `trade_stats_monthly` → 按月统计胜率/盈亏比/总盈亏

**场景7：市场全景感知**
> 用户："今天市场情绪怎么样？"
> Agent 自动调用 `market_temperature` → 涨跌停+涨跌比+换手率+成交额 → 0-100评分（极热/偏热/中性/偏冷/极冷）

**场景8：事件驱动扫描**
> 用户："我的自选股最近有龙虎榜或大宗交易吗？"
> Agent 自动调用 `scan_events` → 扫描龙虎榜/大宗交易/限售解禁/业绩预告4类事件异动

**场景9：市场情绪感知**
> 用户："紫金矿业现在市场情绪怎么样？散户和机构怎么看？"
> Agent 自动调用 `sentiment_scan` → 5维度情绪聚合（机构参与度/综合评价/关注度/买入欲望/热门概念）→ 输出情绪温度和题材热度分布
> 进阶用法：买入欲望>80警惕散户接盘；关注度低+评价高=左侧逆向机会；题材热度变化揭示市场交易逻辑切换

**场景10：智能选股（v4.0 五风格组分路由）**
> 用户："帮我推荐一只股票"
> Agent 自动调用 `stock_screen` → 触发禁买清单（市值<100亿 / RSI>70 / 均线空头 / 破布林上轨）直接拦截返回 REJECT，或按行业风格分组（A周期/B金融/C成长/D消费/E稳定）走独立估值路由，通过 Q1(趋势)/Q2(盈利能力)/Q3(价格合理)/Q5(安全垫) 四关测试返回 PASS 及详细数据依据。
> v4.0 核心改进：不再用 PB/ROE 一刀切，而是按行业特性分别校验——周期股看 PE/PB 历史分位数，金融股看破净+拨备，成长股看 PEG，消费股看 PE 分位数+PB分位数，稳定股看股息率。避免"用尺子量温度"。


---

## 🤝 推荐搭配：TradingAgents-CN 深度投研

GuanLan 是**快速感知层**（秒级行情+技术面+异动扫描），但投资决策有时需要更深度的多维度研判。强烈推荐搭配 [TradingAgents-CN](https://github.com/hsliuping/TradingAgents-CN) 使用，形成**"快速感知 → 深度研判"两段式投研闭环**。

### 两者定位差异

| 维度 | GuanLan | TradingAgents-CN |
|------|---------|------------------|
| **定位** | Agent的量化感知器官 | 多Agent深度辩论投研引擎 |
| **响应速度** | 秒级（1-8秒） | 分钟级（8-10分钟） |
| **分析深度** | 技术面+基本面+资金面+事件面 | 4分析师多维度辩论+多空对弈+风控三方辩论 |
| **架构** | 单Agent工具调用 | 多Agent图（Market/Fundamental/News/Social → Bull/Bear → 投委会 → 风控） |
| **适合场景** | 日常盯盘、快速筛选、持仓管理 | 关键标的深度研判、买卖决策最终裁决 |

### 配合使用流程

```
日常盯盘：GuanLan scan_anomalies → 无异动 → 继续监控
                                      ↓ 发现异动/关键决策点
深度研判：TradingAgents-CN 多Agent辩论（8-10分钟）
          → 4分析师汇报 → 多空对弈 → 投委会裁决 → 风控三方辩论 → 最终决策
                                      ↓ 得出明确方向
执行层：  GuanLan position_add/close → 仓位管理 + ATR动态止损 + 盘后复盘
```

**实战示例**：
1. GuanLan `scan_anomalies` 发现紫金矿业主力资金连续流入 + 放量突破MA20
2. 触发 TradingAgents-CN 深度分析 → 4维度分析师辩论 → 裁决"买入，信心度0.75"
3. 回到 GuanLan `position_add` 建仓，设置止损/目标
4. 持续用 GuanLan `portfolio_summary` 监控，ATR跟踪止损自动上移锁利润
5. 月末用 `trade_stats_monthly` 复盘胜率和盈亏比

### TradingAgents-CN 部署要点

TradingAgents-CN 基于 Docker 部署（5容器：MongoDB + Redis + FastAPI + Vue3 + Nginx），通过 PowerShellExecutor 调用容器内 `ta_run4.py` 执行。Agent 在对话中自然语言触发即可（"深度分析紫金矿业"），无需用户手动操作。详见 [TradingAgents-CN](https://github.com/hsliuping/TradingAgents-CN)。

---

## 🌍 推荐搭配：DigitalOracle 全球金融数据信源

GuanLan 专注于 **A股市场** 的数据感知，但 A 股从来不是孤立的——外围市场情绪、美联储利率预期、大宗商品价格、全球宏观风险都会深刻影响 A 股走势。搭配 [DigitalOracle] 插件，让 Agent 具备**全球宏观视野**，实现内外盘联动分析。

### 定位差异

| 维度 | GuanLan | DigitalOracle |
|------|---------|---------------|
| **覆盖市场** | A股（沪深两市） | 全球（美股/外汇/商品/加密/预测市场） |
| **数据类型** | 行情/基本面/资金/事件/情绪 | 宏观指标/利率预期/大宗商品/恐慌指数/期权隐含波动率 |
| **适合场景** | 个股盯盘、选股回测、持仓管理 | 建立盘前全球宏观基准、验证板块逻辑（如金价验证黄金股）、监控外围风险事件 |

### 配合使用流程

```
盘前（07:00-09:00）：DigitalOracle → 恐惧贪婪指数 + 美联储利率预期 + 隔夜美股/黄金/原油表现
                     → 建立今日全球宏观基准："外围偏暖/偏冷？大宗商品方向？"
                                ↓
盘中（09:30-15:00）：GuanLan → A股个股行情 + 板块轮动 + 资金流向
                     → 结合外围基准判断："有色板块是否跟随LME铜价？黄金股是否跟随COMEX金价？"
                                ↓
盘后（15:30+）：    GuanLan 日报 + DigitalOracle 尾盘情绪
                     → 内外盘联动复盘，制定次日策略
```

**实战示例**：
1. 盘前 DigitalOracle 拉取美联储利率预期（FedWatch）+ 美元指数（DXY）+ COMEX 黄金价格
2. 判断："美元走弱 + 黄金走强 → 利好 A 股有色/黄金板块"
3. GuanLan `sector_rotation` 验证有色板块是否已出现资金流入信号
4. 若信号共振 → GuanLan `stock_screen` 筛选板块内优质标的
5. 建仓后持续用 GuanLan 监控，同时用 DigitalOracle 跟踪大宗商品是否维持趋势

> **部署提示**：DigitalOracle 是 VCP 内置插件，可直接使用。

---

## ⏰ 推荐搭配：VCP 定时任务实现全自动盯盘

GuanLan 的命令可以结合 VCPToolBox 的**定时任务系统（VCPTaskAssistant / AgentAssistant）**实现自动执行和主动推送。不需要用户盯着屏幕，Agent 会在关键时刻主动找你。

### 三种自动化场景

**场景1：盘中异动自动扫描+持仓风控自动监控**
```
定时任务配置：工作日 9:30-15:00 每30分钟（时间自定）唤醒Agent
Agent自动执行：
  → scan_anomalies（7类技术异动检测）
  → scan_events（4类事件异动检测）
  → 有异动 → 通过 SmtpMailer 邮件推送 / AgentAssistant / 企业微信 等通知
  → 无异动 → 静默不打扰

  → portfolio_summary（持仓盈亏 + 距止损/目标距离）
  → update_trailing_stops（ATR动态止损自动上移）
  → 止损/目标触发 → 立即推送告警："紫金矿业已跌破止损线27元"
```

**场景2：盘后自动复盘（每日收盘）**
```
定时任务配置：工作日 15:30 自动唤醒Agent
Agent自动执行：
  → market_temperature（当日市场情绪评分）
  → daily_report（自选股表现 + 次日关注要点）
  → 整合为日报邮件推送给用户
```

### 配置要点

通过 VCPTaskAssistant 的 `custom_prompt + cron` 实现周期性任务。Agent 被唤醒后自动调用 GuanLan 命令，并根据结果判断是否需要通知用户（**有异动才打扰，无异动不打扰**）。

> **安全铁律**：定时任务唤醒的 Agent **严禁修改源码或文件**，只能执行数据查询和通知推送。任务模板中必须包含行为边界约束。

---

## 🏗️ 架构设计

### 数据流

```
用户自然语言 → Agent 理解意图 → 选择命令 → main.py 路由 → 数据源适配层 → 结果JSON → Agent 整合 → 自然语言回复
```

### 并发安全

```python
@synchronized_data  # filelock 跨进程锁
def position_close(symbol, sell_price, shares=None, ...):
    with DATA_LOCK:  # 自动获取/释放
        positions = read_positions()
        # ... 安全读写 ...
```

### 双源降级示例

```python
def _get_daily_basic(symbol):
    data = _tushare_api('daily_basic', ...)    # 主源
    if not data:
        return _ak_daily_basic(symbol)          # 容灾接管
    return data
```

---

## ⚠️ 已知限制

| 限制 | 说明 | 影响 |
|------|------|------|
| **回测引擎为轻量级** | 全仓买卖模型、固定佣金、无 Walk-Forward 参数寻优。定位是"快速验证信号质量"，非专业回测 | 过拟合风险，建议结果仅作参考 |
| **压力测试 Beta 为静态近似值** | 行业 Beta 为经验估值（31个行业硬编码），行业归属通过股票名称关键词猜测 | 压力测试结果为近似值 |
| **ETF 异动扫描部分失效** | AKShare 全市场行情对 ETF 代码覆盖不全 | 盘中异动扫描对 ETF 可能返回空 |
| **事件接口非交易时段超时** | AKShare 事件类接口底层爬东财/同花顺网页，周末响应缓慢 | 已加 try/except 降级，交易时段稳定 |
| **无实盘交易接口** | 设计上不接 CTP/券商 API | 安全设计，防止 Agent 自主下单 |
| **PEG的G用历史增速近似**（v4.0） | stock_screen 中 PEG 的 G 使用营收同比(or_yoy)近似，非卖方一致预期 | 后视镜不是望远镜，但彼得·林奇实操中也大量使用历史增速 |
| **fina_indicator报告期对齐**（v4.0） | stock_screen 优先取年报数据，若年报未出则降级取季报，标记 `[stale_data]` | ROE 可能偏低（季报累计非年化），不影响 PASS/REJECT 判断 |
| **拨备覆盖率待接入**（v4.0） | 银行 Q5 安全垫的拨备覆盖率≥150%尚未接入 | 当前银行 Q5 跳过，Phase 2 待找数据源 |

---

## 📋 版本历史

| 版本 | 日期 | 主要变更 |
|------|------|----------|
| v2.0 | 2026-05 | 异动扫描(7类)+自选股管理+盘后日报 |
| v2.5 | 2026-06 | Tushare迁移+新浪源切换+交易记录系统 |
| v3.1 | 2026-07 | DataHub双源容灾 + 回测引擎 + 事件扫描 + 舆情分析 + 压力测试 + 板块轮动 |
| v3.2 | 2026-07 | 真实A股费率引擎 + filelock并发安全 + position_update |
| v3.3 | 2026-07 | position_close减仓摊薄成本 + 38命令全量 |
| **v4.0** | **2026-08** | **选股框架重写：五风格组分路由(周期/金融/成长/消费/稳定) + 110细分行业映射 + 历史分位数估值(5年窗口) + PEG(Cap=50%) + 版本戳[fv:hash8] + Nova 6条防御性补丁** |

---

## 📄 License

CC BY-NC-SA 4.0 (Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International) - 遵循 VCPDistributedServer 仓库协议，欢迎社区贡献与二次开发。

## 🙏 致谢

- [VCPToolBox](https://github.com/lioensky/VCPToolBox) - 插件宿主框架
- [AKShare](https://github.com/akfamily/akshare) - 开源金融数据接口
- [Tushare](https://tushare.pro/) - 金融数据社区
- [pandas-ta](https://github.com/twopirllc/pandas-ta) - 技术指标计算库