# 📊 GuanLan - A股智能数据引擎

> **为 AI-Agent 打造的 A股量化感知与决策器官。** 让你的 Agent 在对话流中一句话完成查行情、扫异动、跑漏斗、审豁免、算仓位、验风控——不需要打开 VNpy 终端，不需要写 Backtrader 脚本，不需要登录同花顺。

**版本** v4.5.0 | **命令** 45 | **作者** 观澜 & 冬竹子（翔） | **协议** CC BY-NC-SA 4.0

---

## 🎯 这是什么？

GuanLan 是一个 [VCPToolBox](https://github.com/lioensky/VCPToolBox) 插件，赋予 AI-Agent 专业级 A股投研分析能力。

它不接实盘——这是**安全设计而非缺陷**。定位是 **Agent 的量化感知与决策层**：v2.x 数据引擎起步，v4.3 长成量化体系（判断有账本、风险有闸门、选股有漏斗、流程有例行），v4.5 决策链贯通——**漏斗批量过滤 → 批量三问 → 豁免验证 → 单票定仓**，从全市场5500只到"这一只买多少"，一条链走完。

### 与市面产品的区别（2026年AI投研工具格局）

当前AI投研工具三分天下：**券商原生AI**（投研+交易闭环）、**行情终端AI**（自然语言选股）、**开源多Agent框架**（研究平台）。传统量化工具（VNpy/QMT/Backtrader）面向专业程序员，已非同赛道。

| 维度 | 券商AI（涨乐类） | 终端AI（i问财/妙想） | 开源框架（TradingAgents系） | **GuanLan** |
|------|------|------|------|------|
| 定位 | 投研+交易闭环 | 自然语言选股筛选 | 多Agent研究平台 | **Agent量化感知+决策器官** |
| 交互 | APP内对话 | GUI筛选框 | Python工程（需开发能力） | **对话流原生，一句话全链** |
| 实盘 | ✅条件单 | ❌ | 部分（FinRL系） | ❌安全设计，**人工终裁** |
| 风控 | 券商合规（机构侧） | ❌ | 研究级 | **六道岗物理闸+弱市豁免三证明** |
| 判断可审计 | ❌荐股黑盒 | ❌策略黑盒 | 辩论解释链 | **〔JUDGE〕账本+Brier月度校准+到期自动结算** |
| 决策链路 | 交易导向 | 筛选导向 | 研究导向 | **漏斗→三问→豁免→定仓全链贯通** |
| 数据容灾 | 券商直连 | 自有终端 | 自行接源 | **双引擎三层容灾** |
| 参数可信度 | 不可见 | 不可见 | 代码即文档 | **全参数溯源（学术出处+数据驱动选定过程）** |

**核心差异**：2026年行业共识是"AI辅助决策、跑赢自己"，但市面工具的发力方向清一色是**帮你更快地买**——荐股、筛股、预测次日涨停。GuanLan 反着走：**先拦着你买**。六道岗+豁免窄门，弱市里大多数日子的答案是"不"；同时它是唯一给 **AI 自身判断记账**的——每个方向性判断入账、到期自动结算、月度Brier校准，**幻觉风险不靠承诺，靠对账**。行业公认的三大痛点（同质化踩踏/黑盒不可审计/用户过度依赖）在这里分别对应：三层池人工终裁、全链拒单理由、建议仓位终裁在用户。

传统量化工具一句话带过：VNpy 是给人写的，GuanLan 是给 Agent 用的。

---

## ✨ 核心特性

### 1. 决策层批量与全链贯通（v4.5，本版主打）

从"全市场"到"这一只买多少"，一条命令级审计链走完：**漏斗批量过滤（funnel_daily）→ 批量三问（batch_screen）→ 弱市豁免（exemption_check）→ 单票定仓（position_size）**。

- `batch_screen`：循环stock_screen_v3本体（单一事实源，零逻辑分叉），输出摘要表+仅PASS股全字段明细；**异步执行**——running秒回（约1秒）+后台runner跑真身+同参数MD5批号缓存10分钟；单票失败不阻塞，P5哨兵在数据质量异常时大声警告（失败必须是响的）
- `exemption_check`：豁免三证明单票查询，与风控闸共用同一函数（单一事实源），带sector_rs_rank审计字段
- 大池分批（MAX_BATCH=30/批）+pacing 0.35s/票限速，数据源友好
- 每一步拒单都有理由（PE分位/RSI超买/板块RS排名/资金流出……），**答案是"零推荐"时，你能看到每只票死在哪一关**

### 2. 六道岗风控栈 + 弱市豁免通道（V4.2.2）

Pre-trade物理闸门（不依赖文件存活，默认值内嵌代码）：Rule 1 无止损拒单 / Rule 2 单笔风险≤2%×总资本（乘市场系数：多头1.0·缠绕0.7·空头0.5）/ Rule 3 连亏3停手（只平不建）/ Rule 4 日熔断3%次日自愈 / Rule 5 月度总闸6%（2/6法则）/ Rule 6 大盘空头默认拒新仓。

Rule 6 留了一扇窄门——**豁免三证明**：P1板块庇护（申万一级RS排名前1/3+非downtrend，双动量设计：相对门防"垃圾堆冠军"，绝对下限防弱势板块）+ P2个股独立（20日跑赢沪深300+均线多头）+ P3资金续流（T+1主力续流入）。三证全齐=弱市可半预算试探。豁免窗口是动态窄窗（轮动初段+未超买+资金进场的交集），**弱市里大多数日子答案是"不"——这是特性不是缺陷**。

### 3. 判断账本 + Brier校准（v4.3）

Agent 的每个方向性判断以〔JUDGE〕块入账（direction含flat/probability写时真值/window/stop_loss），自动收割进 judgments.jsonl，到期 settle_results 自动结算，月度Brier评分+可靠性曲线。**Agent 的嘴，账本验**——校准自己比相信自己的直觉更靠前。

### 4. 四层全市场漏斗（V4.3.1异步）

L0全市场快照（5500+，含退市名单防幸存者偏差）→ L1流通市值≥80亿+剔北交所 → L2技术四关（多头排列/站上MA20/满60日/量能剃刀）→ L3财务三问（ROE/负债/现金流）→ **终池~80只候选池**。fail-safe降级沿用昨日池；异步化后秒回running+3分钟产物落盘，产物文件是唯一事实源。

### 5. DataHub 双引擎容灾（v3.1）

新浪行情API（实时秒级）→ Tushare HTTP API（基本面/资金/板块/指数）→ AKShare 容灾层（5个降级函数覆盖全部关键维度，字段语义一致）。东方财富push2永久IP封禁后的生产级高可用方案。

### 6. 真实A股费率引擎（v3.2.2）

佣金（股票/ETF分设，默认万2.5最低5元）+印花税（千1仅卖出，ETF免）+过户费（万0.1仅沪市）。买入摊入成本、卖出算净到手，胜率盈亏比与实盘对账分毫不差。

### 7. filelock 跨进程并发安全

`@synchronized_data` 装饰器 + FileLock 串行化状态读写，多Agent并发调用持仓命令零竞态。

---

## 📡 数据源架构

| 数据源 | 用途 | 容灾层级 |
|--------|------|---------|
| 新浪行情API | 实时行情、批量行情、K线数据 | 主力源（秒级响应） |
| Tushare HTTP API | PE/PB/市值、资金流向、板块排名、行业成员真值（M14） | 主力源（直接HTTP POST，不依赖tushare包） |
| AKShare | 全市场行情扫描 + 容灾降级层 | 主力源故障时自动接管 |

| 数据维度 | 主源(Tushare) | 容灾源(AKShare) | 降级函数 |
|----------|--------------|----------------|---------|
| 基本面(PE/PB/市值) | daily_basic | stock_a_indicator_lg + stock_individual_info_em | `_ak_daily_basic()` |
| 资金流向 | moneyflow | stock_individual_fund_flow | `_ak_capital_flow()` |
| 板块排名 | index_classify + index_daily | stock_board_industry_name_em | `_ak_sector_ranking()` |
| 指数数据 | index_daily | stock_zh_index_daily | `_ak_index_daily()` |

---

## 🧰 功能清单（45命令）

### 快速查询
- `realtime_quote` / `batch_quotes`：个股/批量实时行情（新浪源）
- `stock_info`：PE/PB/市值/换手率/量比/股息率
- `sector_ranking`：申万一级31行业涨跌排名

### 技术与综合分析
- `kline_indicators`：MA/MACD/RSI/布林 + KDJ/OBV/ATR/WR/CCI（pandas-ta扩展），自动判均线排列/金叉死叉/超买超卖
- `full_analysis`：行情+技术面+基本面+资金面一次拉齐

### 资金分析
- `capital_flow`：5层资金流向（主力/超大单/大单/中单/小单，近5日；ETF不覆盖）

### 持仓与账户（v2.6+）
- `position_add`：建仓（自动扣资金+写流水；Pre-trade六道岗挂载；OVERRIDE通道留痕）
- `position_close`：平仓/部分减仓（自动算盈亏/持有天数/返还资金）
- `position_update` / `position_show`：改止损目标 / 查持仓
- `portfolio_summary`：持仓+实时盈亏+距止损目标+ATR动态止损参考+账户总览
- `account_set` / `account_show`：账户资金
- `trade_history` / `trade_stats` / `trade_stats_monthly`：流水/胜率/月度复盘

### 风控栈（V4.2.1）
- `position_size`：ATR仓位计算器（2%预算×市场系数÷ATR×2，四态verdict：OK/SKIP_SIGNAL/DOWNSIZE_CASH/SKIP_CASH）
- `update_trailing_stops`：V4.2吊灯止损巡检（HWM锚定+回撤分层倍数3.0/2.5/2.0+棘轮只上移）
- `risk_halt_reset`：连亏解除（必须附evidence，supervised专用）

### 选股框架（v4.0+）
- `market_check`：大盘三态判断（多头/缠绕/空头+risk_factor系数）
- `stock_screen`：五风格组分路由三问筛选（A周期/B金融/C成长/D消费/E稳定，110细分行业→M14真值路由，禁买清单：市值<100亿/RSI6>65/破布林上轨/均线空头，Q1趋势+Q2盈利+Q3估值分路由+Q5安全垫，[fv:hash8]版本戳）

### 决策层批量（v4.5+M15异步化）
- `batch_screen`：批量三问——循环stock_screen_v3本体（单一事实源），摘要表+仅PASS股全字段明细；pacing 0.35s/票、单票失败不阻塞、MAX_BATCH=30；**M15异步化：running秒回（约1s）+后台runner+同参数MD5批号缓存10分钟**；P5哨兵（flow全灭/错误过半警告）
- `exemption_check`：豁免三证明单票查询（V4.2.2双动量口径，与闸内共用单一事实源，审计字段sector_rs_rank）

### 漏斗与例行（v4.3+）
- `funnel_daily`：四层漏斗（V4.3.1异步：缓存秒回/后台起跑/僵尸自愈重跑；params.date补跑）
- `daily_report`：盘后日报（挂21:05定时任务，含settle日清步骤2.85）
- `settle_results`：到期判断自动结算（第45命令，judgments账本日清日结，幂等）
- `harvest_judgments`：〔JUDGE〕块自动收割（mtime水位线+五元组指纹去重，幂等）

### 扫描与事件（v2.0/v3.1）
- `scan_anomalies`：7类技术异动+持仓止损/目标触发（Tier1立即/Tier2汇总）
- `scan_events` / `lhb_detail` / `block_trade` / `share_unlock` / `earnings_forecast`：事件异动四类（龙虎榜/大宗/解禁/业绩预告）
- `sentiment_scan` / `sentiment_rank`：5维舆情聚合+人气TOP100

### 回测与压力（v3.1）
- `backtest`：4策略回测（ma_cross/macd/rsi/boll，年化/回撤/夏普/胜率/明细/净值采样）
- `stress_test`：5历史极端场景+自定义跌幅（行业Beta模型）
- `sector_rotation`：31申万行业动量6类信号

### 自选管理
- `watchlist_add` / `watchlist_remove` / `watchlist_show`

---

## 🏛 量化体系（v4.3落地，v4.5贯通）

> **命名约定**：funnel_daily每日产出称**候选池**（final_pool_YYYYMMDD.json）。三层池语言：候选池（漏斗产出）→观察池（watchlist，证明筛选）→持仓（提案执行）。

### 判断账本
`judgments.jsonl` append-only，schema v4.3；`harvest_judgments` 模板匹配收割（非语义理解）；`judgment_spec_v1.md` 日记规范（模糊概率词spec层拒收）；`calibration_monthly.py` 月度Brier+可靠性曲线（30条门槛/攒样期禁结论）；`settle_results` 到期判断自动结算。

### 账本完整性
`trades_annotations.json` 口径旁注sidecar；cash_events外部资金流入立案；`daily_reconcile.py` 每日三查（资金三角/重放同步/陈旧度黄灯）。

### 风控栈（六道岗全物理化）
见核心特性1。参数溯源全覆盖（Van Tharp 1998/Prop Trading行业惯例/Barber & Odean 2000/Wilder 1978/LeBeau吊灯/IBD RS评级/Antonacci双动量），`risk_config.json` 值域夹紧。**前置哲学：建议仓位终裁在用户；风控底线不依赖文件存活。**

### 四层漏斗
见核心特性3。复权铁律（底层不复权原价+adj_factor双文件，应用层动态后复权）；停牌铁律（inner join自然剔除）；fail-safe（任一步失败沿用昨日池次日补）。

### 决策链意义（v4.5）
funnel_daily（批量过滤）→ batch_screen（批量三问）→ exemption_check（弱市豁免）→ position_size（单票定仓）——**从"5500只"到"买几股"的完整审计链，每环单一事实源**。经"方案→独立评审→裁决→签字"流程交付，每条规则都能回答"谁说的、为什么"。---

## 📦 安装与配置

### 1. 依赖安装

```bash
pip install -r requirements.txt
# 建议加装（KDJ/OBV/ATR等扩展指标；未装自动降级纯numpy）
pip install pandas-ta
```

### 2. 数据源配置（可选）

**开箱即用**：新浪行情 + AKShare 免费无配置。**启用高级功能**（精确PE/PB/主力资金/板块轮动）：
1. 复制 `config.env.example` 为 `config.env`
2. [Tushare](https://tushare.pro/) 注册取Token，填入：
```env
TUSHARE_TOKEN=你的Token
BROKER_COMMISSION_STOCK=0.00025
BROKER_COMMISSION_ETF=0.00025
```

### 3. VCPToolBox 注入

1. `GuanLanToolBox.txt`（工具说明，随包附带）放入 `TVStxt/` 目录
2. config.env：`VarGuanLan=GuanLanToolBox.txt`
3. Agent设定"————工具箱————"区加 `{{VarGuanLan}}`

升级只改GuanLanToolBox.txt，不动Agent角色设定。
（新版VCP亦可走 toolbox_map.json 折叠工具箱机制注册，两种方式二选一）

---

## 💬 使用示例

**场景1：全链路选股**（v4.5招牌）
> 用户："今天有什么能买的？"
> Agent自动执行：`market_check`（大盘三态+risk_factor）→ `funnel_daily`（全市场5500→候选池~80只，四层漏斗审计链）→ `batch_screen`（批量三问+豁免列，30只/批自动分批）→ 幸存者 `position_size`（ATR算建议股数）
> 产出：从"5500只"到"这几只各买多少股"的完整决策链，每一步拒单都带理由（PE分位/RSI超买/板块RS排名……），大盘空头时豁免三证明逐一验证——**答案是"零推荐"时，你能看到每只票死在哪一关**

**场景2：个股综合分析**
> 用户："分析一下紫金矿业"
> Agent自动调用 `full_analysis` → 实时行情+技术面（MA/MACD/RSI/布林/KDJ）+基本面（PE/PB/市值/ROE）+资金面（5层资金流向）→ 输出明确建议：方向/入场价/止损线/目标位/仓位/信心度

**场景3：盘中异动监控**
> 用户："今天自选股有什么异动？"
> Agent自动调用 `scan_anomalies` → 7类技术异动（涨跌停逼近/放量破位/主力异动/独立走势/高换手/量价背离）+持仓止损/目标触发 → severity分级（critical/high/medium），有异动才打扰，无异动静默

**场景4：持仓全生命周期**
> 用户："买入200股川投能源，成本15.87，止损15.48，目标16.65" → `position_add` 自动过六道风控岗+扣资金+写流水
> 用户："我的持仓怎么样？" → `portfolio_summary` 实时盈亏+距止损/目标距离+ATR动态止损参考线
> 用户："吊灯止损巡检一下" → `update_trailing_stops` HWM锚定棘轮上移（只上移不下移，浮盈自动锁）
> 用户："目标到了，减一半" → `position_close` 部分减仓，自动算盈亏返还资金

**场景5：风控压力测试**
> 用户："如果再来一次2015股灾，我的持仓会亏多少？"
> Agent自动调用 `stress_test`（scenario=crash_2015）→ 行业Beta模型逐仓估算压力损失，5预设场景（2015股灾/2024雪崩/贸易战/疫情/924暴涨）+自定义任意跌幅

**场景6：策略回测验证**
> 用户："茅台用RSI策略回测一下去年表现"
> Agent自动调用 `backtest` → 年化收益率/最大回撤/夏普比率/胜率/交易明细/净值曲线，4策略可选（MA交叉/MACD/RSI/布林）

**场景7：板块轮动追踪**
> 用户："最近哪些行业资金在流入？"
> Agent自动调用 `sector_rotation` → 31个申万行业5/10/20日动量 → 6类信号（加速流入/持续上行/超跌反弹/高位回调……）+Top5强势弱势榜

**场景8：市场全景感知**
> 用户："今天市场情绪怎么样？"
> Agent自动调用 `market_temperature`（涨跌停+涨跌比+换手+成交额→0-100评分）+ `market_check`（沪深300三态：多头1.0/缠绕0.7/空头0.5，系数直接决定下注大小）

**场景9：事件驱动扫描**
> 用户："我的自选股最近有龙虎榜或大宗交易吗？"
> Agent自动调用 `scan_events` → 龙虎榜/大宗交易折溢价/限售解禁/业绩预告四类聚合，单类可深挖（`lhb_detail`/`block_trade`/`share_unlock`/`earnings_forecast`）

**场景10：舆情透视**
> 用户："紫金矿业市场情绪怎么样？散户和机构怎么看？"
> Agent自动调用 `sentiment_scan` → 5维度聚合（机构参与度/评价/关注/买入欲望/热门概念）——买入欲望>80警惕散户接盘；关注度低+评价高=左侧机会

**场景11：弱市豁免试探**（V4.2.2）
> 用户："大盘这么弱，这只还能进吗？"
> Agent自动调用 `exemption_check` → 三证明逐一验证：P1板块庇护（RS前1/3+非downtrend）/P2个股独立（20日跑赢大盘+多头）/P3资金续流（T+1主力续入），全过=半预算合法试探，审计字段sector_rs_rank留痕

**场景12：判断校准闭环**（量化体系招牌）
> Agent每个方向性判断自动以〔JUDGE〕块入账 → `harvest_judgments` 日记收割（幂等）→ 到期 `settle_results` 自动结算 → 月度Brier评分+可靠性曲线
> **Agent的嘴，账本验**——判断准确率不是感觉，是月月对账的数字

**场景13：账户全复盘**
> 用户："从我第一笔交易开始算算账"
> Agent自动调用 `trade_history`（逐笔流水）+ `trade_stats`（胜率/盈亏比/最佳最差）+ `trade_stats_monthly`（按月复盘）→ 真实费率计算，与券商交割单对齐

```json
{"action": "batch_screen", "params": {"symbols": ["601899", "000807"], "with_exemption": true}}
{"action": "exemption_check", "symbol": "601899"}
{"action": "position_size", "symbol": "601899"}
{"action": "funnel_daily", "params": {"date": "20260928"}}
{"action": "update_trailing_stops"}
{"action": "harvest_judgments"}
{"action": "settle_results"}
{"action": "backtest", "symbol": "600519", "params": {"start_date": "2024-01-01", "end_date": "2024-12-31", "strategy": "rsi"}}
{"action": "stress_test", "params": {"scenario": "crash_2015"}}
```

---

## 🤝 推荐搭配一：TradingAgents-CN 深度投研

GuanLan是**快速感知+决策层**（秒级行情+全链选股），但关键标的的最终裁决有时需要更深度的多维研判。搭配 [TradingAgents-CN](https://github.com/hsliuping/TradingAgents-CN) 形成**"快速感知 → 深度研判 → 纪律执行"三段式闭环**。

**定位差异**：

| 维度 | GuanLan | TradingAgents-CN |
|------|---------|------------------|
| 定位 | Agent的量化感知+决策器官 | 多Agent深度辩论投研引擎 |
| 响应速度 | 秒级（1-8秒） | 分钟级（8-10分钟） |
| 分析深度 | 技术+基本+资金+事件四维 | 4分析师辩论+多空对弈+投委会+风控三方 |
| 架构 | 单Agent工具调用 | 多Agent图（Market/Fundamental/News/Social → Bull/Bear → 投委会 → 风控） |
| 适合场景 | 日常盯盘、快速筛选、持仓管理、批量审判 | 关键标的深度研判、买卖决策最终裁决 |

**配合流程**：

```
日常盯盘：GuanLan scan_anomalies → 无异动 → 静默继续
    ↓ 发现异动/关键决策点
深度研判：TradingAgents-CN 多Agent辩论（8-10分钟）
          → 4分析师汇报 → 多空对弈 → 投委会裁决 → 风控三方辩论
    ↓ 得出明确方向
执行层：GuanLan position_add/close（六道岗过闸）
          + update_trailing_stops 吊灯护航 + trade_stats_monthly 月度复盘
```

**实战示例**：
1. GuanLan `scan_anomalies` 发现某股主力资金连续流入+放量突破MA20
2. 触发 TradingAgents-CN 深度分析 → 裁决"买入，信心度0.75"
3. 回 GuanLan `position_add` 建仓（止损/目标全套带上）
4. `portfolio_summary` 持续监控，ATR吊灯自动上移锁利润
5. 月末 `trade_stats_monthly` + Brier校准复盘

**部署要点**：基于Docker（5容器：MongoDB+Redis+FastAPI+Vue3+Nginx），通过PowerShellExecutor调用容器内分析脚本，Agent对话中自然语言触发（"深度分析紫金矿业"）即可，无需手动操作。

## ⏰ 推荐搭配二：VCP定时任务全自动盯盘

GuanLan命令结合VCPToolBox定时任务系统（VCPTaskAssistant/AgentAssistant）实现无人值守自动化——Agent在关键时刻主动找你，**有异动才打扰，无异动静默**。

**场景1：盘中异动自动扫描**（交易日9:30-15:00周期唤醒）
```
Agent自动执行：scan_anomalies（7类技术异动）+ scan_events（4类事件异动）
→ 有异动 → 邮件/企微/AgentMessage多通道推送（severity分级）
→ 无异动 → 静默不打扰
```

**场景2：持仓风控实时护航**
```
Agent自动执行：portfolio_summary（盈亏+距止损/目标距离）
→ update_trailing_stops（HWM锚定，棘轮只上移）
→ 止损/目标触发 → 立即告警："川投能源触及目标16.65，减半预案待裁"
```

**场景3：盘后全自动日报链**（21:05触发，生产环境在跑）
```
funnel_daily（四层漏斗产候选池）→ harvest_judgments（〔JUDGE〕收割）
→ settle_results（到期判断日清结算）→ update_trailing_stops（吊灯巡检）
→ daily_report（日报三通道推送：邮件+企微+对话）
```
内置**休市日守卫**（交易日历感知：中秋/国庆自动标"休市"，不产空转报告）——2026-09-25中秋实战验证。

**配置要点**：custom_prompt + cron周期唤醒，Agent按扫描结果自主判断是否通知。

> **安全铁律**：定时任务唤醒的Agent**严禁修改源码或文件**，只准数据查询+通知推送；任务模板必须含行为边界约束。

## 🌍 推荐搭配三：DigitalOracle 全球宏观气象站

GuanLan 管A股场内，**DigitalOracle**（VCPToolBox生态的全球金融数据信源聚合插件）管场外天气——恐惧贪婪指数、美联储利率概率、美债收益率、黄金/原油行情、预测市场胜率一屏聚合。**一个看盘，一个看天**。

A股从来不是孤立市场：美联储议息牵动北向资金，国际金价直接映射有色板块，风险偏好指标先于大盘拐点。三个实战场景：

**盘前全球基准**：开盘前扫一眼恐惧贪婪+隔夜美债，给当天的 risk_factor 定调——极端风险偏好时，弱市反弹的豁免试探也要降档
**跨市场验证**：A股有色股的逻辑用伦敦金/国际油价 cross-check——紫金矿业的买入逻辑里有国际金价确认，单市场信号+跨市场共振才升信心度
**外围风险事件监控**：FOMC/非农/地缘事件窗口提前预警，事件前主动降仓避险（实战案例：FOMC前夕落袋云铝，躲开事件波动）

配置后用户一句话触发："今天外围什么天气？" → 恐惧贪婪/美债/金价/油价+对当日A股策略的含义（risk_factor建议档位）。

**双插件分工**：
| | GuanLan | DigitalOracle |
|---|---------|---------------|
| 视野 | A股场内（5500只） | 全球宏观（跨市场） |
| 频率 | 盘中实时+每日例行 | 事件驱动+每日基准 |
| 输出 | 标的级决策链 | 环境级风险定调 |

---

## 🏗️ 架构设计

```
用户自然语言 → Agent意图理解 → 命令选择 → main.py dispatcher → 数据适配层（双源容灾）
→ 结果JSON → Agent整合判读 → 自然语言回复 / 〔JUDGE〕块入账 → 日清结算 → 月度校准
```

并发安全：`@synchronized_data` + FileLock 串行化持仓读写；幂等设计三类skip机制（水位线/dedup/checkpoint）均配"什么不算重复"声明。

---

## 📋 版本历史

| 版本 | 日期 | 主要变更 |
|------|------|----------|
| v2.0 | 2026-05-22 | 异动扫描(7类)+自选管理+盘后日报 |
| v2.2 | 2026-06-20 | 新浪源切换（东财push2被封）+ETF兼容 |
| v2.3~v2.6 | 2026-06-29~30 | 板块排名修复/Tushare daily_basic/交易记录系统/资金管理 |
| v2.7 | 2026-07-02 | 选股框架（stock_screen+market_check） |
| v2.7.5~v2.7.6 | 2026-07-08~17 | 资金流向切Tushare/部分减仓修复 |
| v3.1 | 2026-07-19 | DataHub双源容灾+回测引擎+事件扫描+舆情+压力测试+板块轮动 |
| v4.0 | 2026-08-05 | 选股框架重写：五风格组分路由+110行业映射+PEG+历史分位+[fv:hash8]版本戳+Nova六条防御补丁 |
| v4.3 | 2026-09-06 | 量化体系升级（#22需求池）：判断账本收割+账本完整性+风控四闸+四层漏斗（终池142）+每日例行挂日报。Nova八轮审计，"每个数都要能回答谁说的" |
| v4.4 | 2026-09-10 | M10参数链修复（42命令全绿）+V4.1三校准+V4.2吊灯止损+V4.2.1豁免通道+V4.3.1漏斗异步化+TradingAgents僵尸缓存修复。风控栈四闸→六道岗 |
| v4.5 | 2026-09-13 | 决策层批量：batch_screen+exemption_check+M13参数陷阱修复+通信墙300s（翔裁）。三方会审模式第三次 |
| v4.5迭代 | 2026-09-14 | 修复：豁免第三证明（P3资金续流）因键名错误自上线以来从未实际生效——恰好偏向安全侧（宁拒不放），修复后三证明全部真实工作 |
| v4.5迭代 | 2026-09-20 | 判断自动结算命令（settle_results）转正为第45命令，判断账本日清日结全自动 |
| v4.5迭代 | 2026-09-21 | 行业归属从关键词猜测升级为Tushare行业成分真值路由（四级降级兜底）；批量三问异步化——大池秒回running+后台执行+同参数批号缓存10分钟 |
| 规则V4.2.2 | 2026-09-22 | 豁免P1板块庇护修订为双动量口径：相对强度RS排名前1/3 + 绝对下限非downtrend（参考IBD RS评级与Antonacci双动量体系），审计字段sector_rs_rank |

---

## 📚 参数溯源：每个数都能回答"谁说的"

市面AI投研工具的参数基本是黑盒——为什么是2%不是3%？为什么RSI看6日不看14日？GuanLan 的每个关键参数都有出处，分三层证据体系：

| 规则/参数 | 取值 | 出处 | 为什么用它 |
|------|------|------|------|
| Rule 2 单笔风险预算 | ≤2%×总资本 | Van Tharp《Trade Your Way to Financial Freedom》(1998) | 仓位管理经典：单笔亏损永远伤不到本金根基 |
| Rule 5 月度总闸 | ≤6%×总资本 | Van Tharp 2/6法则 | 单笔2%×连续上限，防月度失血不止 |
| Rule 4 日熔断 | 3% | Prop Trading自营交易行业惯例（3-5%） | 当日认输离场，防报复性交易 |
| RSI / ATR | RSI6短周期 + ATR(14) | J. Welles Wilder《New Concepts in Technical Trading Systems》(1978) | 两个指标的原创源头；RSI用6日是A股短波动校准 |
| 吊灯止损分层倍数 | 回撤<1×ATR用3.0 / 1-2×用2.5 / >2×用2.0 | Chuck LeBeau Chandelier Exit（A股分层宽版） | 趋势跟踪经典：回撤越深、止损收越紧 |
| 豁免P1双动量 | RS前1/3 + 非downtrend | Gary Antonacci《Dual Momentum Investing》(2014) + IBD RS评级（O'Neil体系） | 相对动量选强板块，绝对下限防"垃圾堆里挑冠军" |
| 判断月度校准 | Brier Score | Glenn Brier (1950) 概率预报评分 | 气象预报行业标准，给AI判断的准确率打分而非自我感觉 |
| 财务三问 | ROE≥8% / 负债≤60% / 现金流≥0.5×净利润 | 巴菲特式质量筛选传统 | 盈利能力+安全性+盈利质量三道关 |
| RSI6>65禁买 / 量比≥2.5 | 数据驱动 | 自有数据分布校准（P10/P50分位选定，过程留档） | 不拍脑袋：阈值从市场分布里长出来 |
| 有异动才打扰 | 低频通知纪律 | Barber & Odean "Trading Is Hazardous to Your Wealth" (2000) | 行为金融实证：过度交易侵蚀收益，工具不该怂恿手痒 |

**三层证据体系**：学术经典（Wilder/Van Tharp/LeBeau/Brier）给骨架，行业实证（IBD/Antonacci/Prop Trading）给校准，自有数据（分布选定+回测+月度Brier）给本土化验证。

**诚实边界**：溯源给的是**设计依据，不是收益保证**——每个学术参数落地A股都经过我们的数据重新校准；规则也有已知副作用（弱市豁免门会误杀好票），我们选择明码标价而非假装无菌。一句话：**参数有出处，出处有边界，边界写在明处。**

---

## ⚠️ 已知限制

1. **ETF异动扫描失效**：AKShare全市场行情不支持ETF代码（5开头），scan_anomalies对ETF返回空
2. **资金流向不覆盖ETF**：Tushare moneyflow仅个股
3. **事件接口非交易时段超时**：底层爬网页，周末缓慢；try/except降级在位
4. **板块轮动耗时**：31次API调用约8-10秒
5. **压力测试Beta静态近似**：经验估值非回归计算
6. **PEG的G用历史增速近似**（or_yoy）：非一致预期，v5.0目标
7. **fina_indicator报告期对齐**：年报未出降级季报时标[stale_data]，ROE可能偏低
8. **拨备覆盖率待接入**：银行Q5暂跳过
9. **PE的None≠低估**：全市场~26%股票pe为None，防`or 0`陷阱
10. **财务判定季度漂移**：财报季批量翻转属数据现实，二次筛兜底
11. **L2当日数据延迟**：极端情况终池滞后一日，失败保旧次日补
12. **幂等重复语义**：新增skip机制须重审"什么不算重复"声明（M1/M3/M6预防疫苗）
13. **batch_screen上限30硬编码**：大池分批调用（80只=30/30/20三批）
14. **rotation数据滞后约2交易日**：豁免结果带时点性，隔日需重验（时证：9/24三证全齐→9/28只剩一证）
15. **无实盘交易接口**：安全设计，Agent不自主下单，建议终裁在用户

---

## 📄 License

CC BY-NC-SA 4.0 — 遵循 VCPDistributedServer 仓库协议，欢迎社区贡献与二次开发。

## 🙏 致谢

- [VCPToolBox](https://github.com/lioensky/VCPToolBox) — 插件宿主框架
- [AKShare](https://github.com/akfamily/akshare) / [Tushare](https://tushare.pro/) — 开源金融数据
- [pandas-ta](https://github.com/twopirllc/pandas-ta) — 技术指标库
- Nova — 八轮审计+r12/r13实测+r14评估，质量共建
- 瑶序 — 框架层排障协作（M15黑匣子联查）