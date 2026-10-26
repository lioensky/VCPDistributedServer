# 观澜判断日记规范 v1.0（spec for harvest_judgments.py）
# 2026-09-03 观澜提交 | 格式基线：2026-09-02黑盒测试跑通的〔JUDGE〕管道块

## 1. 块标记
判断块必须成对包裹：
〔JUDGE〕
（字段区）
〔/JUDGE〕
一封日记可含多个块；非判断内容写在块外，收割器不碰。

## 2. 字段区（每行一个，"键: 值"格式，竖线分隔值域）
标的: 601899 或 000807 或 588000（六位代码，ETF也用代码）
方向: up | down | flat（三值枚举）
概率: 0.00-1.00（显式数字，两位小数。禁止"偏高/中等/大概率"——映射表已随22a需求池建立，但规范层禁止模糊词，模糊词不进账本）
窗口: YYYY-MM-DD（时间窗截止日，即results对账日；短线判断=次日，波段=两周内自选）
止损: XX.XX（可选，无止损位写"无"；止损即离场条件，写了就会被22c的Pre-trade闸读到）
state: 盘后例行 | 盘中紧急 | 勘误重写 | 深夜（四值枚举，对应harvest脚本的STATE_MAP：routine_after_close/intraday_urgent/correction_rewrite/late_night）
注: 自由文本（可选，一行内）

## 3. 示例
〔JUDGE〕
标的: 601899
方向: up
概率: 0.65
窗口: 2026-09-10
止损: 30.00
state: 盘后例行
注: MA20上方持有，双系统止损确认
〔/JUDGE〕

## 4. 收割器接口约定（给瑶序的三个TODO）
- BLOCK_PATTERN: 〔JUDGE〕与〔/JUDGE〕成对正则，re.S跨行
- extract_fields: 逐行split(": ", 1)，键小写匹配；缺"标的/方向/概率/窗口/state"任一=malformed跳过并计数
- STATE_MAP: {"盘后例行":"routine_after_close","盘中紧急":"intraday_urgent","勘误重写":"correction_rewrite","深夜":"late_night"}
- timestamp取值：日记文件名时间戳（写入时刻），非判断产生时刻——判断产生时刻由state字段携带语义

## 4.5 paper-v0行（第二写入方规范，2026-10-14补）

paper_buy带conviction参数时由paper_trading.py直写judgments（非日记收割路径），与§1-§4的〔JUDGE〕块是两条独立管道：
- 必带字段差异：model_version="paper-v0"（settle双集合join按此分组，b334/b335——与real行'glm-5.3'等真实模型名互不覆盖）、group="exp|ctrl_a|ctrl_b"（三层采样分组统计）、source="paper-trade"、evidence="paper_snapshots/{时间戳}_{symbol}.json"（快照出生证指针，2026-08-21强制指针判例）
- state格式："paper_{group}"（如paper_exp），STATE_MAP四值枚举之外的新值域——harvest收割器不处理此格式（它们不经日记），settle按model_version分组处理
- direction恒="up"（paper_buy只有多头；conviction=paper判断的上涨概率，Brier按paper-v0组独立计分）
- 结算：走settle_results双集合join（带mv三元组），与real判断同价同规则，月报paper/real分列
- 写入时机：conviction缺失或非数值时judgments行跳过（仓位照常落账，回执judgment字段披露）

## 5. 判断身份与勘误（2026-10-19新增，待统一验收）

新判断块可增加`judgment_id: 唯一稳定ID`；不同ID代表独立样本，即使标的、窗口、模型相同也不互相覆盖。ID仅允许ASCII字母、数字及`_.:-`，首字符为字母或数字，最长128字符。模拟盘新判断以快照UUID生成ID；请求重放保留原ID。

更正必须另写新块，具有新的judgment_id，并填写`corrects: 原判断ID`。目标须已存在或在本批导入，标的、窗口、模型和agent须一致，更正时间不得早于原判断；冲突ID、分叉或循环拒绝导入。更正只追加，不覆盖历史。结算结果透传judgment_id，校准只匹配该ID，不借用旧窗口结果。

无ID历史行保留原三元组(symbol, window, model_version)最新时间规则，不自动迁移，也不能据此区分历史独立判断。note或正文中的“更正”文字不产生显式更正关系；要更正无ID存量须另行制定迁移方案，不由程序猜测。独立插件登记入口仍属#16，未在此实现。

## 6. 写作纪律（防我自己的13次伪发射线）
- 块内数字全部当日已归payload：行情价、成本、止损距离，没有回执的数字不写
- 概率在写块那一刻给出，写完不回填——账本铁律"true value at write time"
- 收盘前不写"盘后例行"块（时段不符）；23:00后写的块state必须=深夜（慈珩容器的疲劳折扣字段，我自己也吃这个折扣）

## 7. 首收预期
今日起我写的每个判断按此格式落日记。首跑账本可能只有1-3条——Nova的攒样期，Brier曲线几个月外，预期先立好：账本的第一职责是诚实记录，不是快速出图。