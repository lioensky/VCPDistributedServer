# -*- coding: utf-8 -*-
"""
观澜 Plugin A - A股数据引擎 (v4.5)
v4.5: 决策层批量batch_screen+豁免查询exemption_check+settle_results日清 (2026-09-13/20, #27三方会审)
v4.3: 判断账本收割+风控四闸+四层漏斗+每日例行 (2026-09-06, #22)
v3.2: 市场温度计+月度复盘+ATR跟踪止损+ETF适配+filelock跨进程锁
v3.1: DataHub双源容灾+回测引擎+事件异动+舆情分析+压力测试+板块轮动
v2.x: 新浪源+Tushare API+异动扫描+自选股+持仓管理+选股框架
"""

_PTA_AVAILABLE = False
try:
    import pandas_ta as ta
    _PTA_AVAILABLE = True
except ImportError:
    pass

import sys
import json
import time
import os
import traceback
from datetime import datetime, timedelta
from filelock import FileLock

import akshare as ak
import pandas as pd
import numpy as np

sys.stdout.reconfigure(encoding='utf-8')

PLUGIN_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_LOCK = FileLock(os.path.join(PLUGIN_DIR, "guanlan.lock"))

def synchronized_data(func):
    """跨进程文件锁装饰器：防止并发调用导致的JSON读写竞态"""
    def wrapper(*args, **kwargs):
        with DATA_LOCK:
            return func(*args, **kwargs)
    return wrapper

WATCHLIST_PATH = os.path.join(PLUGIN_DIR, "watchlist.json")
POSITIONS_PATH = os.path.join(PLUGIN_DIR, "positions.json")
TRADES_PATH = os.path.join(PLUGIN_DIR, "trades.json")
ACCOUNT_PATH = os.path.join(PLUGIN_DIR, "account.json")


def log(msg):
    print(f"[GuanLan] {msg}", file=sys.stderr, flush=True)


def safe_request(func, *args, retries=1, delay=0.5, **kwargs):
    for attempt in range(retries + 1):
        try:
            time.sleep(0.5)
            result = func(*args, **kwargs)
            return result
        except Exception as e:
            if attempt < retries:
                log(f"重试{attempt+1}: {e}")
                time.sleep(delay)
            else:
                raise e


# ========== 新浪数据源适配层 ==========

import requests as _req

def _sina_prefix(symbol):
    """根据股票代码返回新浪前缀"""
    if symbol.startswith(('sh', 'sz', 'bj')):
        return symbol
    if symbol.startswith(('6', '9', '5')):
        return f"sh{symbol}"
    elif symbol.startswith(('0', '3')):
        return f"sz{symbol}"
    elif symbol.startswith(('4', '8')):
        return f"bj{symbol}"
    else:
        return f"sh{symbol}"


def _sina_realtime(symbol):
    """新浪API获取单只股票实时行情"""
    headers = {'Referer': 'https://finance.sina.com.cn', 'User-Agent': 'Mozilla/5.0'}
    code = _sina_prefix(symbol)
    r = _req.get(f'https://hq.sinajs.cn/list={code}', headers=headers, timeout=10)
    r.encoding = 'gbk'
    data = r.text.split('"')[1].split(',')
    if len(data) < 10:
        return None
    name = data[0]
    open_p = float(data[1]) if data[1] else 0
    prev_close = float(data[2]) if data[2] else 0
    price = float(data[3]) if data[3] else 0
    high = float(data[4]) if data[4] else 0
    low = float(data[5]) if data[5] else 0
    volume = float(data[8]) if data[8] else 0
    amount = float(data[9]) if data[9] else 0
    pct_chg = round((price - prev_close) / prev_close * 100, 2) if prev_close > 0 else 0
    amplitude = round((high - low) / prev_close * 100, 2) if prev_close > 0 else 0
    return {
        "代码": symbol,
        "名称": name,
        "最新价": price,
        "涨跌幅": pct_chg,
        "成交额": amount,
        "振幅": amplitude,
        "最高": high,
        "最低": low,
        "昨收": prev_close,
        "今开": open_p,
        "成交量": volume,
    }


def _sina_batch_quotes(symbols):
    """新浪API批量获取实时行情"""
    # 修复：兼容字符串格式的symbols（逗号分隔 → 列表）
    if isinstance(symbols, str):
        symbols = [s.strip() for s in symbols.split(',') if s.strip()]
    elif not isinstance(symbols, list):
        symbols = list(symbols) if symbols else []
    headers = {'Referer': 'https://finance.sina.com.cn', 'User-Agent': 'Mozilla/5.0'}
    results = []
    batch_size = 80
    for i in range(0, len(symbols), batch_size):
        batch_syms = symbols[i:i+batch_size]
        codes = [_sina_prefix(s) for s in batch_syms]
        query = ','.join(codes)
        try:
            r = _req.get(f'https://hq.sinajs.cn/list={query}', headers=headers, timeout=15)
            r.encoding = 'gbk'
            lines = r.text.strip().split('\n')
            for j, line in enumerate(lines):
                try:
                    if j >= len(batch_syms):
                        break
                    sym = batch_syms[j]
                    parts = line.split('"')
                    if len(parts) < 2:
                        continue
                    data = parts[1].split(',')
                    if len(data) < 10:
                        continue
                    name = data[0]
                    prev_close = float(data[2]) if data[2] else 0
                    price = float(data[3]) if data[3] else 0
                    pct_chg = round((price - prev_close) / prev_close * 100, 2) if prev_close > 0 else 0
                    results.append({
                        "代码": sym,
                        "名称": name,
                        "最新价": round(price, 2),
                        "涨跌幅": pct_chg,
                    })
                except:
                    continue
        except:
            continue
        time.sleep(0.3)
    return results


def _sina_kline(symbol, datalen=120):
    """新浪API获取日K线数据（秒级响应，替代AKShare盘中卡死问题）"""
    headers = {'Referer': 'https://finance.sina.com.cn', 'User-Agent': 'Mozilla/5.0'}
    code = _sina_prefix(symbol)
    url = f'https://money.finance.sina.com.cn/quotes_service/api/json_v2.php/CN_MarketData.getKLineData?symbol={code}&scale=240&ma=no&datalen={datalen}'
    r = _req.get(url, headers=headers, timeout=10)
    data = json.loads(r.text)
    if not data:
        return None
    df = pd.DataFrame(data)
    for col in ['open', 'high', 'low', 'close', 'volume']:
        df[col] = pd.to_numeric(df[col], errors='coerce')
    df.rename(columns={'day': 'date'}, inplace=True)
    return df


def _get_spot_data():
    """获取全市场实时行情（新浪源，兼容东财字段格式）"""
    try:
        df = safe_request(ak.stock_zh_a_spot)
        if df is None or df.empty:
            return None
        df = df.copy()
        df['代码'] = df['代码'].astype(str).str.strip()
        for col in ['最高', '最低', '昨收', '最新价']:
            if col in df.columns:
                df[col] = pd.to_numeric(df[col], errors='coerce').fillna(0)
        prev_close = df['昨收'].replace(0, float('nan'))
        df['振幅'] = ((df['最高'] - df['最低']) / prev_close * 100).round(2).fillna(0)
        if '量比' not in df.columns:
            df['量比'] = 0
        if '换手率' not in df.columns:
            df['换手率'] = 0
        if '流通市值' not in df.columns:
            df['流通市值'] = 0
        return df
    except Exception as e:
        log(f"全市场行情获取失败(新浪源): {e}")
        return None


# ========== Tushare HTTP API适配层 ==========

TUSHARE_TOKEN = os.environ.get("TUSHARE_TOKEN", "")


def _tushare_api(api_name, params, fields=''):
    """Tushare HTTP API封装（不依赖tushare包）"""
    try:
        r = _req.post('http://api.tushare.pro', json={
            'api_name': api_name,
            'token': TUSHARE_TOKEN,
            'params': params,
            'fields': fields
        }, timeout=15)
        d = r.json()
        if d.get('code') == 0:
            return d.get('data', {})
        log(f"Tushare {api_name}: {d.get('msg', 'unknown error')}")
        return None
    except Exception as e:
        log(f"Tushare {api_name} exception: {e}")
        return None


def _ts_code(symbol):
    """股票代码转Tushare格式"""
    if symbol.startswith(('sh', 'sz')):
        return symbol.upper()
    if symbol.startswith(('6', '9', '5')):
        return f"{symbol}.SH"
    else:
        return f"{symbol}.SZ"


def _get_daily_basic(symbol):
    """获取最新daily_basic数据（PE/PB/市值/换手率/量比）"""
    ts_code = _ts_code(symbol)
    data = _tushare_api('daily_basic',
        {'ts_code': ts_code, 'start_date': '20260101', 'end_date': '20261231'},
        'ts_code,trade_date,close,pe,pe_ttm,pb,ps,ps_ttm,dv_ratio,total_mv,circ_mv,turnover_rate,volume_ratio')
    if not data or not data.get('items'):
        log(f"Tushare daily_basic无数据({symbol})，尝试AKShare容灾")
        return _ak_daily_basic(symbol)
    fields = data.get('fields', [])
    latest = data['items'][0]
    result = dict(zip(fields, latest))
    return result


def _get_valuation_percentile(symbol, years=5):
    """获取PE/PB历史分位数（默认5年）"""
    ts_code = _ts_code(symbol)
    from datetime import datetime, timedelta
    end_date = datetime.now().strftime('%Y%m%d')
    start_date = (datetime.now() - timedelta(days=365 * years)).strftime('%Y%m%d')
    data = _tushare_api('daily_basic',
        {'ts_code': ts_code, 'start_date': start_date, 'end_date': end_date},
        'ts_code,trade_date,close,pe,pe_ttm,pb')
    if not data or not data.get('items'):
        log(f"valuation_percentile: Tushare daily_basic无数据({symbol})")
        return None
    fields = data.get('fields', [])
    items = data.get('items', [])
    if len(items) < 30:
        log(f"valuation_percentile: 样本不足({symbol}), 仅{len(items)}条")
        return None
    pe_list, pb_list, pe_ttm_list, dates = [], [], [], []
    for item in items:
        row = dict(zip(fields, item))
        dates.append(row.get('trade_date', ''))
        pe_list.append(row.get('pe'))
        pe_ttm_list.append(row.get('pe_ttm'))
        pb_list.append(row.get('pb'))
    latest = dict(zip(fields, items[0]))
    latest_pe = latest.get('pe')
    latest_pe_ttm = latest.get('pe_ttm')
    latest_pb = latest.get('pb')
    def percentile(value, arr):
        valid = [x for x in arr if x is not None and x > 0]
        if not valid or value is None or value <= 0:
            return None
        below = sum(1 for x in valid if x < value)
        return round(below / len(valid) * 100, 1)
    def safe_min(arr):
        valid = [x for x in arr if x is not None and x > 0]
        return round(min(valid), 2) if valid else None
    def safe_max(arr):
        valid = [x for x in arr if x is not None and x > 0]
        return round(max(valid), 2) if valid else None
    def safe_avg(arr):
        valid = [x for x in arr if x is not None and x > 0]
        return round(sum(valid) / len(valid), 2) if valid else None
    return {
        'symbol': symbol,
        'trade_date': dates[0] if dates else '',
        'data_points': len(items),
        'period': f"{dates[-1]}~{dates[0]}" if len(dates) >= 2 else '',
        'pe': {
            'current': round(latest_pe, 2) if latest_pe and latest_pe > 0 else None,
            'percentile': percentile(latest_pe, pe_list),
            'min': safe_min(pe_list), 'max': safe_max(pe_list), 'avg': safe_avg(pe_list)
        },
        'pe_ttm': {
            'current': round(latest_pe_ttm, 2) if latest_pe_ttm and latest_pe_ttm > 0 else None,
            'percentile': percentile(latest_pe_ttm, pe_ttm_list),
            'min': safe_min(pe_ttm_list), 'max': safe_max(pe_ttm_list), 'avg': safe_avg(pe_ttm_list)
        },
        'pb': {
            'current': round(latest_pb, 2) if latest_pb and latest_pb > 0 else None,
            'percentile': percentile(latest_pb, pb_list),
            'min': safe_min(pb_list), 'max': safe_max(pb_list), 'avg': safe_avg(pb_list)
        }
    }


# ========== AKShare 容灾数据层 (DataHub v3.1) ==========

def _ak_daily_basic(symbol):
    """AKShare容灾: 获取PE/PB/市值等基本面数据(替代Tushare daily_basic)"""
    try:
        result = {}
        # 方法1: 东财个股指标
        try:
            df_ind = safe_request(ak.stock_a_indicator_lg, symbol=symbol)
            if df_ind is not None and not df_ind.empty:
                latest = df_ind.iloc[-1]
                result['pe_ttm'] = round(float(latest.get('pe_ttm', 0) or 0), 1)
                result['pb'] = round(float(latest.get('pb', 0) or 0), 2)
                result['dv_ratio'] = round(float(latest.get('dv_ratio', 0) or 0), 2)
                result['turnover_rate'] = round(float(latest.get('turnover_rate', 0) or 0), 2)
        except Exception:
            pass

        # 方法2: 东财个股信息(市值)
        try:
            df_info = safe_request(ak.stock_individual_info_em, symbol=symbol)
            if df_info is not None and not df_info.empty:
                for _, row in df_info.iterrows():
                    item = str(row.iloc[0]).strip() if len(row) > 0 else ''
                    value = row.iloc[1] if len(row) > 1 else ''
                    if '总市值' in item:
                        try:
                            mv = float(str(value).replace(',', '').replace('亿', ''))
                            result['total_mv'] = mv * 10000  # 转万元
                        except:
                            pass
                    elif '流通市值' in item:
                        try:
                            mv = float(str(value).replace(',', '').replace('亿', ''))
                            result['circ_mv'] = mv * 10000
                        except:
                            pass
                    elif '量比' in item:
                        try:
                            result['volume_ratio'] = round(float(value), 2)
                        except:
                            pass
        except Exception:
            pass

        if result:
            result['trade_date'] = datetime.now().strftime('%Y%m%d')
            result['close'] = 0
            return result
    except Exception as e:
        log(f'AKShare daily_basic容灾失败: {e}')
    return None


def _ak_capital_flow(symbol):
    """AKShare容灾: 获取个股资金流向(替代Tushare moneyflow)"""
    try:
        df = safe_request(ak.stock_individual_fund_flow, stock=symbol, market='sh' if symbol.startswith('6') else 'sz')
        if df is None or df.empty:
            return None

        df = df.tail(5).copy()
        recent_flow = []
        for _, row in df.iterrows():
            main_net = round(float(row.get('主力净流入-净额', 0) or 0) / 10000, 2)
            sm_net = round(float(row.get('小单净流入-净额', 0) or 0) / 10000, 2)
            md_net = round(float(row.get('中单净流入-净额', 0) or 0) / 10000, 2)
            lg_net = round(float(row.get('大单净流入-净额', 0) or 0) / 10000, 2)
            elg_net = round(float(row.get('超大单净流入-净额', 0) or 0) / 10000, 2)
            trade_date = str(row.get('日期', '')).replace('-', '')

            recent_flow.append({
                '日期': f'{trade_date[:4]}-{trade_date[4:6]}-{trade_date[6:]}' if len(trade_date) == 8 else str(row.get('日期', '')),
                '主力净流入': main_net,
                '小单净流入': sm_net,
                '中单净流入': md_net,
                '大单净流入': lg_net,
                '超大单净流入': elg_net,
            })

        recent_flow.reverse()  # 最新在前

        if not recent_flow:
            return None

        latest = recent_flow[0]
        return {
            'symbol': symbol,
            'latest_flow': latest,
            'recent_flow': recent_flow,
            'summary': {
                '主力净流入万': latest.get('主力净流入', 0),
                '超大单净流入万': latest.get('超大单净流入', 0),
                '大单净流入万': latest.get('大单净流入', 0),
                '方向': '主力流入' if latest.get('主力净流入', 0) > 0 else '主力流出'
            },
            '_source': 'AKShare'
        }
    except Exception as e:
        log(f'AKShare capital_flow容灾失败: {e}')
    return None


_SW_HIST_CACHE = {}

def _sw_hist(code_si, tail_n=2):
    """申万行业指数历史日线 (M9: 2026-09-07修复).
    病根: index_daily对申万代码(801xxx.SI)静默返回0行(覆盖面外), sw_daily无权限(积分墙),
    东财容灾被封(9/4实证RemoteDisconnected)——三路全断.
    正解: AKShare index_hist_sw(申万官网). 限制: 数据滞后约2个交易日(9/7查询最新到9/2),
    调用方必须向用户标注数据日期.
    返回: 按日期正序的tail_n行[{'date','close'}], 失败None. 进程内缓存(31行业×2函数复用)."""
    try:
        if code_si not in _SW_HIST_CACHE:
            import akshare as ak
            sym = code_si.split('.')[0]
            df = safe_request(lambda: ak.index_hist_sw(symbol=sym, period='day'))
            if df is None or (hasattr(df, 'empty') and df.empty):
                return None
            rows = sorted(
                ({'date': str(r['日期']).replace('-', ''), 'close': float(r['收盘'])}
                 for _, r in df.iterrows()),
                key=lambda x: x['date'])
            _SW_HIST_CACHE[code_si] = rows
        rows = _SW_HIST_CACHE[code_si]
        if not rows or len(rows) < tail_n:
            return rows if rows else None
        return rows[-tail_n:]
    except Exception as e:
        log(f'_sw_hist {code_si} 失败: {e}')
        return None

def _ak_sector_ranking():
    """AKShare容灾: 获取行业板块涨跌排名(替代Tushare申万行业)"""
    try:
        df = safe_request(ak.stock_board_industry_name_em)
        if df is None or df.empty:
            return None

        results = []
        for _, row in df.iterrows():
            name = str(row.get('板块名称', '')).strip()
            pct = float(row.get('涨跌幅', 0) or 0)
            if name:
                results.append({'板块名称': name, '涨跌幅': round(pct, 2)})

        if not results:
            return None

        results.sort(key=lambda x: x['涨跌幅'], reverse=True)
        return {
            '涨幅前3': results[:3],
            '跌幅前3': results[-3:],
            '数据源': 'AKShare(东财行业)'
        }
    except Exception as e:
        log(f'AKShare sector_ranking容灾失败: {e}')
    return None


def _ak_index_daily(ts_code='000300.SH', limit=1):
    """AKShare容灾: 获取指数数据(替代Tushare index_daily)"""
    try:
        symbol_map = {
            '000300.SH': 'sh000300',
            '000001.SH': 'sh000001',
            '399001.SZ': 'sz399001',
            '399006.SZ': 'sz399006',
        }
        ak_symbol = symbol_map.get(ts_code, f'sh{ts_code[:6]}')
        df = safe_request(ak.stock_zh_index_daily, symbol=ak_symbol)
        if df is None or df.empty:
            return None

        df = df.tail(int(limit)).copy()
        if limit == 1:
            latest = df.iloc[-1]
            return {
                'close': round(float(latest.get('close', 0) or 0), 2),
                'pct_chg': 0,  # 需要计算
                'items': [[latest.get('date', ''), round(float(latest.get('close', 0) or 0), 2)]]
            }

        # 多条数据
        closes = [round(float(x), 2) for x in df['close'].tolist()]
        return {'closes': closes, 'items': df.values.tolist()}
    except Exception as e:
        log(f'AKShare index_daily容灾失败: {e}')
    return None


def _ak_lhb_detail(symbol, days=5):
    """AKShare: 获取个股龙虎榜明细（先拉全市场再过滤个股）"""
    try:
        start_date = (datetime.now() - timedelta(days=int(days))).strftime('%Y%m%d')
        end_date = datetime.now().strftime('%Y%m%d')

        df = safe_request(ak.stock_lhb_detail_em,
                         start_date=start_date,
                         end_date=end_date)
        if df is None or df.empty:
            return {'symbol': symbol, 'message': f'近{days}天全市场无龙虎榜数据'}

        # 过滤目标个股（__all__ 标记跳过过滤返回全量）
        if symbol == '__all__':
            df_filtered = df
        elif '代码' in df.columns:
            df_filtered = df[df['代码'].astype(str) == str(symbol)]
        elif '股票代码' in df.columns:
            df_filtered = df[df['股票代码'].astype(str) == str(symbol)]
        else:
            return {'symbol': symbol, 'message': '龙虎榜列名未识别', 'columns': list(df.columns)}

        if df_filtered.empty:
            return {'symbol': symbol, 'message': f'近{days}天该股无龙虎榜记录'}

        results = []
        for _, row in df_filtered.iterrows():
            entry = {}
            for col in df_filtered.columns:
                val = row[col]
                if pd.api.types.is_numeric_dtype(df_filtered[col]):
                    entry[col] = round(float(val), 2) if pd.notna(val) else 0
                else:
                    entry[col] = str(val) if pd.notna(val) else ''
            results.append(entry)

        return {
            'symbol': symbol,
            'count': len(results),
            'records': results,
            'data_source': 'AKShare'
        }
    except Exception as e:
        return {'error': f'龙虎榜数据获取失败: {str(e)[:80]}'}


def _ak_block_trade(symbol, days=5):
    """AKShare: 获取个股大宗交易明细"""
    try:
        start_date = (datetime.now() - timedelta(days=int(days))).strftime('%Y%m%d')
        end_date = datetime.now().strftime('%Y%m%d')

        try:
            df = safe_request(ak.stock_dzjy_mrmx, symbol='股票', start_date=start_date, end_date=end_date)
        except Exception:
            df = None
            
        if df is None or df.empty:
            return {'symbol': symbol, 'message': f'近{days}天无大宗交易或数据源解析异常'}

        if symbol == '__all__':
            df_filtered = df
        else:
            code_col = None
            for col in ['股票代码', '代码']:
                if col in df.columns:
                    code_col = col
                    break
            if not code_col:
                return {'symbol': symbol, 'message': '大宗交易列名未识别', 'columns': list(df.columns)}
            df_filtered = df[df[code_col].astype(str) == str(symbol)]
            
        if df_filtered.empty:
            return {'symbol': symbol, 'message': f'近{days}天该股无大宗交易'}

        results = []
        for _, row in df_filtered.iterrows():
            entry = {}
            for col in df_filtered.columns:
                val = row[col]
                if pd.api.types.is_numeric_dtype(df_filtered[col]):
                    entry[col] = round(float(val), 2) if pd.notna(val) else 0
                else:
                    entry[col] = str(val) if pd.notna(val) else ''
            results.append(entry)

        return {
            'symbol': symbol,
            'count': len(results),
            'records': results,
            'data_source': 'AKShare'
        }
    except Exception as e:
        return {'error': f'大宗交易数据获取失败: {str(e)[:80]}'}


def _ak_share_unlock():
    """AKShare: 获取限售解禁排名（全市场，返回近30天）"""
    try:
        df = safe_request(ak.stock_rank_cxsl_ths)
        if df is None or df.empty:
            return []

        results = []
        for _, row in df.iterrows():
            entry = {}
            for col in df.columns:
                val = row[col]
                # M10d-2026-09-08: NaN不再转0 -- 停牌股0价曾算出-100%假跌幅
                if pd.api.types.is_numeric_dtype(df[col]):
                    entry[col] = round(float(val), 2) if pd.notna(val) else None
                else:
                    entry[col] = str(val) if pd.notna(val) else ''
            if entry.get('最新价') is None:
                entry['停牌标记'] = 'price_null(suspect suspended)'
            results.append(entry)
        return results
    except Exception as e:
        log(f'限售解禁数据获取失败: {e}')
        return []


def _ak_earnings_forecast(date=None):
    """AKShare: 获取业绩预告（按报告期）"""
    try:
        if not date:
            now = datetime.now()
            y = now.year
            m = now.month
            if m <= 4:
                date = f'{y-1}0930'  # 去年三季报
            elif m <= 7:
                date = f'{y-1}1231'  # 去年年报
            elif m <= 10:
                date = f'{y}0331'  # 一季报
            else:
                date = f'{y}0630'  # 中报

        df = safe_request(ak.stock_yjyg_em, date=date)
        if df is None or df.empty:
            return [], date

        results = []
        for _, row in df.iterrows():
            entry = {}
            for col in df.columns:
                val = row[col]
                # M10d-2026-09-08: NaN不再转0 -- 停牌股0价曾算出-100%假跌幅
                if pd.api.types.is_numeric_dtype(df[col]):
                    entry[col] = round(float(val), 2) if pd.notna(val) else None
                else:
                    entry[col] = str(val) if pd.notna(val) else ''
            if entry.get('最新价') is None:
                entry['停牌标记'] = 'price_null(suspect suspended)'
            results.append(entry)
        return results, date
    except Exception as e:
        log(f'业绩预告数据获取失败: {e}')
        return [], date if date else ''


def scan_events(symbols=None, days=5):
    """事件型异动扫描 - 4类检测（盘后/非实时）"""
    if not symbols:
        wl = read_watchlist()
        symbols = [s['code'] for s in wl]

    if not symbols:
        return {'scan_time': datetime.now().strftime('%Y-%m-%d %H:%M:%S'), 'message': '自选股为空'}

    results = {}
    symbols_str = [str(s) for s in symbols]

    # 1. 龙虎榜异动
    try:
        lhb_data = _ak_lhb_detail('__all__', days)
        if 'records' in lhb_data:
            lhb_filtered = [r for r in lhb_data['records'] if str(r.get('代码', r.get('股票代码', ''))) in symbols_str]
            results['龙虎榜'] = {'count': len(lhb_filtered), 'records': lhb_filtered}
        else:
            results['龙虎榜'] = {'count': 0, 'message': f'近{days}天无龙虎榜记录'}
    except Exception as e:
        results['龙虎榜'] = {'error': str(e)[:80]}

    # 2. 大宗交易
    try:
        bt_data = _ak_block_trade('__all__', days)
        if 'records' in bt_data:
            bt_filtered = [r for r in bt_data['records'] if str(r.get('股票代码', r.get('代码', ''))) in symbols_str]
            results['大宗交易'] = {'count': len(bt_filtered), 'records': bt_filtered}
        else:
            results['大宗交易'] = {'count': 0, 'message': f'近{days}天无大宗交易'}
    except Exception as e:
        results['大宗交易'] = {'error': str(e)[:80]}

    # 3. 限售解禁
    try:
        unlock_all = _ak_share_unlock()
        unlock_filtered = [r for r in unlock_all if str(r.get('代码', r.get('股票代码', ''))) in symbols_str]
        results['限售解禁'] = {'count': len(unlock_filtered), 'records': unlock_filtered}
    except Exception as e:
        results['限售解禁'] = {'error': str(e)[:80]}

    # 4. 业绩预告
    try:
        forecast_all, report_date = _ak_earnings_forecast()
        forecast_filtered = [r for r in forecast_all if str(r.get('代码', r.get('股票代码', ''))) in symbols_str]
        results['业绩预告'] = {'count': len(forecast_filtered), 'report_date': report_date, 'records': forecast_filtered}
    except Exception as e:
        results['业绩预告'] = {'error': str(e)[:80]}

    return {
        'scan_time': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'symbols': symbols,
        'days': days,
        'results': results
    }


# ========== 舆情分析 v3.1 ==========

def _ak_sentiment_detail(symbol):
    """AKShare: 个股舆情聚合（机构参与度+综合评分+关注度+买入欲望+关键词）"""
    result = {'symbol': symbol, 'data_source': 'AKShare(东财)'}
    
    # 1. 机构参与度 (1-5分)
    try:
        df = safe_request(ak.stock_comment_detail_zlkp_jgcyd_em, symbol=symbol)
        if df is not None and not df.empty:
            latest = df.iloc[-1]
            result['机构参与度'] = {
                '评分': str(latest.iloc[1]) if pd.notna(latest.iloc[1]) else '',
                '日期': str(latest.iloc[0]) if pd.notna(latest.iloc[0]) else '',
    
            }
    except Exception:
        pass

    # 2. 综合评价历史评分
    try:
        df = safe_request(ak.stock_comment_detail_zhpj_lspf_em, symbol=symbol)
        if df is not None and not df.empty:
            latest = df.iloc[-1]
            result['综合评价'] = {
                '评分': round(float(latest.iloc[1]), 2) if pd.notna(latest.iloc[1]) and str(latest.iloc[1]).replace('.','',1).replace('-','',1).isdigit() else str(latest.iloc[1]),
                '日期': str(latest.iloc[0]) if pd.notna(latest.iloc[0]) else '',
            }
    except Exception:
        pass

    # 3. 关注度
    try:
        df = safe_request(ak.stock_comment_detail_scrd_focus_em, symbol=symbol)
        if df is not None and not df.empty:
            latest = df.iloc[-1]
            result['关注度'] = {
                '评分': round(float(latest.iloc[1]), 2) if pd.notna(latest.iloc[1]) and str(latest.iloc[1]).replace('.','',1).replace('-','',1).isdigit() else str(latest.iloc[1]),
                '日期': str(latest.iloc[0]) if pd.notna(latest.iloc[0]) else '',
            }
    except Exception:
        pass

    # 4. 买入欲望
    try:
        df = safe_request(ak.stock_comment_detail_scrd_desire_em, symbol=symbol)
        if df is not None and not df.empty:
            latest = df.iloc[-1]
            desire = latest.get('参与意愿', 0)
            result['买入欲望'] = {
                '参与意愿': round(float(desire), 2) if pd.notna(desire) else 0,
                '5日均值': round(float(latest.get('5日平均参与意愿', 0) or 0), 2),
                '变化': round(float(latest.get('参与意愿变化', 0) or 0), 2),
                '日期': str(latest.get('交易日期', '')),
            }
    except Exception:
        pass

    # 5. 热门概念（东财概念热度，替代关键词）
    try:
        ak_symbol = f"{'SH' if symbol.startswith('6') else 'SZ'}{symbol}"
        df = safe_request(ak.stock_hot_keyword_em, symbol=ak_symbol)
        if df is not None and not df.empty:
            concepts = []
            for _, row in df.head(8).iterrows():
                concepts.append({
                    '概念': str(row.get('概念名称', '')),
                    '热度': int(row.get('热度', 0)) if pd.notna(row.get('热度')) else 0
                })
            result['热门概念'] = concepts
    except Exception:
        pass

    return result


def _ak_sentiment_market_rank():
    """AKShare: 全市场人气排名TOP100"""
    try:
        df = safe_request(ak.stock_hot_rank_em)
        if df is None or df.empty:
            return []

        results = []
        for _, row in df.head(100).iterrows():
            entry = {}
            for col in df.columns:
                val = row[col]
                # M10d-2026-09-08: NaN不再转0 -- 停牌股0价曾算出-100%假跌幅
                if pd.api.types.is_numeric_dtype(df[col]):
                    entry[col] = round(float(val), 2) if pd.notna(val) else None
                else:
                    entry[col] = str(val) if pd.notna(val) else ''
            if entry.get('最新价') is None:
                entry['停牌标记'] = 'price_null(suspect suspended)'
            results.append(entry)
        return results
    except Exception as e:
        log(f'全市场人气排名获取失败: {e}')
        return []


def sentiment_scan(symbol=None, symbols=None):
    """舆情分析主入口 — 个股或批量"""
    if not symbol and not symbols:
        return {'error': '请提供symbol(单个)或symbols(批量)'}

    target_symbols = [symbol] if symbol else symbols
    results = []

    for sym in target_symbols:
        detail = _ak_sentiment_detail(str(sym))
        results.append(detail)

    # 如果是批量，额外附加人气排名交叉匹配
    if len(target_symbols) > 1:
        try:
            rank_all = _ak_sentiment_market_rank()
            if rank_all:
                rank_map = {}
                for item in rank_all:
                    code = str(item.get('股票代码', ''))
                    if code:
                        rank_map[code] = item
                
                for r in results:
                    sym = r.get('symbol', '')
                    if sym in rank_map:
                        r['市场人气排名'] = rank_map[sym]
        except Exception:
            pass

    return {
        'scan_time': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'count': len(results),
        'results': results
    }


# ========== 组合压力测试 v3.1 ==========

def _get_sector_betas():
    """获取申万一级行业相对沪深300的近似Beta值"""
    return {
        '银行': 0.85, '非银金融': 1.35, '食品饮料': 0.95, '医药生物': 0.90,
        '电子': 1.25, '计算机': 1.30, '通信': 1.15, '传媒': 1.20,
        '汽车': 1.15, '机械设备': 1.20, '电力设备': 1.25, '国防军工': 1.30,
        '化工': 1.10, '钢铁': 1.15, '有色金属': 1.40, '建筑材料': 1.05,
        '建筑装饰': 0.95, '农林牧渔': 1.05, '家用电器': 0.90, '纺织服饰': 0.95,
        '轻工制造': 1.00, '房地产': 1.35, '商贸零售': 1.05, '社会服务': 1.10,
        '综合': 1.00, '公用事业': 0.70, '交通运输': 0.95, '环保': 1.05,
        '美容护理': 0.95, '石油石化': 1.10, '煤炭': 1.20
    }


_SECTOR_CACHE = {}


def _real_sector(symbol):
    """M14-2026-09-21: SW L1 truth route -- index_member_all runtime query + process cache.
    Fixes M10d keyword-guess misjudgment (川投能源 '能源'->煤炭 / 华能国际 no-keyword->综合).
    Probe verified 2026-09-21 with 2126 pts: 600674->公用事业 / 601963->银行.
    Returns None on failure; caller _guess_sector degrades to keyword fallback."""
    if symbol in _SECTOR_CACHE:
        return _SECTOR_CACHE[symbol]
    try:
        data = _tushare_api('index_member_all',
            {'ts_code': _ts_code(symbol)}, 'ts_code,name,l1_code,l1_name')
        if data and data.get('items'):
            for row in data['items']:
                if len(row) > 3 and row[3]:
                    _SECTOR_CACHE[symbol] = row[3]
                    return row[3]
    except Exception:
        pass
    return None


def _guess_sector(symbol):
    """M14-2026-09-21: 真值优先四级路由 -- _real_sector(index_member_all真值) -> name关键词(31行业, 断网降级) -> watchlist行业真值 -> 综合兜底
    主案修复(翔批2026-09-21 09:13授权): _exemption_check P1板块庇护曾被关键词猜谜污染,
    川投能源(水电)因名含'能源'误判煤炭downtrend. 展示层与判决层统一走本函数,
    零级失败自动降级M10d原三级路由, 永不抛错."""
    real = _real_sector(symbol)
    if real:
        return real
    # ---- M10d原三级路由, 自此为断网fallback ----
    name = _get_name(symbol)
    hints = {
        '银行': ['银行', '商行'], '非银金融': ['证券', '中信', '保险', '人寿', '期货'],
        '食品饮料': ['酒', '茅台', '五粮液', '食品', '乳业', '饮料'],
        '医药生物': ['药', '医疗', '生物', '健康', '制药'],
        '电子': ['半导体', '芯片', '电子', '科技', '光', '晶'],
        '计算机': ['软件', '信息', '数据', '计算机', '智能'],
        '通信': ['通信', '通讯', '网络', '电信'],
        '传媒': ['传媒', '影视', '文化', '出版', '游戏'],
        '汽车': ['汽车', '车', '长安', '比亚迪', '赛力斯'],
        '机械设备': ['机械', '设备', '重工', '精密'],
        '电力设备': ['电力设备', '电池', '光伏', '风电', '储能', '宁德'],
        '国防军工': ['军工', '国防', '航空', '航天', '兵器'],
        '基础化工': ['化工', '化学', '氟', '硅'],
        '钢铁': ['钢', '铁', '冶金'],
        '有色金属': ['有色', '铝', '铜', '金', '银', '锂', '钼', '锌', '镍', '稀土', '矿'],
        '建筑材料': ['建材', '水泥', '玻璃', '石膏'],
        '建筑装饰': ['建筑', '装饰', '建设', '工程'],
        '农林牧渔': ['农业', '牧', '渔', '种业', '养殖', '饲料', '猪', '牧原'],
        '家用电器': ['家电', '电器', '格力', '美的', '海尔'],
        '纺织服饰': ['纺织', '服饰', '服装', '布', '纤'],
        '轻工制造': ['轻工', '家居', '造纸', '包装', '文具'],
        '房地产': ['地产', '万科', '保利', '置业'],
        '商贸零售': ['商贸', '零售', '百货', '超市', '商城'],
        '社会服务': ['服务', '旅游', '酒店', '教育', '餐饮'],
        '公用事业': ['电力', '水务', '燃气', '环保', '环境'],
        '交通运输': ['运输', '物流', '航空', '港口', '铁路', '海运', '远洋'],
        '环保': ['环保', '环境', '节能', '治污'],
        '美容护理': ['美容', '护理', '化妆'],
        '石油石化': ['石油', '石化', '油', '油田'],
        '煤炭': ['煤炭', '煤', '焦', '神华'],  # M14止血: '能源'摘除--川投/三峡能源皆水电系, 错挂煤炭比空白综合更毒
        '综合': ['综合', '控股', '集团', '投资'],
    }
    for sector, keywords in hints.items():
        if any(kw in name for kw in keywords):
            return sector
    # 二级: watchlist行业字段真值(若录入过)
    try:
        wl = read_watchlist()
        for s in wl:
            if s.get('code') == symbol and s.get('industry'):
                return s['industry']
    except Exception:
        pass
    return '综合'


def stress_test(scenario='crash_2015', drop_pct=None, custom_drop=None):
    """组合压力测试 — 历史极端行情模拟
    
    场景：
    - crash_2015: 2015股灾（3周跌35%）
    - crash_2024: 2024年1月雪崩（单周跌12%）
    - trade_war: 2018贸易战（6个月跌25%）
    - covid_2020: 2020年3月疫情（2周跌16%）
    - 924_surge: 2024年924行情（单周涨25%）← 压力反向测试
    - custom: 自定义跌幅
    """
    scenarios = {
        'crash_2015': {'name': '2015股灾', 'hs300_drop': -35, 'days': 21, 'desc': '3周暴跌35%'},
        'crash_2024': {'name': '2024年1月', 'hs300_drop': -12, 'days': 7, 'desc': '单周跌12%'},
        'trade_war': {'name': '2018贸易战', 'hs300_drop': -25, 'days': 120, 'desc': '6个月跌25%'},
        'covid_2020': {'name': '2020疫情', 'hs300_drop': -16, 'days': 14, 'desc': '2周跌16%'},
        '924_surge': {'name': '924行情', 'hs300_drop': 25, 'days': 5, 'desc': '单周暴涨25%'},
    }
    
    if scenario not in scenarios and not custom_drop:
        return {'error': f'未知场景: {scenario}。支持: {", ".join(scenarios.keys())}'}
    
    # 自定义场景
    if custom_drop is not None:
        scenarios['custom'] = {'name': '自定义', 'hs300_drop': float(custom_drop), 'days': 30, 'desc': f'沪深300跌/涨{custom_drop}%'}
        scenario = 'custom'
    
    sc = scenarios[scenario]
    hs300_drop = sc['hs300_drop']
    
    positions = read_positions()
    active = [p for p in positions if p.get('status') == 'active']
    if not active:
        return {'error': '当前无活跃持仓，无法进行压力测试'}
    
    # 获取实时价格
    symbols = [p['symbol'] for p in active]
    quotes = _sina_batch_quotes(symbols)
    quote_map = {q.get('代码'): q for q in quotes}
    
    betas = _get_sector_betas()
    results = []
    
    for pos in active:
        sym = pos['symbol']
        cost = pos['cost']
        shares = pos['shares']
        
        q = quote_map.get(sym, {})
        current_price = float(q.get('最新价', 0) or 0)
        if current_price <= 0:
            continue
        
        current_value = current_price * shares
        
        # 猜测行业Beta
        sector = _guess_sector(sym)
        beta = betas.get(sector, 1.0)
        
        # 模拟压力：个股跌幅 ≈ 大盘跌幅 × Beta
        # 对上涨场景同样适用
        stock_drop = hs300_drop * beta
        stressed_price = current_price * (1 + stock_drop / 100)
        stressed_value = stressed_price * shares
        
        loss = stressed_value - current_value
        loss_pct = round((stressed_price - current_price) / current_price * 100, 2)
        
        # 对总成本的压力
        total_pnl = stressed_value - cost * shares
        total_pnl_pct = round((stressed_price - cost) / cost * 100, 2) if cost > 0 else 0
        
        results.append({
            'symbol': sym,
            'name': pos.get('name', sym),
            'sector': sector,
            'beta': beta,
            'current_price': round(current_price, 2),
            'stressed_price': round(stressed_price, 2),
            'current_value': round(current_value, 2),
            'stressed_value': round(stressed_value, 2),
            'change': round(loss, 2),
            'change_pct': loss_pct,
            'vs_cost_pct': total_pnl_pct,
        })
    
    # 汇总
    total_current = sum(r['current_value'] for r in results)
    total_stressed = sum(r['stressed_value'] for r in results)
    total_change = total_stressed - total_current
    total_change_pct = round(total_change / total_current * 100, 2) if total_current > 0 else 0
    
    # 账户级别
    acct = read_account()
    available_cash = acct.get('available_cash', 0)
    total_capital = acct.get('total_capital', 0)
    current_total_assets = total_current + available_cash
    stressed_total_assets = total_stressed + available_cash
    current_pnl = round(current_total_assets - total_capital, 2) if total_capital > 0 else 0
    stressed_pnl = round(stressed_total_assets - total_capital, 2) if total_capital > 0 else 0
    
    # 组合加权Beta
    weighted_beta = round(sum(r['beta'] * r['current_value'] for r in results) / total_current, 2) if total_current > 0 else 1.0
    
    return {
        'scenario': sc['name'],
        'description': sc['desc'],
        'hs300_change_pct': hs300_drop,
        'portfolio_beta': weighted_beta,
        'positions': results,
        'summary': {
            'total_current_value': round(total_current, 2),
            'total_stressed_value': round(total_stressed, 2),
            'total_change': round(total_change, 2),
            'total_change_pct': total_change_pct,
            'current_assets': round(current_total_assets, 2),
            'stressed_assets': round(stressed_total_assets, 2),
            'current_pnl': current_pnl,
            'stressed_pnl': stressed_pnl,
            'available_cash': round(available_cash, 2),
        }
    }


# ========== 板块轮动追踪 v3.1 ==========

def sector_rotation():
    """板块轮动追踪 — 31个申万行业5日/10日/20日动量分析"""
    try:
        # Step1: 拿行业列表
        ind_data = _tushare_api('index_classify',
            {'level': 'L1', 'src': 'SW2021'},
            'index_code,industry_name')
        
        if not ind_data or not ind_data.get('items'):
            log("板块轮动: Tushare行业列表获取失败，尝试AKShare")
            # AKShare容灾：拉东财行业当前快照（无历史对比）
            ak_result = _ak_sector_ranking()
            if ak_result:
                return {
                    'mode': 'snapshot_only',
                    'message': '历史数据获取失败，仅返回当日快照',
                    'today_ranking': ak_result
                }
            return {'error': '板块数据获取失败'}

        industries = ind_data.get('items', [])
        results = []

        # Step2: 每个行业拉20天日线 (M9修复2026-09-07: index_daily对申万代码静默0行, 改走申万官网 _sw_hist)
        for code, name in industries:
            time.sleep(0.12)
            hist = _sw_hist(code, tail_n=22)
            if not hist:
                continue

            # 适配下游: _sw_hist仅date+close, 补算pct_chg保持原rows结构兼容(正序)
            rows = []
            for i, r in enumerate(hist):
                prev_close = hist[i - 1]['close'] if i > 0 else None
                pct_chg = round((r['close'] / prev_close - 1) * 100, 4) if prev_close else 0.0
                rows.append({'trade_date': r['date'], 'close': r['close'], 'pct_chg': pct_chg})

            if len(rows) < 5:
                continue

            closes = [float(r.get('close', 0) or 0) for r in rows]

            # 计算区间涨跌幅
            today_close = closes[-1]
            pct_1d = float(rows[-1].get('pct_chg', 0) or 0)

            pct_5d = 0
            if len(closes) >= 6:
                pct_5d = round((today_close - closes[-6]) / closes[-6] * 100, 2)

            pct_10d = 0
            if len(closes) >= 11:
                pct_10d = round((today_close - closes[-11]) / closes[-11] * 100, 2)

            pct_20d = 0
            if len(closes) >= 21:
                pct_20d = round((today_close - closes[-21]) / closes[-21] * 100, 2)

            # 动量信号判断
            momentum = 'neutral'
            if pct_5d > pct_10d > pct_20d and pct_5d > 0:
                momentum = 'accelerating'  # 动量加速
            elif pct_5d < pct_10d < pct_20d and pct_5d < 0:
                momentum = 'decelerating'  # 动量衰减
            elif pct_5d > 0 and pct_10d > 0 and pct_20d > 0:
                momentum = 'uptrend'  # 持续上行
            elif pct_5d < 0 and pct_10d < 0 and pct_20d < 0:
                momentum = 'downtrend'  # 持续下行
            elif pct_5d > 0 and pct_20d < 0:
                momentum = 'rebounding'  # 超跌反弹
            elif pct_5d < 0 and pct_20d > 0:
                momentum = 'pulling_back'  # 回调

            results.append({
                'name': name,
                'code': code,
                'pct_1d': pct_1d,
                'pct_5d': pct_5d,
                'pct_10d': pct_10d,
                'pct_20d': pct_20d,
                'momentum': momentum
            })

        if not results:
            return {'error': '板块历史数据获取失败'}

        # 排序：按5日涨跌幅
        results.sort(key=lambda x: x['pct_5d'], reverse=True)

        # 分类汇总
        accelerating = [r for r in results if r['momentum'] == 'accelerating']
        decelerating = [r for r in results if r['momentum'] == 'decelerating']
        uptrend = [r for r in results if r['momentum'] == 'uptrend']
        downtrend = [r for r in results if r['momentum'] == 'downtrend']
        rebounding = [r for r in results if r['momentum'] == 'rebounding']
        pulling_back = [r for r in results if r['momentum'] == 'pulling_back']

        # 强势Top5（5日涨幅最大）
        top5 = results[:5]
        # 弱势Top5（5日跌幅最大）
        bot5 = results[-5:][::-1]

        return {
            'mode': 'full_rotation',
            'scan_time': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'data_source': 'Tushare(申万一级)',
            'total_sectors': len(results),
            'top5_5d': top5,
            'bot5_5d': bot5,
            'signals': {
                'accelerating': accelerating,  # 资金加速流入
                'decelerating': decelerating,  # 资金加速流出
                'uptrend': uptrend,            # 持续强势
                'downtrend': downtrend,        # 持续弱势
                'rebounding': rebounding,      # 超跌反弹
                'pulling_back': pulling_back,  # 高位回调
            },
            'all_sectors': results
        }
    except Exception as e:
        return {'error': f'板块轮动分析失败: {str(e)[:80]}'}


# ========== 市场温度计 v3.2 ==========

def market_temperature():
    """市场温度计 — 涨跌停/涨跌比/换手率/成交额 → 市场情绪综合判断"""
    try:
        today = datetime.now().strftime('%Y%m%d')
        
        # 1. 涨跌停数据（AKShare东财涨停池）
        zt_count = 0
        dt_count = 0
        zt_sectors = []
        try:
            zt_df = safe_request(ak.stock_zt_pool_em, date=today)
            if zt_df is not None and not zt_df.empty:
                zt_count = len(zt_df)
                # 统计涨停股所属行业
                if '所属行业' in zt_df.columns:
                    zt_sectors = zt_df['所属行业'].value_counts().head(5).to_dict()
        except Exception:
            pass
        
        try:
            dt_df = safe_request(ak.stock_zt_pool_dtgc_em, date=today)
            if dt_df is not None and not dt_df.empty:
                dt_count = len(dt_df)
        except Exception:
            pass

        # 2. 全市场行情统计
        df = _get_spot_data()
        if df is None or df.empty:
            return {"error": "全市场行情数据获取失败"}
        
        up = int((df['涨跌幅'] > 0).sum())
        down = int((df['涨跌幅'] < 0).sum())
        flat = int((df['涨跌幅'] == 0).sum())
        up_down_ratio = round(up / max(down, 1), 2)
        
        # 换手率中位数
        turnover_vals = pd.to_numeric(df.get('换手率', pd.Series([0]*len(df))), errors='coerce')
        turnover_median = round(float(turnover_vals.median()), 2)
        
        # 两市成交额（AKShare的成交额单位是元，转亿）
        if '成交额' in df.columns:
            total_amount = pd.to_numeric(df['成交额'], errors='coerce').sum()
            total_amount_yi = round(float(total_amount) / 100000000, 0)
        else:
            total_amount_yi = 0

        # 3. 温度计评分（0-100，50为中性）
        score = 50.0
        # 涨跌比偏离1.0 → 每偏离0.1加/减2分
        score += (up_down_ratio - 1.0) * 20
        # 涨停-跌停净数 → 每个加/减0.3分
        score += (zt_count - dt_count) * 0.3
        # 成交额偏离8000亿均值 → 每偏离1000亿加/减2分
        score += (total_amount_yi - 8000) / 500
        # 换手率偏离2.5%中位 → 每偏离0.5%加/减1分
        score += (turnover_median - 2.5) / 0.5
        score = max(0, min(100, round(score, 1)))

        # 4. 情绪判断
        if score >= 75:
            sentiment = "🔥 极热（情绪亢奋，警惕高位分歧）"
        elif score >= 60:
            sentiment = "☀️ 偏热（多头占优，可正常操作）"
        elif score >= 40:
            sentiment = "☁️ 中性（多空均衡，半仓观望）"
        elif score >= 25:
            sentiment = "❄️ 偏冷（空头占优，收紧止损）"
        else:
            sentiment = "🧊 极冷（恐慌蔓延，观望或逆向思考）"

        return {
            "date": today,
            "score": score,
            "sentiment": sentiment,
            "limit_up": zt_count,
            "limit_down": dt_count,
            "advance": up,
            "decline": down,
            "flat": flat,
            "up_down_ratio": up_down_ratio,
            "turnover_median": turnover_median,
            "total_amount_yi": total_amount_yi,
            "hot_sectors": zt_sectors,
            "hs300_change": get_hs300_change()
        }
    except Exception as e:
        return {"error": f"市场温度计计算失败: {str(e)[:80]}"}


# ========== 月度复盘 v3.2 ==========

def trade_stats_monthly():
    """月度复盘 — 按月/胜率/盈亏比统计"""
    trades = read_trades()
    sells = [t for t in trades if t.get("action") == "sell"]
    
    if not sells:
        return {"total_trades": 0, "message": "暂无已平仓交易"}
    
    # 按月分组
    monthly = {}
    for t in sells:
        date = t.get("date", "")
        month_key = date[:7] if len(date) >= 7 else "unknown"
        if month_key not in monthly:
            monthly[month_key] = {
                "month": month_key,
                "trades": 0, "wins": 0, "losses": 0,
                "total_pnl": 0, "win_pnls": [], "loss_pnls": []
            }
        m = monthly[month_key]
        m["trades"] += 1
        pnl = t.get("pnl", 0)
        m["total_pnl"] += pnl
        if pnl > 0:
            m["wins"] += 1
            m["win_pnls"].append(pnl)
        elif pnl < 0:
            m["losses"] += 1
            m["loss_pnls"].append(pnl)
    
    # 计算每月详细统计
    monthly_stats = []
    for month_key in sorted(monthly.keys()):
        m = monthly[month_key]
        win_rate = round(m["wins"] / m["trades"] * 100, 1) if m["trades"] > 0 else 0
        avg_win = round(sum(m["win_pnls"]) / len(m["win_pnls"]), 2) if m["win_pnls"] else 0
        avg_loss = round(sum(m["loss_pnls"]) / len(m["loss_pnls"]), 2) if m["loss_pnls"] else 0
        profit_ratio = round(abs(avg_win / avg_loss), 2) if avg_loss != 0 else 0
        
        monthly_stats.append({
            "month": month_key,
            "trades": m["trades"],
            "wins": m["wins"],
            "losses": m["losses"],
            "win_rate": win_rate,
            "total_pnl": round(m["total_pnl"], 2),
            "avg_win": avg_win,
            "avg_loss": avg_loss,
            "profit_ratio": profit_ratio  # 盈亏比 = 平均盈利/平均亏损
        })
    
    # 总览
    total_pnl = sum(t.get("pnl", 0) for t in sells)
    all_wins = [t for t in sells if t.get("pnl", 0) > 0]
    all_losses = [t for t in sells if t.get("pnl", 0) < 0]
    avg_win = round(sum(t.get("pnl", 0) for t in all_wins) / len(all_wins), 2) if all_wins else 0
    avg_loss = round(sum(t.get("pnl", 0) for t in all_losses) / len(all_losses), 2) if all_losses else 0
    
    return {
        "total_summary": {
            "total_sells": len(sells),
            "win_rate": round(len(all_wins) / len(sells) * 100, 1),
            "total_pnl": round(total_pnl, 2),
            "avg_win": avg_win,
            "avg_loss": avg_loss,
            "profit_ratio": round(abs(avg_win / avg_loss), 2) if avg_loss != 0 else 0
        },
        "monthly": monthly_stats
    }


# ========== 自选股管理 ==========

def read_watchlist():
    if not os.path.exists(WATCHLIST_PATH):
        return []
    try:
        with open(WATCHLIST_PATH, 'r', encoding='utf-8') as f:
            data = json.load(f)
            return data.get("stocks", [])
    except Exception:
        return []


def save_watchlist(stocks):
    data = {
        "updated": datetime.now().strftime("%Y-%m-%d"),
        "stocks": stocks
    }
    with open(WATCHLIST_PATH, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


@synchronized_data
def watchlist_add(code, name=""):
    stocks = read_watchlist()
    for s in stocks:
        if s["code"] == code:
            return {"status": "exists", "message": f"{code}已在自选股中"}
    if not name or name == code:
        name = _get_name(code) or code  # 主动获取真名，失败则用代码兜底
    stocks.append({
        "code": code,
        "name": name,
        "added": datetime.now().strftime("%Y-%m-%d")
    })
    save_watchlist(stocks)
    return {"status": "added", "message": f"已添加 {name}({code})"}


@synchronized_data
def watchlist_remove(code):
    stocks = read_watchlist()
    new_stocks = [s for s in stocks if s["code"] != code]
    if len(new_stocks) == len(stocks):
        return {"status": "not_found", "message": f"{code}不在自选股中"}
    removed_name = next((s["name"] for s in stocks if s["code"] == code), code)
    save_watchlist(new_stocks)
    return {"status": "removed", "message": f"已移除 {removed_name}({code})"}


@synchronized_data
def watchlist_show():
    stocks = read_watchlist()
    # 自动修复乱码名称
    changed = False
    for s in stocks:
        # 修复：名称含?或等于代码时，自动从新浪获取真名
        current_name = str(s.get('name', ''))
        if '?' in current_name or current_name == s.get('code', ''):
            new_name = _get_name(s['code'])
            if new_name and '?' not in new_name:
                s['name'] = new_name
                changed = True
    if changed:
        save_watchlist(stocks)
    return {"count": len(stocks), "stocks": stocks}


# ========== 持仓监控管理 ==========

def read_positions():
    if not os.path.exists(POSITIONS_PATH):
        return []
    try:
        with open(POSITIONS_PATH, 'r', encoding='utf-8') as f:
            data = json.load(f)
            return data.get("positions", [])
    except Exception:
        return []


def save_positions(positions):
    data = {
        "updated": datetime.now().strftime("%Y-%m-%d"),
        "positions": positions
    }
    with open(POSITIONS_PATH, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)



# ========== 交易记录管理 ==========

def read_trades():
    if not os.path.exists(TRADES_PATH):
        return []
    try:
        with open(TRADES_PATH, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception:
        return []


def save_trades(trades):
    with open(TRADES_PATH, 'w', encoding='utf-8') as f:
        json.dump(trades, f, ensure_ascii=False, indent=2)

def read_account():
    """读取账户资金信息"""
    _path = ACCOUNT_PATH
    if not os.path.exists(_path):
        return {"total_capital": 0, "available_cash": 0, "updated": ""}
    try:
        with open(_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception:
        return {"total_capital": 0, "available_cash": 0, "updated": ""}


def save_account(data):
    _path = ACCOUNT_PATH
    if not os.path.exists(os.path.dirname(_path)):
        os.makedirs(os.path.dirname(_path), exist_ok=True)
    with open(_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


@synchronized_data
def account_set(total_capital, available_cash=None):
    """设置账户总资金和可用资金"""
    acct = read_account()
    old_capital = acct.get("total_capital", 0)
    acct["total_capital"] = float(total_capital)
    if available_cash is not None:
        acct["available_cash"] = float(available_cash)
    elif old_capital == 0:
        acct["available_cash"] = float(total_capital)
    acct["updated"] = datetime.now().strftime("%Y-%m-%d")
    save_account(acct)
    return {"status": "set", "total_capital": acct["total_capital"], "available_cash": acct["available_cash"]}




def _get_name(symbol):
    """从新浪行情获取股票名称（解决中文乱码问题）。
    注意：失败时返回空字符串''，不要返回symbol本身，否则上层无法判断是否真的修复了。
    """
    try:
        q = _sina_realtime(symbol)
        if q and q.get("名称"):
            return q["名称"]
    except Exception:
        pass
    return ''


# ===================== 22c Risk Stack =====================
# added 2026-09-03 | design 瑶序 | params: 2026-08-27 调研 (瑶序 生存体系 + Nova 测量有效性)
# fail-safe: config file is override layer, embedded defaults are the floor.
_RISK_DEFAULTS = {
    "single_trade_risk_pct": 0.02,
    "daily_circuit_breaker_pct": 0.03,
    "consecutive_loss_halt": 3,
    "min_lot_threshold": 0.5,
}

def _load_risk_config():
    """Merge override file onto embedded defaults. Missing/corrupt file -> defaults (gate never silently off)."""
    cfg = dict(_RISK_DEFAULTS)
    try:
        with open(os.path.join(PLUGIN_DIR, "risk_config.json"), encoding="utf-8") as _rf:
            _override = json.load(_rf)
        if isinstance(_override, dict):
            for _k, _v in _override.items():
                if not str(_k).startswith("_") and _k in cfg:
                    # 22c C-fix (Nova audit r4 + 观澜 rule): config must be sane, not just present
                    if _k in ("single_trade_risk_pct", "daily_circuit_breaker_pct"):
                        if not (isinstance(_v, (int, float)) and not isinstance(_v, bool) and 0 < float(_v) <= 0.1):
                            sys.stderr.write(f"[risk_config] REJECT {_k}={_v!r} outside (0, 0.1] - default kept (fail-safe)\n")
                            continue
                        if float(_v) > 0.03:
                            sys.stderr.write(f"[risk_config] NOTE {_k}={_v} above recommended 2-3% band - risk loosening is a behavior event, logged\n")
                    elif _k == "consecutive_loss_halt":
                        if not (isinstance(_v, int) and not isinstance(_v, bool) and _v >= 1):
                            sys.stderr.write(f"[risk_config] REJECT {_k}={_v!r} (need int>=1) - default kept\n")
                            continue
                    elif _k == "min_lot_threshold":
                        if not (isinstance(_v, (int, float)) and not isinstance(_v, bool) and 0 < float(_v) <= 1):
                            sys.stderr.write(f"[risk_config] REJECT {_k}={_v!r} outside (0, 1] - default kept\n")
                            continue
                    cfg[_k] = _v
    except Exception:
        pass  # fail-safe: defaults hold
    return cfg

def _mk_ex_proof_override(ov):
    return {"proofs": {"p1_sector_shelter": "overridden",
                       "p2_independence": "overridden",
                       "p3_flow_continuity": "overridden"},
            "authority": f"人工终裁override by {ov.get('override_by','?')}: {ov.get('override_reason','')[:80]}"}

def _risk_gate_check(symbol, entry, shares, stop_loss, cfg, override=None):
    """Pre-trade gate. Returns rejection dict (with full calculation for diary citation) or None to pass."""
    # Rule 1: stop_loss must be a valid number below entry
    try:
        _stop = float(stop_loss)
        _valid_stop = 0 < _stop < entry
    except (TypeError, ValueError):
        _valid_stop = False
    if not _valid_stop:
        return {"status": "rejected", "gate": "pre_trade_risk",
                "message": f"拒单: 无有效止损位 (stop_loss={stop_loss}). 止损是风险预算的分母, 无止损不开仓.",
                "calc": {"symbol": symbol, "entry": entry, "shares": shares, "stop_loss": stop_loss}}
    # Rule 6 (V4.2.1): market regime - 大盘状态系数闸 (翔批 2026-09-10)
    _ov = override or {}
    _mf, _mk_trend, _mk_ex = _market_factor(symbol, full_check=True) if not _ov.get("override_market") else (0.5, "空头排列(人工override)", _mk_ex_proof_override(_ov))
    if _mf is None:
        return {"status": "rejected", "gate": "market_regime",
                "message": "拒单: 大盘空头排列且未过豁免三证明(板块庇护/个股独立/资金续流). 弱市建仓需交三份证明. 如需人工override: params带override_market=true+override_by+override_reason.",
                "calc": {"trend": _mk_trend, "exemption": _mk_ex.get("proofs", {}) if _mk_ex else {},
                         "authority": "V4.2.1市场系数闸: Faber板块轮动+RS+T+1续流 (调研2026-09-10)"}}
    # Rule 3 (gate-2): consecutive-loss halt - 连亏停手, 冷静期只平不建
    # 只平不建语义由接线自动满足: 闸仅挂 position_add, position_close 不过闸
    _streak = _consecutive_loss_count()
    _halt_line = int(cfg.get("consecutive_loss_halt", 3))
    if _streak >= _halt_line:
        return {"status": "rejected", "gate": "pre_trade_risk",
                "message": f"拒单: 连亏停手冷静期 - 已连亏{_streak}笔 ≥ 上限{_halt_line}笔. 只平不建(position_close可用). 解除双路径: 盈利平仓自动清零 或 复盘后人工解除(risk_halt_reset, 需evidence).",
                "calc": {"consecutive_losses": _streak, "halt_line": _halt_line,
                         "authority": "行业共识2-3次 + Barber & Odean 2000 (第3次连亏后决策降级)",
                         "note": "仅已实现亏损计数, 浮亏不计 (口径: 观澜 2026-09-03裁定)"}}
    # Rule 4 (gate-2): daily circuit breaker - 日熔断, 次日自愈无需解除
    # 分母用当前total_capital (精确版需当日开盘快照, 过度设计; 误差=当日盈亏量级, 已披露)
    _today_loss = _today_realized_loss()
    if _today_loss < 0:
        _day_cap = read_account().get("total_capital", 0)
        _day_limit = round(cfg["daily_circuit_breaker_pct"] * _day_cap, 2)
        if abs(_today_loss) >= _day_limit:
            return {"status": "rejected", "gate": "pre_trade_risk",
                    "message": f"拒单: 日熔断 - 今日已实现亏损 {abs(_today_loss):.2f}元 ≥ 限额 {_day_limit:.2f}元 ({cfg['daily_circuit_breaker_pct']:.1%}×{_day_cap:.2f}). 明日自动解除.",
                    "calc": {"today_realized_loss": round(_today_loss, 2), "daily_limit": _day_limit,
                             "authority": "Prop Trading 行业准入 3-5% 取下沿",
                             "note": "收盘结算口径浮亏不计(偏松版), 补救=日报浮亏提示行(提醒制)"}}

    # Rule 2: risk budget
    acct = read_account()
    _capital = acct.get("total_capital", 0)
    if _capital <= 0:
        return {"status": "rejected", "gate": "pre_trade_risk",
                "message": "拒单: 账户总资本未知或为0, 无法计算风险预算. 先用 account_set 校准.",
                "calc": {"total_capital": _capital}}
    _risk_amt = (entry - _stop) * shares
    _limit = round(cfg["single_trade_risk_pct"] * _capital * _mf, 2)
    if _risk_amt > _limit and not _ov.get("override_budget"):
        return {"status": "rejected", "gate": "pre_trade_risk",
                "message": f"拒单: 单笔风险 {_risk_amt:.2f} 元 > 限额 {_limit:.2f} 元 (基准{cfg['single_trade_risk_pct']:.1%}×市场系数{_mf:.2f}×{_capital:.2f}——空头时收紧, L1598文案修复Nova r11)",
                "calc": {"symbol": symbol, "entry": entry, "stop_loss": _stop, "shares": shares,
                         "risk_amount": round(_risk_amt, 2), "risk_limit": _limit,
                         "risk_pct_of_capital": round(_risk_amt / _capital, 4),
                         "rule": "single_trade_risk 2% floor"}}

    # Rule 5 (V4.1 2026-09-08): monthly risk cap - 月度风险总闸 (2/6法则下半句)
    # 语义: 活跃持仓总敞口 + 本新仓风险 <= 6% x 总资本. 浮盈锁利仓(止损>=成本)风险归零不占预算.
    _month_cap = round(cfg.get("monthly_risk_cap_pct", 0.06) * _capital, 2)
    _active_ps = [p for p in read_positions() if p.get('status') == 'active']
    _open_risk = sum(max(0, (p.get('cost', 0) - p.get('stop_loss', 0)) * p.get('shares', 0))
                     for p in _active_ps)
    _total_risk = _open_risk + _risk_amt
    if _total_risk > _month_cap:
        return {"status": "rejected", "gate": "pre_trade_risk",
                "message": f"拒单: 月度风险总闸 - 活跃敞口{_open_risk:.2f} + 本单{_risk_amt:.2f} = {_total_risk:.2f}元 > 月限{_month_cap:.2f}元 ({cfg.get('monthly_risk_cap_pct', 0.06):.0%} x {_capital:.2f}). 平掉部分仓位释放预算后可再建.",
                "calc": {"open_risk": round(_open_risk, 2), "this_trade_risk": round(_risk_amt, 2),
                         "total_risk": round(_total_risk, 2), "monthly_cap": _month_cap,
                         "active_positions": len(_active_ps),
                         "authority": "2/6法则 (Elder) 月度总敞口<=6% | 翔批准 2026-09-08"}}
    return None

def _load_risk_state():
    """22c gate-2: manual lift override record. Missing/corrupt file -> no lift (fail-safe: halt STAYS).
    风控默认态是'在' - 解除凭据丢失时停手保持, 与 gate-1 配置默认同哲学."""
    try:
        with open(os.path.join(PLUGIN_DIR, "risk_state.json"), encoding="utf-8") as _sf:
            return json.load(_sf)
    except Exception:
        return {}

def _consecutive_loss_count(trades=None):
    """Trailing consecutive realized losses, chronological by date. Profit close resets to 0.
    口径 (观澜裁定): 仅已实现亏损 - 止损离场计数, 浮亏永不计入.
    Manual lift: only sells strictly AFTER loss_halt_cleared_until count - lift covers the past
    streak only; new losses after that date re-trigger (解除不是免死金牌)."""
    if trades is None:
        trades = read_trades()
    _cleared = str(_load_risk_state().get("loss_halt_cleared_until", ""))
    sells = sorted(
        (t for t in trades
         if t.get("action") == "sell" and "pnl" in t and str(t.get("date", "")) > _cleared),
        key=lambda t: str(t.get("date", "")))
    count = 0
    for t in reversed(sells):
        if float(t.get("pnl", 0)) < 0:
            count += 1
        else:
            break
    return count

def _today_realized_loss(trades=None):
    """Sum of today's realized losses (negative part only) for daily circuit breaker.
    收盘结算口径, 浮亏不计 - 偏松版已披露, 补救为日报浮亏提示行 (提醒制)."""
    if trades is None:
        trades = read_trades()
    _today = datetime.now().strftime("%Y-%m-%d")
    return sum(float(t.get("pnl", 0)) for t in trades
               if t.get("action") == "sell" and t.get("date") == _today
               and float(t.get("pnl", 0)) < 0)

def _risk_halt_reset(cleared_until, reset_by, evidence):
    """Manual lift of loss-halt. Writes override WITH evidence - no evidence, no lift.
    Daily breaker self-heals at date rollover - no reset path by design.
    NOTE: 不进日报白名单 - designed for supervised sessions with 翔 present."""
    try:
        _d = datetime.strptime(str(cleared_until)[:10], "%Y-%m-%d").strftime("%Y-%m-%d")
    except ValueError:
        return {"status": "error", "message": f"cleared_until 日期无效: {cleared_until} (需YYYY-MM-DD)"}
    if not evidence or not str(evidence).strip():
        return {"status": "error", "message": "解除连亏停手必须附evidence(复盘结论/日记指针), 拒绝无凭据解除"}
    state = {"loss_halt_cleared_until": _d,
             "reset_by": str(reset_by or "unknown"),
             "evidence": str(evidence)[:500],
             "reset_at": datetime.now().isoformat(timespec="seconds")}
    with open(os.path.join(PLUGIN_DIR, "risk_state.json"), "w", encoding="utf-8") as _sf:
        json.dump(state, _sf, ensure_ascii=False, indent=2)
    return {"status": "success", "result": state,
            "message": f"连亏停手解除至{_d}: 该日及之前的连亏清零, 之后新亏损重新计数"}

def _position_size(symbol, entry=None, cfg=None):
    """22c: ATR-based position sizer (3/4). 前100条判断期用ATR版公式
    (Nova 2026-08-27: 攒样期凯利输入不可信, ATR版零样本要求).
    公式: shares = risk_budget / (ATR x multiplier); 一手(100股)取整;
    不足半手(50股)舍弃信号 - 不凑单; 资金约束降仓或跳过. 建议仓位, 决策权在翔."""
    if cfg is None:
        cfg = _load_risk_config()
    kline = get_kline_with_indicators(symbol, days=35)
    if "latest" not in kline:
        return {"status": "error", "message": "K线数据不可用, 无法计算ATR"}
    atr = kline["latest"].get("ATR")
    if not atr or float(atr) <= 0:
        return {"status": "error", "message": f"ATR无效: {atr}"}
    close = kline["latest"].get("收盘", 0)
    try:
        price = float(entry) if entry not in (None, "", 0) else float(close)
    except (TypeError, ValueError):
        return {"status": "error", "message": f"entry无效: {entry}"}
    if price <= 0:
        return {"status": "error", "message": f"价格无效: price={price}, close={close}"}
    mult = float(cfg.get("atr_stop_multiplier", 2.0))
    stop_dist = float(atr) * mult
    stop_price = round(price - stop_dist, 2)
    acct = read_account()
    capital = acct.get("total_capital", 0)
    _mf_ps, _trend_ps, _ = _market_factor(symbol, full_check=False)
    budget = round(cfg["single_trade_risk_pct"] * capital * _mf_ps, 2)
    raw_shares = int(budget / stop_dist) if stop_dist > 0 else 0
    shares = (raw_shares // 100) * 100
    min_lot = int(round(float(cfg.get("min_lot_threshold", 0.5)) * 100))
    cash = acct.get("available_cash", 0)
    cash_needed = round(shares * price, 2)
    verdict = "OK"
    if shares < min_lot:
        verdict = "SKIP_SIGNAL"
    elif cash_needed > cash:
        afford = (int(cash / (price * 100))) * 100
        if afford >= min_lot:
            verdict = "DOWNSIZE_CASH"
            shares = afford
            cash_needed = round(shares * price, 2)
        else:
            verdict = "SKIP_CASH"
    risk_amt = round(stop_dist * shares, 2)
    return {"status": "success", "result": {
        "symbol": symbol, "price_ref": price, "ATR": round(float(atr), 4), "multiplier": mult,
        "stop_distance": round(stop_dist, 3), "stop_price": stop_price,
        "risk_budget": budget, "raw_shares": raw_shares,
        "shares_final": shares, "lots": shares // 100, "min_lot": min_lot,
        "cash_needed": cash_needed, "cash_available": cash,
        "final_risk_amount": risk_amt,
        "market_factor": _mf_ps,
        "market_trend": _trend_ps,
        "final_risk_pct": round(risk_amt / capital, 4) if capital else None,
        "verdict": verdict,
        "authority": "Wilder 1978 ATR 2-3x波段下沿 | 2%预算 Van Tharp | 攒样期ATR版判据 Nova 2026-08-27",
        "note": "verdict: OK可下单 / SKIP_SIGNAL不足半手舍弃不凑单 / DOWNSIZE_CASH按资金降仓 / SKIP_CASH资金不够半手. 建议仓位, 终裁在翔"}}

@synchronized_data
def position_add(symbol, name, cost, shares, stop_loss, target, reason="", override_market=None, override_budget=None, override_by=None, override_reason=None):
    positions = read_positions()
    for p in positions:
        if p["symbol"] == symbol and p.get("status") == "active":
            return {"status": "exists", "message": f"{symbol}已有活跃持仓"}

    # === Pre-trade Risk Gate (22c) | 风控闸 | added 2026-09-03 ===
    # Rule 1: no valid stop_loss -> no trade. Rule 2: (entry-stop)*shares <= risk_pct * capital.
    _rc = _load_risk_config()
    _ov_p = {}
    if override_market or override_budget:
        _ov_p = {"override_market": bool(override_market),
                 "override_budget": bool(override_budget),
                 "override_by": str(override_by or ""),
                 "override_reason": str(override_reason or "")}
        if not _ov_p["override_by"] or not _ov_p["override_reason"]:
            return {"status": "rejected", "gate": "override_invalid",
                    "message": "拒单: override需完整四键(override_market/override_budget/override_by/override_reason), 终裁人和理由不得为空."}
    _gate = _risk_gate_check(symbol, float(cost), int(shares), stop_loss, _rc, override=_ov_p)
    if _gate is not None:
        return _gate
    if _ov_p:
        reason = (reason or "") + f" [OVERRIDE:{_ov_p['override_by']}: {_ov_p['override_reason']}]"
    
    if not name or name == symbol or '?' in str(name):
        name = _get_name(symbol) or symbol  # 获取失败时用代码兜底
    
    today = datetime.now().strftime("%Y-%m-%d")
    
    positions.append({
        "symbol": symbol,
        "name": name,
        "cost": float(cost),
        "shares": int(shares),
        "stop_loss": float(stop_loss),
        "target": float(target),
        "entry_date": today,
        "added": today,
        "entry_reason": reason,
        "status": "active"
    })
    save_positions(positions)
    
    # === 扣减可用资金 (真实费率 v3.2.1) ===
    # 佣金：可配置（默认万2.5，最低5元），股票/ETF分别设置
    comm_rate = float(os.environ.get("BROKER_COMMISSION_ETF", 0.00025)) if symbol.startswith(('5', '159')) else float(os.environ.get("BROKER_COMMISSION_STOCK", 0.00025))
    comm_fee = max(float(cost) * int(shares) * comm_rate, 5)
    # 过户费：沪市双边万0.1
    transfer_fee = float(cost) * int(shares) * 0.00001 if symbol.startswith(('6', '5', '9', '11', '13')) else 0
    total_fee = round(comm_fee + transfer_fee, 2)
    # 真实摊薄成本 = (买入金额 + 手续费) / 股数
    actual_cost = round((float(cost) * int(shares) + total_fee) / int(shares), 4)
    positions[-1]["cost"] = actual_cost  # 更新刚追加的持仓成本
    save_positions(positions)
    cost_total = float(cost) * int(shares) + total_fee
    acct = read_account()
    if acct.get("total_capital", 0) > 0:
        acct["available_cash"] = round(acct.get("available_cash", 0) - cost_total, 2)
        acct["updated"] = today
        save_account(acct)
    
    trades = read_trades()
    trades.append({
        "symbol": symbol,
        "name": name,
        "action": "buy",
        "price": float(cost),
        "shares": int(shares),
        "date": today,
        "reason": reason
    })
    save_trades(trades)
    
    return {"status": "added", "message": f"已添加持仓 {name}({symbol}) 成本{cost} 数量{shares} 止损{stop_loss} 目标{target}", "trades_updated": True}


@synchronized_data
def position_close(symbol, sell_price, shares=None, reason="", commission=5):
    positions = read_positions()
    pos = None
    for p in positions:
        if p["symbol"] == symbol and p.get("status") == "active":
            pos = p
            break
    
    if not pos:
        return {"status": "not_found", "message": f"{symbol}无活跃持仓"}
    
    sell_price = float(sell_price)
    cost = pos["cost"]
    # 数量解析：None/缺省=全部，0=无效，负数=无效
    if shares is not None:
        close_shares = int(shares)
    else:
        close_shares = pos["shares"]
    # 数量上限保护：卖出数量不超过实际持仓
    if close_shares > pos["shares"]:
        close_shares = pos["shares"]
    if close_shares <= 0:
        return {"status": "error", "message": f"卖出数量无效(shares={shares})"}
    today = datetime.now().strftime("%Y-%m-%d")
    
    # === 真实A股费率计算引擎 v3.2.1 ===
    # 1. 佣金：可配置（默认万2.5，最低5元），股票/ETF分别设置
    comm_rate = float(os.environ.get("BROKER_COMMISSION_ETF", 0.00025)) if symbol.startswith(('5', '159')) else float(os.environ.get("BROKER_COMMISSION_STOCK", 0.00025))
    raw_amount = sell_price * close_shares
    comm_fee = max(raw_amount * comm_rate, 5)
    # 2. 印花税：千1(0.1%)，仅股票卖出收取，ETF免收
    stamp_tax = raw_amount * 0.001 if not symbol.startswith(('5', '159')) else 0
    # 3. 过户费：万0.1(0.001%)，沪市双边收取，深市免收
    transfer_fee = raw_amount * 0.00001 if symbol.startswith(('6', '5', '9', '11', '13')) else 0
    # 卖出净到手金额
    total_fee = round(comm_fee + stamp_tax + transfer_fee, 2)
    return_total = raw_amount - total_fee
    # 真实盈亏 = 净到手 - 买入总成本
    cost_basis_total = cost * close_shares
    pnl = round(return_total - cost_basis_total, 2)
    pnl_pct = round((return_total - cost_basis_total) / cost_basis_total * 100, 2)
    
    entry_date = pos.get("entry_date", pos.get("added", today))
    try:
        d1 = datetime.strptime(entry_date, "%Y-%m-%d")
        d2 = datetime.strptime(today, "%Y-%m-%d")
        hold_days = (d2 - d1).days
    except Exception:
        hold_days = 0
    
    trades = read_trades()
    trades.append({
        "symbol": symbol,
        "name": pos.get("name", symbol),
        "action": "sell",
        "price": sell_price,
        "shares": close_shares,
        "date": today,
        "commission": commission,
        "cost_basis": cost,
        "pnl": pnl,
        "pnl_pct": pnl_pct,
        "hold_days": hold_days,
        "reason": reason
    })
    save_trades(trades)
    
    # 检查是否为部分减仓
    if close_shares < pos["shares"]:
        # 部分减仓：保留剩余持仓，更新数量+重算摊薄成本
        original_total_cost = cost * pos["shares"]
        remaining_shares = pos["shares"] - close_shares
        if remaining_shares > 0:
            diluted_cost = round((original_total_cost - return_total) / remaining_shares, 4)
            pos["cost"] = diluted_cost
        pos["shares"] = remaining_shares
        save_positions(positions)
        
        # 返还可用资金（使用真实费率计算的净到手金额）
        acct = read_account()
        if acct.get("total_capital", 0) > 0:
            acct["available_cash"] = round(acct.get("available_cash", 0) + return_total, 2)
            acct["updated"] = today
            save_account(acct)
        
        result_str = "盈利" if pnl > 0 else "亏损"
        return {
            "status": "partial_closed",
            "message": f"部分减仓 {pos.get('name', symbol)}({symbol}) 卖出价{sell_price} 卖出{close_shares}股 {result_str}{abs(pnl)}元({pnl_pct}%) 持仓{hold_days}天。剩余{pos['shares']}股",
            "pnl": pnl,
            "pnl_pct": pnl_pct,
            "hold_days": hold_days,
            "remaining_shares": pos["shares"]
        }
    
    # 全部平仓
    pos["status"] = "closed"
    pos["closed"] = today
    pos["sell_price"] = sell_price
    pos["pnl"] = pnl
    save_positions(positions)
    
    # 返还可用资金（使用真实费率计算的净到手金额）
    acct = read_account()
    if acct.get("total_capital", 0) > 0:
        acct["available_cash"] = round(acct.get("available_cash", 0) + return_total, 2)
        acct["updated"] = today
        save_account(acct)
    
    result_str = "盈利" if pnl > 0 else "亏损"
    return {
        "status": "closed",
        "message": f"已平仓 {pos.get('name', symbol)}({symbol}) 卖出价{sell_price} {result_str}{abs(pnl)}元({pnl_pct}%) 持仓{hold_days}天",
        "pnl": pnl,
        "pnl_pct": pnl_pct,
        "hold_days": hold_days
    }


@synchronized_data
def position_update(symbol, stop_loss=None, target=None):
    """更新活跃持仓的风控参数（止损/目标价）"""
    positions = read_positions()
    found = False
    for pos in positions:
        if pos.get("symbol") == symbol and pos.get("status") == "active":
            if stop_loss is not None:
                pos["stop_loss"] = float(stop_loss)
                pos["atr_stop_loss"] = float(stop_loss)
            if target is not None:
                pos["target"] = float(target)
            found = True
            break
    if not found:
        return {"status": "not_found", "message": f"{symbol}无活跃持仓"}
    save_positions(positions)
    return {"status": "success", "message": f"{symbol} 风控参数已更新", "position": pos}

@synchronized_data
def position_remove(symbol):
    positions = read_positions()
    found = False
    for p in positions:
        if p["symbol"] == symbol and p.get("status") == "active":
            p["status"] = "closed"
            p["closed"] = datetime.now().strftime("%Y-%m-%d")
            found = True
    if not found:
        return {"status": "not_found", "message": f"{symbol}无活跃持仓"}
    save_positions(positions)
    return {"status": "removed", "message": f"已平仓 {symbol}（旧版接口，建议用position_close记录盈亏）"}


@synchronized_data
def position_show():
    positions = read_positions()
    active = [p for p in positions if p.get("status") == "active"]
    # 自动修复乱码名称
    changed = False
    for p in active:
        if '?' in str(p.get('name', '')):
            new_name = _get_name(p['symbol'])
            if new_name and '?' not in new_name:
                p['name'] = new_name
                changed = True
    if changed:
        save_positions(positions)
    return {"count": len(active), "positions": active}


def trade_history(symbol=None):
    trades = read_trades()
    if symbol:
        trades = [t for t in trades if t.get("symbol") == symbol]
    return {"count": len(trades), "trades": trades}


def trade_stats():
    trades = read_trades()
    sells = [t for t in trades if t.get("action") == "sell"]
    
    if not sells:
        return {"total_trades": 0, "message": "暂无已平仓交易"}
    
    total_pnl = sum(t.get("pnl", 0) for t in sells)
    wins = [t for t in sells if t.get("pnl", 0) > 0]
    losses = [t for t in sells if t.get("pnl", 0) < 0]
    win_rate = round(len(wins) / len(sells) * 100, 1) if sells else 0
    avg_hold = round(sum(t.get("hold_days", 0) for t in sells) / len(sells), 1) if sells else 0
    
    best = max(sells, key=lambda x: x.get("pnl", 0)) if sells else None
    worst = min(sells, key=lambda x: x.get("pnl", 0)) if sells else None
    
    return {
        "total_sells": len(sells),
        "win_rate": win_rate,
        "wins": len(wins),
        "losses": len(losses),
        "total_pnl": round(total_pnl, 2),
        "avg_hold_days": avg_hold,
        "best": {"name": best.get("name"), "pnl": best.get("pnl"), "pct": best.get("pnl_pct")} if best else None,
        "worst": {"name": worst.get("name"), "pnl": worst.get("pnl"), "pct": worst.get("pnl_pct")} if worst else None,
    }



@synchronized_data
def _calc_atr_trailing_stop(symbol, current_stop, price, multiplier=2.5, hwm=None):
    """V4.2吊灯止损+渐进收紧(2026-09-08): hwm=持仓期最高价(LeBeau吊灯锚). 回撤<1xATR用3.0倍/1-2x用2.5/>2x用2.0(经典3->2->1的A股波段宽版, 1.0x对深盈单=即时死刑). hwm空->回退现价锚定旧逻辑. 棘轮只上移"""
    try:
        kline = get_kline_with_indicators(symbol, days=35)
        if "latest" not in kline:
            return current_stop
        atr = kline["latest"].get("ATR")
        if not atr or atr <= 0 or not _PTA_AVAILABLE:
            return current_stop
        if hwm and hwm > 0:
            anchor = max(hwm, price)
            dd_atr = (anchor - price) / atr
            mult = 3.0 if dd_atr < 1 else (2.5 if dd_atr < 2 else 2.0)
            atr_stop = round(anchor - mult * atr, 2)
        else:
            atr_stop = round(price - multiplier * atr, 2)
        # 只上移不下移
        if atr_stop > current_stop:
            return atr_stop
        return current_stop
    except Exception:
        return current_stop


@synchronized_data
def update_trailing_stops():
    """批量更新所有活跃持仓的ATR跟踪止损线"""
    positions = read_positions()
    active = [p for p in positions if p.get("status") == "active"]
    if not active:
        return {"updated": 0, "message": "无活跃持仓"}
    
    symbols = [p["symbol"] for p in active]
    quotes = _sina_batch_quotes(symbols)
    quote_map = {q.get("代码"): q for q in quotes}
    
    updated = 0
    changes = []
    for p in active:
        sym = p["symbol"]
        old_stop = p.get("stop_loss", 0)
        q = quote_map.get(sym, {})
        price = float(q.get("最新价", 0) or 0)
        if price <= 0:
            continue
        # V4.2: HWM回填(首次K线回溯, 失败兜底当日高) + 每日维护
        day_high = float(q.get("最高", 0) or 0)
        hwm = p.get("hwm", 0)
        if not hwm:
            try:
                kdf = _sina_kline(sym, 120)
                entry_dt = str(p.get("entry_date", ""))
                if kdf is not None and hasattr(kdf, "columns") and len(kdf) > 0 and entry_dt:
                    hi_col = "最高" if "最高" in kdf.columns else ("high" if "high" in kdf.columns else None)
                    dt_col = "日期" if "日期" in kdf.columns else ("date" if "date" in kdf.columns else None)
                    if hi_col and dt_col:
                        after = kdf[kdf[dt_col].astype(str) >= entry_dt]
                        if len(after) > 0:
                            hwm = float(after[hi_col].max())
            except Exception:
                hwm = 0
            if not hwm or hwm <= 0:
                hwm = day_high if day_high > 0 else price
        hwm = max(hwm, day_high, price)
        p["hwm"] = hwm
        new_stop = _calc_atr_trailing_stop(sym, old_stop, price, hwm=hwm)
        if new_stop != old_stop:
            p["stop_loss"] = new_stop
            updated += 1
            changes.append({
                "symbol": sym,
                "name": p.get("name", sym),
                "old_stop": old_stop,
                "new_stop": new_stop,
                "change_pct": round((new_stop - old_stop) / old_stop * 100, 2)
            })
    
    if active:
        save_positions(positions)  # V4.2: hwm每日维护需落盘
    
    return {
        "updated": updated,
        "total": len(active),
        "changes": changes
    }


@synchronized_data
def portfolio_summary():
    """组合概览：持仓+实时价格+盈亏+距止损（含ATR动态止损展示）"""
    positions = read_positions()
    active = [p for p in positions if p.get("status") == "active"]
    if not active:
        return {"count": 0, "positions": []}
    symbols = [p["symbol"] for p in active]
    quotes = _sina_batch_quotes(symbols)
    quote_map = {q.get("代码"): q for q in quotes}
    results = []
    for p in active:
        sym = p["symbol"]
        cost = p["cost"]
        stop = p["stop_loss"]
        target = p["target"]
        q = quote_map.get(sym, {})
        price = float(q.get("最新价", 0) or 0)
        # ATR动态止损参考（只读不写）
        atr_stop = _calc_atr_trailing_stop(sym, stop, price) if price > 0 else stop
        if price > 0 and cost > 0:
            pnl_pct = round((price - cost) / cost * 100, 2)
            dist_stop = round((price - stop) / stop * 100, 2) if stop > 0 else None
            dist_atr_stop = round((price - atr_stop) / atr_stop * 100, 2) if atr_stop > 0 else None
            dist_target = round((target - price) / target * 100, 2) if target > 0 else None
        else:
            pnl_pct = None
            dist_stop = None
            dist_atr_stop = None
            dist_target = None
        warning = ""
        if dist_stop is not None and dist_stop < 3:
            warning = f"距止损仅{dist_stop}%"
        results.append({
            "symbol": sym, "name": p.get("name", sym), "cost": cost, "price": price,
            "shares": p["shares"], "pnl_pct": pnl_pct, "stop_loss": stop, "target": target,
            "atr_stop_loss": atr_stop, "dist_stop_pct": dist_stop, "dist_atr_stop_pct": dist_atr_stop,
            "dist_target_pct": dist_target,
            "warning": warning, "change_pct": float(q.get("涨跌幅", 0) or 0)
        })
    # 计算总览
    total_market_value = sum(r.get("price", 0) * r.get("shares", 0) for r in results)
    acct = read_account()
    available_cash = acct.get("available_cash", 0)
    total_capital = acct.get("total_capital", 0)
    total_assets = round(total_market_value + available_cash, 2)
    total_pnl = round(total_assets - total_capital, 2) if total_capital > 0 else None
    total_pnl_pct = round(total_pnl / total_capital * 100, 2) if total_capital > 0 else None
    
    return {
        "count": len(results),
        "positions": results,
        "account": {
            "total_capital": total_capital,
            "available_cash": round(available_cash, 2),
            "market_value": round(total_market_value, 2),
            "total_assets": total_assets,
            "total_pnl": total_pnl,
            "total_pnl_pct": total_pnl_pct
        }
    }


# ========== 行情与指标 ==========

def get_realtime_quote(symbol):
    try:
        result = _sina_realtime(symbol)
        if result:
            return result
        return {"error": f"未找到 {symbol}"}
    except Exception as e:
        return {"error": str(e)[:80]}


def get_batch_quotes(symbols):
    try:
        results = _sina_batch_quotes(symbols)
        return {"stocks": results, "count": len(results)}
    except Exception as e:
        return {"error": str(e)[:80]}


def _sf(val):
    if val is None or (isinstance(val, float) and (val != val)):
        return None
    return round(float(val), 2)


def _ma_align(latest):
    ma5, ma10, ma20 = latest.get('MA5'), latest.get('MA10'), latest.get('MA20')
    if any(v is None or (isinstance(v, float) and (v != v)) for v in [ma5, ma10, ma20]):
        return "数据不足"
    if ma5 > ma10 > ma20:
        return "多头排列"
    elif ma5 < ma10 < ma20:
        return "空头排列"
    return "交叉缠绕"


def get_kline_with_indicators(symbol, days=120):
    try:
        # 优先用新浪K线API（秒级响应）
        df = _sina_kline(symbol, datalen=days)
        
        # 新浪失败时降级到AKShare
        if df is None or df.empty:
            sz_code = f"sz{symbol}" if symbol.startswith(('0', '3')) else f"sh{symbol}"
            df = safe_request(ak.stock_zh_a_daily, symbol=sz_code, adjust="qfq")
        
        if df is None or df.empty:
            return {"error": f"未获取到 {symbol} K线"}

        df = df.tail(days).copy()
        df['date'] = df['date'].astype(str)
        close = df['close'].astype(float)
        high = df['high'].astype(float) if 'high' in df.columns else close
        low = df['low'].astype(float) if 'low' in df.columns else close
        volume = df['volume'].astype(float) if 'volume' in df.columns else pd.Series([0]*len(df))

        for w in [5, 10, 20, 60]:
            df[f'MA{w}'] = close.rolling(window=w).mean().round(2)

        ema12 = close.ewm(span=12, adjust=False).mean()
        ema26 = close.ewm(span=26, adjust=False).mean()
        dif = (ema12 - ema26).round(3)
        dea = dif.ewm(span=9, adjust=False).mean().round(3)
        df['MACD_DIF'] = dif
        df['MACD_DEA'] = dea
        df['MACD'] = ((dif - dea) * 2).round(3)

        delta = close.diff()
        gain = delta.where(delta > 0, 0)
        loss = (-delta).where(delta < 0, 0)
        avg_gain = gain.rolling(window=14).mean()
        avg_loss = loss.rolling(window=14).mean()
        rs = avg_gain / avg_loss.replace(0, np.nan)
        df['RSI'] = (100 - (100 / (1 + rs))).round(2)

        bb_mid = close.rolling(window=20).mean()
        bb_std = close.rolling(window=20).std()
        df['BOLL_UP'] = (bb_mid + 2 * bb_std).round(2)
        df['BOLL_MID'] = bb_mid.round(2)
        df['BOLL_DN'] = (bb_mid - 2 * bb_std).round(2)

        if _PTA_AVAILABLE:
            # pandas-ta 模式：计算 KDJ, OBV, ATR, WR, CCI
            stoch_df = ta.stoch(high, low, close, k=9, d=3, smooth_k=3)
            if stoch_df is not None and not stoch_df.empty:
                df['KDJ_K'] = stoch_df.iloc[:, 0].round(2)
                df['KDJ_D'] = stoch_df.iloc[:, 1].round(2)
                df['KDJ_J'] = (3 * df['KDJ_K'] - 2 * df['KDJ_D']).round(2)
            else:
                df['KDJ_K'] = np.nan; df['KDJ_D'] = np.nan; df['KDJ_J'] = np.nan

            obv_s = ta.obv(close, volume)
            df['OBV'] = obv_s.round(0) if obv_s is not None else pd.Series([0]*len(df))

            atr_s = ta.atr(high, low, close, length=14)
            df['ATR'] = atr_s.round(2) if atr_s is not None else pd.Series([0]*len(df))

            wr_s = ta.willr(high, low, close, length=14)
            df['WR'] = wr_s.round(2) if wr_s is not None else pd.Series([-50]*len(df))

            cci_s = ta.cci(high, low, close, length=14)
            df['CCI'] = cci_s.round(2) if cci_s is not None else pd.Series([0]*len(df))
        else:
            # 降级模式：填充 NaN
            df['KDJ_K'] = np.nan; df['KDJ_D'] = np.nan; df['KDJ_J'] = np.nan
            df['OBV'] = np.nan; df['ATR'] = np.nan; df['WR'] = np.nan; df['CCI'] = np.nan

        latest = df.iloc[-1]
        rsi_val = float(latest.get('RSI', 50)) if latest.get('RSI') is not None and not (isinstance(latest.get('RSI'), float) and (latest.get('RSI') != latest.get('RSI'))) else 50.0

        macd_signal = "无明显信号"
        if len(df) >= 3:
            h1 = df['MACD'].iloc[-1]
            h2 = df['MACD'].iloc[-2]
            if h2 < 0 and h1 > 0:
                macd_signal = "金叉（偏多）"
            elif h2 > 0 and h1 < 0:
                macd_signal = "死叉（偏空）"

        rsi_judge = "超买区" if rsi_val > 70 else ("超卖区" if rsi_val < 30 else "中性区")

        # 新增指标判断 (仅 pandas-ta 模式有效)
        kdj_k = _sf(latest.get('KDJ_K'))
        kdj_d = _sf(latest.get('KDJ_D'))
        kdj_j = _sf(latest.get('KDJ_J'))
        kdj_judge = "未启用"
        if _PTA_AVAILABLE and kdj_j is not None:
            if kdj_j > 100: kdj_judge = "超买区(J>100)"
            elif kdj_j < 0: kdj_judge = "超卖区(J<0)"
            elif kdj_k > 80 and kdj_d > 80: kdj_judge = "高位区"
            elif kdj_k < 20 and kdj_d < 20: kdj_judge = "低位区"
            else: kdj_judge = "中性区"

        wr_val = _sf(latest.get('WR'))
        wr_judge = "未启用"
        if _PTA_AVAILABLE and wr_val is not None:
            wr_judge = "超买区" if wr_val > -20 else ("超卖区" if wr_val < -80 else "中性区")

        cci_val = _sf(latest.get('CCI'))
        cci_judge = "未启用"
        if _PTA_AVAILABLE and cci_val is not None:
            cci_judge = "超买区" if cci_val > 100 else ("超卖区" if cci_val < -100 else "中性区")

        recent = []
        for _, row in df.tail(3).iterrows():
            recent.append({
                "日期": str(row['date']),
                "收盘": round(float(row['close']), 2),
                "成交量": int(row['volume']) if row.get('volume') is not None else 0,
            })

        return {
            "symbol": symbol,
            "latest": {
                "日期": str(latest['date']),
                "收盘": round(float(latest['close']), 2),
                "MA5": _sf(latest.get('MA5')),
                "MA10": _sf(latest.get('MA10')),
                "MA20": _sf(latest.get('MA20')),
                "MA60": _sf(latest.get('MA60')),
                "MACD_DIF": _sf(latest.get('MACD_DIF')),
                "MACD_DEA": _sf(latest.get('MACD_DEA')),
                "MACD柱": _sf(latest.get('MACD')),
                "RSI": round(rsi_val, 1),
                "BOLL上": _sf(latest.get('BOLL_UP')),
                "BOLL中": _sf(latest.get('BOLL_MID')),
                "BOLL下": _sf(latest.get('BOLL_DN')),
                "ATR": _sf(latest.get('ATR')),  # M5 fix 2026-09-03 (Nova audit r5): ATR computed in df since v3.x but never boxed - sizer & trailing-stop both read None
                "KDJ_K": _sf(latest.get('KDJ_K')),  # col verified 2026-09-04 L2128
                "KDJ_D": _sf(latest.get('KDJ_D')),  # L2129
                "KDJ_J": _sf(latest.get('KDJ_J')),  # L2130
                "OBV": _sf(latest.get('OBV')),  # L2135
                "WR": _sf(latest.get('WR')),  # L2141 willr range -100~0
                "CCI": _sf(latest.get('CCI'))   # L2144
            },
            "summary": {
                "MACD信号": macd_signal,
                "RSI状态": rsi_judge,
                "均线排列": _ma_align(latest),
            },
            "recent_3days": recent
        }
    except Exception as e:
        return {"error": str(e)[:80]}


def get_stock_info(symbol):
    try:
        result = {}
        # Tushare daily_basic
        basic = _get_daily_basic(symbol)
        if basic:
            total_mv = basic.get('total_mv')
            circ_mv = basic.get('circ_mv')
            result.update({
                "股票简称": symbol,
                "PE(TTM)": round(basic.get('pe_ttm', 0) or 0, 1),
                "PB": round(basic.get('pb', 0) or 0, 2),
                "总市值(亿)": round(total_mv / 10000, 1) if total_mv else None,
                "流通市值(亿)": round(circ_mv / 10000, 1) if circ_mv else None,
                "换手率": round(basic.get('turnover_rate', 0) or 0, 2),
                "量比": round(basic.get('volume_ratio', 0) or 0, 2),
                "股息率": round(basic.get('dv_ratio', 0) or 0, 2),
                "数据日期": basic.get('trade_date', ''),
                "数据源": "Tushare"
            })
        # 新浪实时行情补充
        quote = _sina_realtime(symbol)
        if quote:
            result["股票简称"] = quote.get("名称", symbol)
            result["最新价"] = quote.get("最新价", 0)
            result["涨跌幅"] = quote.get("涨跌幅", 0)
            result["成交额"] = quote.get("成交额", 0)
        return result if result else {"error": f"未找到 {symbol}"}
    except Exception as e:
        return {"error": str(e)[:60]}


def _em_market_code(symbol):
    """东方财富市场代码"""
    if symbol.startswith('6'):
        return f"1.{symbol}"
    else:
        return f"0.{symbol}"


def _get_etf_flow(symbol):
    """ETF资金流向（AKShare fund_etf_spot_em实时快照）"""
    try:
        df = safe_request(ak.fund_etf_spot_em)
        if df is None or df.empty:
            return None
        row = df[df['代码'].astype(str) == str(symbol)]
        if row.empty:
            return None
        r = row.iloc[0]

        def _safe_float(val, divide=1):
            try:
                return round(float(val or 0) / divide, 2)
            except:
                return 0

        return {
            "symbol": symbol,
            "name": str(r.get('名称', symbol)),
            "latest_flow": {
                "日期": str(r.get('数据日期', ''))[:10],
                "主力净流入": _safe_float(r.get('主力净流入-净额'), 10000),
                "超大单净流入": _safe_float(r.get('超大单净流入-净额'), 10000),
                "大单净流入": _safe_float(r.get('大单净流入-净额'), 10000),
                "中单净流入": _safe_float(r.get('中单净流入-净额'), 10000),
                "小单净流入": _safe_float(r.get('小单净流入-净额'), 10000),
            },
            "recent_flow": [{
                "日期": str(r.get('数据日期', ''))[:10],
                "主力净流入": _safe_float(r.get('主力净流入-净额'), 10000),
                "超大单净流入": _safe_float(r.get('超大单净流入-净额'), 10000),
                "大单净流入": _safe_float(r.get('大单净流入-净额'), 10000),
                "中单净流入": _safe_float(r.get('中单净流入-净额'), 10000),
                "小单净流入": _safe_float(r.get('小单净流入-净额'), 10000),
            }],
            "summary": {
                "主力净流入万": _safe_float(r.get('主力净流入-净额'), 10000),
                "超大单净流入万": _safe_float(r.get('超大单净流入-净额'), 10000),
                "大单净流入万": _safe_float(r.get('大单净流入-净额'), 10000),
                "方向": "主力流入" if _safe_float(r.get('主力净流入-净额')) > 0 else "主力流出",
                "换手率": _safe_float(r.get('换手率')),
                "折价率": _safe_float(r.get('基金折价率')),
                "净份额(亿)": _safe_float(r.get('最新份额'), 100000000),
            },
            "_source": "AKShare(ETF现货)"
        }
    except Exception as e:
        log(f"ETF资金流向获取失败: {e}")
        return None


def get_capital_flow(symbol):
    """资金流向 — ETF走fund_etf_spot_em，个股走Tushare moneyflow"""
    # ETF代码检测：5开头(沪市ETF)或159开头(深市ETF)
    if symbol.startswith('5') or symbol.startswith('159'):
        etf_result = _get_etf_flow(symbol)
        if etf_result:
            return etf_result
        return {"error": f"ETF {symbol} 资金流向获取失败（fund_etf_spot_em无数据）"}
    try:
        ts_code = _ts_code(symbol)
        data = _tushare_api('moneyflow',
            {'ts_code': ts_code, 'limit': '5'},
            'ts_code,trade_date,buy_sm_amount,sell_sm_amount,buy_md_amount,sell_md_amount,buy_lg_amount,sell_lg_amount,buy_elg_amount,sell_elg_amount,net_mf_amount')
        if not data or not data.get('items'):
            log(f"Tushare moneyflow无数据({symbol})，尝试AKShare容灾")
            ak_result = _ak_capital_flow(symbol)
            if ak_result:
                return ak_result
            return {"error": f"未获取到 {symbol} 资金流向（Tushare+AKShare均无数据，ETF可能不覆盖）"}
        fields = data.get('fields', [])
        recent_flow = []
        for item in data['items']:
            row = dict(zip(fields, item))
            trade_date = row.get('trade_date', '')
            formatted_date = f"{trade_date[:4]}-{trade_date[4:6]}-{trade_date[6:]}" if len(trade_date) == 8 else trade_date
            sm_net = round(float(row.get('buy_sm_amount', 0) or 0) - float(row.get('sell_sm_amount', 0) or 0), 2)
            md_net = round(float(row.get('buy_md_amount', 0) or 0) - float(row.get('sell_md_amount', 0) or 0), 2)
            lg_net = round(float(row.get('buy_lg_amount', 0) or 0) - float(row.get('sell_lg_amount', 0) or 0), 2)
            elg_net = round(float(row.get('buy_elg_amount', 0) or 0) - float(row.get('sell_elg_amount', 0) or 0), 2)
            main_net = round(float(row.get('net_mf_amount', 0) or 0), 2)
            entry = {
                "日期": formatted_date,
                "主力净流入": main_net,
                "小单净流入": sm_net,
                "中单净流入": md_net,
                "大单净流入": lg_net,
                "超大单净流入": elg_net,
            }
            recent_flow.append(entry)
        latest = recent_flow[0] if recent_flow else {}
        return {
            "symbol": symbol,
            "latest_flow": latest,
            "recent_flow": recent_flow,
            "summary": {
                "主力净流入万": latest.get("主力净流入", 0),
                "超大单净流入万": latest.get("超大单净流入", 0),
                "大单净流入万": latest.get("大单净流入", 0),
                "方向": "主力流入" if latest.get("主力净流入", 0) > 0 else "主力流出"
            }
        }
    except Exception as e:
        return {"error": f"资金流向获取失败: {str(e)[:60]}"}


def get_sector_ranking():
    """Tushare申万行业涨跌排名（替代已封禁的东方财富push2）"""
    try:
        # Step1: 拿31个申万一级行业
        ind_data = _tushare_api('index_classify',
            {'level': 'L1', 'src': 'SW2021'},
            'index_code,industry_name')
        if not ind_data or not ind_data.get('items'):
            log("Tushare申万行业列表获取失败，尝试AKShare容灾")
            ak_result = _ak_sector_ranking()
            if ak_result:
                return ak_result
            return {"error": "板块排名获取失败（Tushare+AKShare均无数据）"}
        
        industries = ind_data.get('items', [])
        
        # Step2: 批量拉涨跌幅 (M9修复2026-09-07: index_daily对申万代码静默0行, 改走申万官网 _sw_hist)
        results = []
        for code, name in industries:
            time.sleep(0.15)
            rows = _sw_hist(code, tail_n=2)
            if rows and len(rows) >= 2:
                prev, last = rows[-2], rows[-1]
                pct = (last['close'] / prev['close'] - 1) * 100 if prev['close'] else 0.0
                results.append({"板块名称": name, "涨跌幅": round(pct, 2), "数据日期": last['date']})
        
        if not results:
            return {"error": "板块涨跌幅数据获取失败(申万官网亦失败; 三路全断: index_daily覆盖外/sw_daily积分墙/东财容灾封禁)"}
        
        results.sort(key=lambda x: x["涨跌幅"], reverse=True)
        top3 = results[:3]
        bot3 = results[-3:]
        return {"涨幅前3": top3, "跌幅前3": bot3, "数据源": "Tushare(申万一级)"}
    except Exception as e:
        return {"error": f"板块排名获取失败: {str(e)[:60]}"}


# ========== 增强异动扫描 ==========

SEVERITY_ORDER = {"normal": 0, "medium": 1, "high": 2, "critical": 3}


def _max_severity(current, new):
    if SEVERITY_ORDER.get(new, 0) > SEVERITY_ORDER.get(current, 0):
        return new
    return current


def get_hs300_change():
    """沪深300今日涨跌幅（Tushare主→AKShare容灾）"""
    try:
        data = _tushare_api('index_daily',
            {'ts_code': '000300.SH', 'limit': '1'},
            'ts_code,trade_date,close,pct_chg')
        if data and data.get('items'):
            return float(data['items'][0][3] or 0)
    except Exception:
        pass
    # AKShare容灾
    try:
        df = safe_request(ak.stock_zh_index_daily, symbol='sh000300')
        if df is not None and len(df) >= 2:
            c1 = float(df.iloc[-2].get('close', 0) or 0)
            c2 = float(df.iloc[-1].get('close', 0) or 0)
            if c1 > 0:
                return round((c2 - c1) / c1 * 100, 2)
    except Exception as e:
        log(f"AKShare沪深300容灾失败: {e}")
    return 0.0


def scan_anomalies_enhanced(symbols_override=None):
    """增强版异动扫描 - 7类检测"""
    if symbols_override:
        watchlist = [{"code": s, "name": s} for s in symbols_override]
    else:
        watchlist = read_watchlist()

    if not watchlist:
        return {
            "scan_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "total": 0, "anomaly_count": 0, "normal_count": 0,
            "anomalies": [],
            "message": "自选股列表为空，请先通过 watchlist_add 添加自选股"
        }

    symbols = [s["code"] for s in watchlist]

    # 1. 批量实时行情（新浪源）
    try:
        df_all = _get_spot_data()
        if df_all is None:
            return {"error": "全市场行情数据获取失败(新浪源)"}
    except Exception as e:
        return {"error": f"行情数据获取失败: {str(e)[:80]}"}

    # 2. 沪深300涨跌幅
    hs300_change = get_hs300_change()

    anomalies = []
    normal_count = 0

    for item in watchlist:
        sym = item["code"]
        sym_name = item.get("name", sym)

        row = df_all[df_all['代码'] == sym]
        if row.empty:
            normal_count += 1
            continue

        r = row.iloc[0]

        # 提取实时数据
        pct = float(r.get('涨跌幅', 0) or 0)
        price = round(float(r.get('最新价', 0) or 0), 2)
        vol_ratio = float(r.get('量比', 0) or 0)
        turnover = float(r.get('换手率', 0) or 0)
        high = round(float(r.get('最高', 0) or 0), 2)
        prev_close = round(float(r.get('昨收', 0) or 0), 2)
        flow_mv = float(r.get('流通市值', 0) or 0)

        alert = {
            "code": sym,
            "name": sym_name,
            "price": price,
            "change_pct": round(pct, 2),
            "volume_ratio": round(vol_ratio, 1),
            "turnover_rate": round(turnover, 1),
            "anomaly_types": [],
            "severity": "normal",
            "details": []
        }

        # ===== Tier 1: 立即通知 =====

        # 涨跌停逼近 (≥±8%)
        if abs(pct) >= 8.0:
            alert["anomaly_types"].append("涨跌停逼近")
            alert["severity"] = "critical"
            d = "逼近涨停" if pct > 0 else "逼近跌停"
            alert["details"].append(f"{d}，涨跌幅{pct:+.2f}%")

        # 放量标记（后续结合MA判断）
        heavy_volume = vol_ratio >= 2.5  # V4.1: 突破确认级2.5-3倍(原2.0偏松)

        # ===== Tier 2: 盘中汇总 =====

        # 涨跌幅偏离大盘 (≥±3%)
        deviation = pct - hs300_change
        if abs(deviation) >= 3.0:
            alert["anomaly_types"].append("独立走势")
            alert["severity"] = _max_severity(alert["severity"], "medium")
            alert["details"].append(f"偏离沪深300 {deviation:+.2f}%")

        # 换手率异动 (>10%)
        if turnover >= 10.0:
            alert["anomaly_types"].append("高换手率")
            alert["severity"] = _max_severity(alert["severity"], "medium")
            alert["details"].append(f"换手率{turnover:.1f}%")

        # 量价背离 (创新高 + 量比<0.7)
        if prev_close > 0 and high > prev_close * 1.02 and 0 < vol_ratio < 0.7:
            alert["anomaly_types"].append("量价背离")
            alert["severity"] = _max_severity(alert["severity"], "medium")
            alert["details"].append(f"创盘中新高但量比仅{vol_ratio:.1f}，警惕诱多")

        # ===== 深度检查：仅对有异动的个股取K线+资金 =====
        need_deep = heavy_volume or alert["severity"] != "normal"

        if heavy_volume:
            alert["details"].append(f"量比{vol_ratio:.1f}倍")
            if alert["severity"] == "normal":
                alert["severity"] = "medium"

        if need_deep:
            # K线 → MA20/MA60破位
            kline = get_kline_with_indicators(sym, days=35)
            if "latest" in kline:
                ma20 = kline["latest"].get("MA20")
                ma60 = kline["latest"].get("MA60")

                if ma20 and price and prev_close:
                    if heavy_volume and price > ma20 and prev_close <= ma20:
                        alert["anomaly_types"].append("放量突破MA20")
                        alert["severity"] = _max_severity(alert["severity"], "high")
                        alert["details"].append(f"放量突破MA20({ma20:.2f})")
                    elif heavy_volume and price < ma20 and prev_close >= ma20:
                        alert["anomaly_types"].append("放量跌破MA20")
                        alert["severity"] = _max_severity(alert["severity"], "high")
                        alert["details"].append(f"放量跌破MA20({ma20:.2f})")

                if ma60 and price and prev_close:
                    if price > ma60 and prev_close <= ma60:
                        alert["anomaly_types"].append("突破MA60牛熊线")
                        alert["severity"] = _max_severity(alert["severity"], "high")
                        alert["details"].append(f"突破MA60({ma60:.2f})")
                    elif price < ma60 and prev_close >= ma60:
                        alert["anomaly_types"].append("跌破MA60牛熊线")
                        alert["severity"] = _max_severity(alert["severity"], "high")
                        alert["details"].append(f"跌破MA60({ma60:.2f})")

            # Tushare真实量比补充
            basic = _get_daily_basic(sym)
            if basic and basic.get('volume_ratio'):
                real_vr = float(basic.get('volume_ratio', 0) or 0)
                if real_vr > vol_ratio:
                    vol_ratio = real_vr
                    alert["volume_ratio"] = round(real_vr, 1)
                    if real_vr >= 2.0 and not heavy_volume:
                        heavy_volume = True
                        alert["anomaly_types"].append("放量(Tushare)")
                        alert["severity"] = _max_severity(alert["severity"], "medium")
                        alert["details"].append(f"量比{real_vr:.1f}倍(Tushare)")

            # 资金流向 → 主力异动
            flow = get_capital_flow(sym)
            if "recent_flow" in flow and flow["recent_flow"]:
                main_net = flow["recent_flow"][-1].get("主力净流入万", 0)
                if abs(main_net) >= 2000:
                    alert["anomaly_types"].append("主力资金异动")
                    alert["severity"] = _max_severity(alert["severity"], "high")
                    alert["details"].append(f"主力净流入{main_net:+.0f}万")
                elif flow_mv > 0:
                    threshold_1pct = flow_mv * 0.01 / 10000
                    if abs(main_net) >= threshold_1pct:
                        alert["anomaly_types"].append("主力资金异动(占比)")
                        alert["severity"] = _max_severity(alert["severity"], "medium")
                        pct_flow = abs(main_net) * 10000 / flow_mv * 100
                        alert["details"].append(f"主力净流入占流通市值{pct_flow:.1f}%")
            # V4.2 T+1续流验证: 昨日大额流入今日复查, 区分建仓与游资快闪(9/7云铝课)
            rf = flow.get("recent_flow") or []
            lf = flow.get("latest_flow") or {}
            if len(rf) >= 2 and lf:
                prev_day = rf[1] if (rf and rf[0] is lf) else (rf[-2] if rf[-1] is lf else None)
                if prev_day:
                    prev_net = float(prev_day.get("主力净流入万", prev_day.get("主力净流入", 0)) or 0)  # M13b
                    today_net = float(lf.get("主力净流入万", lf.get("主力净流入", 0)) or 0)
                    if prev_net >= 2000:
                        if today_net < 0 and abs(today_net) >= prev_net * 0.5:
                            alert["anomaly_types"].append("T+1快闪嫌疑")
                            alert["severity"] = _max_severity(alert["severity"], "high")
                            alert["details"].append(f"昨主力+{prev_net:.0f}万今回吐{today_net:.0f}万(>=50%)=游资快闪非建仓(V4.2)")
                        elif today_net >= 0:
                            alert["anomaly_types"].append("T+1续流确认")
                            alert["severity"] = _max_severity(alert["severity"], "medium")
                            alert["details"].append(f"昨+{prev_net:.0f}万今+{today_net:.0f}万续流, 建仓特征(V4.2)")

        # 汇总
        if alert["severity"] != "normal":
            anomalies.append(alert)
        else:
            normal_count += 1

    # ===== 持仓监控 =====
    active_positions = [p for p in read_positions() if p.get("status") == "active"]
    for pos in active_positions:
        sym = pos["symbol"]
        row_p = df_all[df_all['代码'] == sym]
        if row_p.empty:
            continue
        r = row_p.iloc[0]
        price = round(float(r.get('最新价', 0) or 0), 2)
        if price <= 0:
            continue

        stop_loss = pos["stop_loss"]
        target = pos["target"]
        cost = pos["cost"]
        name = pos.get("name", sym)

        p_alert = {
            "code": sym,
            "name": name,
            "price": price,
            "change_pct": round(float(r.get('涨跌幅', 0) or 0), 2),
            "position": True,
            "anomaly_types": [],
            "severity": "normal",
            "details": [f"持仓: 成本{cost} 数量{pos['shares']} 止损{stop_loss} 目标{target}"]
        }

        if price <= stop_loss:
            p_alert["anomaly_types"].append("触发止损")
            p_alert["severity"] = "critical"
            p_alert["details"].append(f"现价{price} <= 止损位{stop_loss}")
        elif price >= target:
            p_alert["anomaly_types"].append("触发目标")
            p_alert["severity"] = "critical"
            p_alert["details"].append(f"现价{price} >= 目标位{target}")
        else:
            if stop_loss > 0:
                dist_stop = (price - stop_loss) / stop_loss * 100
                if dist_stop < 3:
                    p_alert["anomaly_types"].append("接近止损")
                    p_alert["severity"] = "high"
                    p_alert["details"].append(f"距止损仅{dist_stop:.1f}%")
            if target > 0:
                dist_target = (target - price) / target * 100
                if dist_target < 5:
                    p_alert["anomaly_types"].append("接近目标")
                    p_alert["severity"] = "high"
                    p_alert["details"].append(f"距目标仅{dist_target:.1f}%")

        if p_alert["severity"] != "normal":
            anomalies.append(p_alert)

    return {
        "scan_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "hs300_change": round(hs300_change, 2),
        "total": len(symbols),
        "anomaly_count": len(anomalies),
        "normal_count": normal_count,
        "anomalies": anomalies
    }


# ========== 盘后日报 ==========

def daily_report():
    watchlist = read_watchlist()
    if not watchlist:
        return {"error": "自选股列表为空"}

    symbols = [item["code"] for item in watchlist]
    try:
        quotes = _sina_batch_quotes(symbols)
        quote_map = {q.get("代码"): q for q in quotes}
    except Exception as e:
        return {"error": f"行情数据获取失败: {str(e)[:80]}"}

    hs300_change = get_hs300_change()
    report_items = []

    for item in watchlist:
        sym = item["code"]
        sym_name = item.get("name", sym)

        q = quote_map.get(sym, {})
        if not q:
            continue

        entry = {
            "code": sym,
            "name": sym_name,
            "price": round(float(q.get("最新价", 0) or 0), 2),
            "change_pct": round(float(q.get("涨跌幅", 0) or 0), 2),
            "volume_ratio": 0,
            "turnover": 0,
        }

        basic = _get_daily_basic(sym)
        if basic:
            entry["volume_ratio"] = round(basic.get('volume_ratio', 0) or 0, 2)
            entry["turnover"] = round(basic.get('turnover_rate', 0) or 0, 2)

        # K线 → 均线状态 + 关注要点
        kline = get_kline_with_indicators(sym, days=70)
        if "latest" in kline:
            entry["ma_align"] = kline["summary"]["均线排列"]
            entry["macd_signal"] = kline["summary"]["MACD信号"]
            entry["rsi"] = kline["latest"]["RSI"]
            entry["ma5"] = kline["latest"].get("MA5")
            entry["ma20"] = kline["latest"].get("MA20")
            entry["ma60"] = kline["latest"].get("MA60")

            # 次日关注要点
            notes = []
            price = entry["price"]
            ma5 = kline["latest"].get("MA5")
            ma20 = kline["latest"].get("MA20")
            ma60 = kline["latest"].get("MA60")
            rsi = kline["latest"]["RSI"]

            if ma5 and price:
                notes.append(f"MA5支撑/压力: {ma5:.2f}")
            if ma20 and price:
                gap = abs(price - ma20) / ma20 * 100
                if gap < 1.5:
                    notes.append(f"接近MA20({ma20:.2f})，关注突破方向")
            if ma60 and price:
                gap = abs(price - ma60) / ma60 * 100
                if gap < 2:
                    notes.append(f"接近MA60({ma60:.2f})，牛熊线攻防")
            if rsi > 70:
                notes.append("RSI超买，注意回调风险")
            elif rsi < 30:
                notes.append("RSI超卖，关注反弹信号")

            entry["next_day_notes"] = notes
        else:
            entry["next_day_notes"] = ["K线数据不足"]

        report_items.append(entry)

    return {
        "report_date": datetime.now().strftime("%Y-%m-%d"),
        "hs300_change": round(hs300_change, 2),
        "total": len(report_items),
        "stocks": report_items
    }


# ========== 主入口 ==========

# ========== 回测引擎 v3.1 ==========

def _get_kline_range(symbol, start_date, end_date):
    """获取指定区间的日K线数据（Tushare主→AKShare容灾）"""
    # Tushare主源
    ts_code = _ts_code(symbol)
    data = _tushare_api('daily',
        {'ts_code': ts_code, 'start_date': start_date.replace('-', ''), 'end_date': end_date.replace('-', '')},
        'ts_code,trade_date,open,high,low,close,vol,amount,pct_chg')
    
    if data and data.get('items'):
        fields = data.get('fields', [])
        rows = []
        for item in data['items']:
            row = dict(zip(fields, item))
            rows.append({
                'date': f"{row['trade_date'][:4]}-{row['trade_date'][4:6]}-{row['trade_date'][6:]}",
                'open': float(row.get('open', 0) or 0),
                'high': float(row.get('high', 0) or 0),
                'low': float(row.get('low', 0) or 0),
                'close': float(row.get('close', 0) or 0),
                'volume': float(row.get('vol', 0) or 0)
            })
        # Tushare返回的是倒序，需要反转为正序
        rows.reverse()
        df = pd.DataFrame(rows)
        return df

    # AKShare容灾
    try:
        sz_code = f"sz{symbol}" if symbol.startswith(('0', '3')) else f"sh{symbol}"
        df = safe_request(ak.stock_zh_a_daily, symbol=sz_code, start_date=start_date, end_date=end_date, adjust="qfq")
        if df is not None and not df.empty:
            df = df.rename(columns={'date': 'date', 'open': 'open', 'high': 'high', 'low': 'low', 'close': 'close', 'volume': 'volume'})
            return df
    except Exception as e:
        log(f"AKShare区间K线容灾失败: {e}")
    
    return None


def _gen_signals(df, strategy):
    """根据策略名称在K线DataFrame上生成买卖信号列"""
    df = df.copy()
    df['signal'] = 0  # 1=买入, -1=卖出

    if strategy == "ma_cross":
        df['MA5'] = df['close'].rolling(5).mean()
        df['MA20'] = df['close'].rolling(20).mean()
        df['prev_MA5'] = df['MA5'].shift(1)
        df['prev_MA20'] = df['MA20'].shift(1)
        
        # 金叉买入
        golden_cross = (df['MA5'] > df['MA20']) & (df['prev_MA5'] <= df['prev_MA20'])
        df.loc[golden_cross, 'signal'] = 1
        # 死叉卖出
        death_cross = (df['MA5'] < df['MA20']) & (df['prev_MA5'] >= df['prev_MA20'])
        df.loc[death_cross, 'signal'] = -1

    elif strategy == "macd":
        ema12 = df['close'].ewm(span=12, adjust=False).mean()
        ema26 = df['close'].ewm(span=26, adjust=False).mean()
        df['DIF'] = ema12 - ema26
        df['DEA'] = df['DIF'].ewm(span=9, adjust=False).mean()
        df['MACD'] = (df['DIF'] - df['DEA']) * 2
        
        df['prev_MACD'] = df['MACD'].shift(1)
        # MACD柱由负转正买入
        df.loc[(df['MACD'] > 0) & (df['prev_MACD'] <= 0), 'signal'] = 1
        # MACD柱由正转负卖出
        df.loc[(df['MACD'] < 0) & (df['prev_MACD'] >= 0), 'signal'] = -1

    elif strategy == "rsi":
        delta = df['close'].diff()
        gain = delta.where(delta > 0, 0)
        loss = (-delta).where(delta < 0, 0)
        avg_gain = gain.rolling(14).mean()
        avg_loss = loss.rolling(14).mean()
        rs = avg_gain / avg_loss.replace(0, np.nan)
        df['RSI'] = 100 - (100 / (1 + rs))
        
        # RSI跌破30买入（超卖反弹）
        df.loc[df['RSI'] < 30, 'signal'] = 1
        # RSI突破70卖出（超买回落）
        df.loc[df['RSI'] > 70, 'signal'] = -1

    elif strategy == "boll":
        df['BOLL_MID'] = df['close'].rolling(20).mean()
        df['BOLL_STD'] = df['close'].rolling(20).std()
        df['BOLL_UP'] = df['BOLL_MID'] + 2 * df['BOLL_STD']
        df['BOLL_DN'] = df['BOLL_MID'] - 2 * df['BOLL_STD']
        
        # 跌破下轨买入
        df.loc[df['close'] < df['BOLL_DN'], 'signal'] = 1
        # 突破上轨卖出
        df.loc[df['close'] > df['BOLL_UP'], 'signal'] = -1

    return df


def _run_backtest_core(df, initial_capital, commission_rate=0.0003):
    """执行回测主循环"""
    position = 0  # 持仓数量
    cash = float(initial_capital)
    entry_price = 0
    trades = []
    equity_curve = []

    for _, row in df.iterrows():
        signal = row['signal']
        price = row['close']
        date = row['date']

        if signal == 1 and position == 0:
            # 全仓买入（回测允许零股，不受A股100股整手限制）
            shares = cash / (price * (1 + commission_rate))
            if shares > 0:
                cost = shares * price * (1 + commission_rate)
                cash -= cost
                position = shares
                entry_price = price
                trades.append({'date': date, 'action': 'BUY', 'price': price, 'shares': shares})

        elif signal == -1 and position > 0:
            # 全仓卖出
            revenue = position * price * (1 - commission_rate)
            cash += revenue
            pnl = (price - entry_price) * position
            trades.append({'date': date, 'action': 'SELL', 'price': price, 'shares': position, 'pnl': round(pnl, 2)})
            position = 0
            entry_price = 0

        # 记录每日净值
        total_value = cash + position * price
        equity_curve.append({'date': date, 'equity': round(total_value, 2)})

    final_value = cash + position * df.iloc[-1]['close']
    return trades, equity_curve, round(final_value, 2)


def _calc_metrics(equity_curve, trades, initial_capital, strategy):
    """计算绩效指标"""
    df_eq = pd.DataFrame(equity_curve)
    df_eq['daily_return'] = df_eq['equity'].pct_change().fillna(0)
    
    final_equity = df_eq['equity'].iloc[-1]
    total_return = round((final_equity - initial_capital) / initial_capital * 100, 2)
    
    # 最大回撤
    df_eq['peak'] = df_eq['equity'].cummax()
    df_eq['drawdown'] = (df_eq['equity'] - df_eq['peak']) / df_eq['peak']
    max_drawdown = round(df_eq['drawdown'].min() * 100, 2)
    
    # 夏普比率 (年化，无风险利率设为2%)
    daily_returns = df_eq['daily_return'].values
    if len(daily_returns) > 1 and np.std(daily_returns) > 0:
        sharpe = np.mean(daily_returns) * 252 / (np.std(daily_returns) * np.sqrt(252))
        # 减去无风险利率
        sharpe = round(sharpe - 0.02, 2)
    else:
        sharpe = 0.0
    
    # 胜率
    sell_trades = [t for t in trades if t['action'] == 'SELL']
    if sell_trades:
        wins = [t for t in sell_trades if t.get('pnl', 0) > 0]
        win_rate = round(len(wins) / len(sell_trades) * 100, 1)
        total_pnl = round(sum(t.get('pnl', 0) for t in sell_trades), 2)
    else:
        win_rate = 0.0
        total_pnl = 0.0

    return {
        "strategy": strategy,
        "initial_capital": initial_capital,
        "final_equity": final_equity,
        "total_return_pct": total_return,
        "max_drawdown_pct": max_drawdown,
        "sharpe_ratio": sharpe,
        "total_trades": len(sell_trades),
        "win_rate": win_rate,
        "total_pnl": total_pnl
    }


def backtest(symbol, start_date, end_date, strategy="ma_cross", initial_capital=100000):
    """回测主入口"""
    valid_strategies = ["ma_cross", "macd", "rsi", "boll"]
    if strategy not in valid_strategies:
        return {"error": f"无效策略: {strategy}。支持: {', '.join(valid_strategies)}"}

    df = _get_kline_range(symbol, start_date, end_date)
    if df is None or df.empty or len(df) < 30:
        return {"error": f"获取{symbol}在{start_date}至{end_date}的数据失败或不足30条"}

    df = _gen_signals(df, strategy)
    trades, equity_curve, final_value = _run_backtest_core(df, initial_capital)
    metrics = _calc_metrics(equity_curve, trades, initial_capital, strategy)

    return {
        "symbol": symbol,
        "period": f"{start_date} 至 {end_date}",
        "metrics": metrics,
        "trades": trades,
        "equity_curve_sample": equity_curve[::max(1, len(equity_curve)//10)][:15] # 采样返回，避免过长
    }



# ========== 选股框架 v4.0 常量与辅助函数 ==========

import hashlib as _hashlib

# Tushare stock_basic.industry -> 风格组映射（110个细分行业全覆盖）
INDUSTRY_STYLE_MAP = {
    # A 周期资源
    '铜': 'A', '铝': 'A', '铅锌': 'A', '黄金': 'A', '小金属': 'A', '矿物制品': 'A',
    '煤炭开采': 'A', '焦炭加工': 'A',
    '石油开采': 'A', '石油加工': 'A', '石油贸易': 'A',
    '普钢': 'A', '特种钢': 'A', '钢加工': 'A',
    '化工原料': 'A', '化纤': 'A', '农药化肥': 'A', '染料涂料': 'A', '塑料': 'A', '橡胶': 'A',
    '水泥': 'A', '玻璃': 'A', '其他建材': 'A', '陶瓷': 'A',
    '建筑工程': 'A', '装修装饰': 'A',
    '专用机械': 'A', '工程机械': 'A', '机床制造': 'A', '机械基件': 'A', '化工机械': 'A', '轻工机械': 'A',
    # B 金融杠杆
    '银行': 'B', '保险': 'B', '证券': 'B', '多元金融': 'B',
    # C 成长科技
    '半导体': 'C', '元器件': 'C', 'IT设备': 'C',
    '软件服务': 'C',
    '通信设备': 'C', '电信运营': 'C',
    '影视音像': 'C', '互联网': 'C', '广告包装': 'C', '出版业': 'C',
    '电气设备': 'C', '电器仪表': 'C',
    '航空': 'C', '船舶': 'C',
    # D 消费稳定
    '白酒': 'D', '啤酒': 'D', '红黄酒': 'D', '软饮料': 'D', '食品': 'D', '乳制品': 'D', '饲料': 'D',
    '中成药': 'D', '化学制药': 'D', '生物制药': 'D', '医疗保健': 'D', '医药商业': 'D',
    '农业综合': 'D', '种植业': 'D', '渔业': 'D', '林业': 'D',
    '纺织': 'D', '服饰': 'D',
    '家用电器': 'D', '电器连锁': 'D',
    '汽车整车': 'D', '汽车配件': 'D', '汽车服务': 'D', '摩托车': 'D',
    '旅游景点': 'D', '旅游服务': 'D', '酒店餐饮': 'D', '公共交通': 'D',
    '百货': 'D', '超市连锁': 'D', '商贸代理': 'D', '商品城': 'D', '其他商业': 'D', '批发业': 'D',
    '日用化工': 'D', '家居用品': 'D',
    '造纸': 'D', '文教休闲': 'D',
    '纺织机械': 'D', '农用机械': 'D',
    # E 基建公用
    '水力发电': 'E', '火力发电': 'E', '新型电力': 'E', '供气供热': 'E', '水务': 'E',
    '机场': 'E', '港口': 'E', '公路': 'E', '路桥': 'E', '水运': 'E', '空运': 'E', '铁路': 'E',
    '仓储物流': 'E',
    '环境保护': 'E',
    '综合类': 'E',
    '全国地产': 'E', '区域地产': 'E', '房产服务': 'E', '园区开发': 'E',
}

FRAMEWORK_V4_PARAMS = {
    'version': '4.1',
    'calibration_20260908': {
        'rsi6_max': 65,
        'vol_confirm_ratio': 2.5,
        'monthly_risk_cap_pct': 6.0,
        'source': '翔批准: RSI周期阈值配套+量比确认级+2/6法则月度闸 | 溯源链: RSI6配6日短周期原70收紧至65(V4.1校准9/8观澜裁定); 量比确认级2.0→2.5(放量确认阈值上调, 减少假确认); 月度6%=单笔2%上限的月度扩展(Van Tharp仓位管理族: 2/6法则——单笔2%+月度6%双闸, 观澜9/8裁定翔批[fv:571a2645])',
    },
    'industry_map': INDUSTRY_STYLE_MAP,
    'Q2': {'A': 8, 'B': 10, 'C': 8, 'D': 12, 'E': 8},
    'Q3': {
        'A': {'pe_pct': 40, 'pb_pct': 50, 'logic': 'OR'},
        'B': {'bank_pb_max': 1.0, 'broker_pb_pct': 50, 'brokerage': ['证券']},
        'C': {'peg_max': 1.0, 'growth_cap': 50},
        'D': {'pe_pct': 50, 'pb_pct': 65, 'logic': 'AND'},
        'E': {'div_min': 3.0, 'pb_pct': 40, 'logic': 'OR'},
    },
    'Q5': {'A': {'debt_max': 60}, 'C': {'rd_ratio_min': 5}, 'D': {'gpm_min': 20}, 'E': {'ocf_min': 0.05}},
    'min_samples': 250,
    'special': {'医药生物': 'use_PEG'},
}

STYLE_NAMES = {'A': '周期资源', 'B': '金融杠杆', 'C': '成长科技', 'D': '消费稳定', 'E': '基建公用'}


def _generate_fv_hash():
    params_str = json.dumps(FRAMEWORK_V4_PARAMS, sort_keys=True, ensure_ascii=False)
    return f"[fv:{_hashlib.md5(params_str.encode()).hexdigest()[:8]}]"


def _get_industry(symbol):
    ts_code = _ts_code(symbol)
    data = _tushare_api('stock_basic', {'ts_code': ts_code}, 'ts_code,name,industry')
    if not data or not data.get('items'):
        log(f"industry fetch failed for {symbol}")
        return None
    fields = data.get('fields', [])
    row = dict(zip(fields, data['items'][0]))
    return row.get('industry', '')


def _get_fina_indicator_v4(symbol):
    ts_code = _ts_code(symbol)
    data = _tushare_api('fina_indicator', {'ts_code': ts_code},
        'ts_code,ann_date,end_date,roe,or_yoy,netprofit_yoy,debt_to_assets,grossprofit_margin,ocf_to_debt,ocf_to_or')
    if not data or not data.get('items'):
        log(f"fina_indicator fetch failed for {symbol}")
        return None
    fields = data.get('fields', [])
    rows = [dict(zip(fields, item)) for item in data['items']]
    # Prefer annual report (end_date contains '1231') - Tushare returns desc by date
    annual = [r for r in rows if str(r.get('end_date', '')).endswith('1231')]
    if annual:
        return annual[0]
    # Fallback to latest semi-annual, then latest available
    semi = [r for r in rows if str(r.get('end_date', '')).endswith('0630')]
    if semi:
        return semi[0]
    return rows[0]


# ========== 选股框架 v3.0 ==========

def market_check():
    """大盘环境判断 — 沪深300趋势"""
    try:
        # 沪深300用Tushare index_daily
        ts_data = _tushare_api('index_daily',
            {'ts_code': '000300.SH'},
            'ts_code,trade_date,close,pct_chg')
        if not ts_data or not ts_data.get('items'):
            log("Tushare沪深300数据失败(market_check)，尝试AKShare容灾")
            try:
                df_idx = safe_request(ak.stock_zh_index_daily, symbol='sh000300')
                if df_idx is not None and len(df_idx) >= 60:
                    closes = [round(float(x), 2) for x in df_idx['close'].tail(60).tolist()]
                else:
                    return {"error": "沪深300数据获取失败（Tushare+AKShare均无数据）"}
            except Exception as e2:
                return {"error": f"沪深300数据获取失败: {str(e2)[:60]}"}
        
        items = ts_data.get('items', [])
        fields = ts_data.get('fields', [])
        closes = [dict(zip(fields, item)).get('close', 0) for item in items[:60]]
        closes.reverse()  # 最新在最后
        
        if len(closes) < 60:
            return {"error": "沪深300数据不足"}
        
        arr = np.array(closes, dtype=float)
        ma5 = round(float(arr[-5:].mean()), 2)
        ma20 = round(float(arr[-20:].mean()), 2)
        ma60 = round(float(arr[-60:].mean()), 2)
        close = round(float(arr[-1]), 2)
        pct = round(float(dict(zip(fields, items[0])).get('pct_chg', 0)), 2)
        
        
        if ma5 > ma20 > ma60:
            trend = "多头排列"
            action = "正常仓位，可以建仓"
            risk_factor = 1.0
        elif ma5 < ma20 < ma60:
            trend = "空头排列"
            action = "不建仓，收紧止损（豁免通道可半预算试探）"
            risk_factor = 0.5
        else:
            trend = "交叉缠绕/震荡"
            action = "半仓观望，只买确定性高的"
            risk_factor = 0.7
        
        return {
            "index": "沪深300",
            "close": close,
            "pct_chg": pct,
            "trend": trend,
            "action": action,
            "ma5": ma5,
            "ma20": ma20,
            "ma60": ma60,
            "risk_factor": risk_factor
        }
    except Exception as e:
        return {"error": str(e)[:60]}


def _exemption_check(symbol):
    """V4.2.2 豁免通道三证明 (翔批 2026-09-10建 / M17修订翔批2026-09-22)
    空头市场个股开仓豁免: ①板块庇护(M17: 板块RS排名前1/3且非downtrend——双动量体系,
    相对强度选板块+绝对下限防垃圾堆冠军, 业界对齐Antonacci双动量/IBD RS百分位)
    ②个股独立(20日涨幅跑赢沪深300+均线多头排列) ③T+1资金续流(近2日主力合计为正且最新日不流出)"""
    proofs = {}
    sector_ok = False
    try:
        sector = _guess_sector(symbol)
        proofs["sector"] = sector
        rot = sector_rotation()
        allsec = rot.get("all_sectors") or []
        mom = next((s.get("momentum") for s in allsec if s.get("name") == sector), None)
        proofs["sector_momentum"] = mom
        # M17-2026-09-22 P1相对动量修订(翔批09:32授权, 业务规则归观澜):
        # all_sectors按pct_5d降序排列, 索引即RS排名; 前1/3且非downtrend=双动量判定
        n_sec = len(allsec)
        idx_sec = next((i for i, s in enumerate(allsec) if s.get("name") == sector), None)
        if idx_sec is not None and n_sec > 0:
            proofs["sector_rs_rank"] = f"{idx_sec + 1}/{n_sec}"
            proofs["sector_rs_pctile"] = round((idx_sec + 1) / n_sec * 100, 1)
            sector_ok = (idx_sec + 1) <= max(3, n_sec // 3) and mom != "downtrend"
        else:
            sector_ok = mom in ("uptrend", "accelerating")  # RS不可得退回绝对动量(降级安全)
    except Exception as e:
        proofs["sector_err"] = str(e)[:40]
    proofs["p1_sector_shelter"] = sector_ok
    indep_ok = False
    try:
        kdf = _sina_kline(symbol, 26)
        idx = _ak_index_daily("000300.SH", 21)
        if kdf is not None and hasattr(kdf, "iloc") and len(kdf) >= 21 and idx and idx.get("closes") and len(idx["closes"]) >= 21:
            _cc = "收盘" if "收盘" in kdf.columns else ("close" if "close" in kdf.columns else None)
            stk_ret = (float(kdf[_cc].iloc[-1]) / float(kdf[_cc].iloc[-21]) - 1) if _cc else None
            idx_ret = idx["closes"][-1] / idx["closes"][-21] - 1
            kl = get_kline_with_indicators(symbol, days=30)
            bull_ma = "多头排列" in str(kl.get("summary", {}).get("均线排列", ""))
            proofs["stock_20d_pct"] = round(stk_ret * 100, 2) if stk_ret is not None else None
            proofs["hs300_20d_pct"] = round(idx_ret * 100, 2)
            proofs["ma_bull"] = bull_ma
            indep_ok = (stk_ret is not None and stk_ret > idx_ret) and bull_ma
    except Exception as e:
        proofs["indep_err"] = str(e)[:40]
    proofs["p2_independence"] = indep_ok
    flow_ok = False
    try:
        fl = get_capital_flow(symbol)
        rf = fl.get("recent_flow") or []
        if len(rf) >= 2:
            rf_sorted = sorted(rf, key=lambda r: str(r.get("日期", "")))
            n1 = float(rf_sorted[-2].get("主力净流入万", rf_sorted[-2].get("主力净流入", 0)) or 0)  # M13b键名兼容
            n0 = float(rf_sorted[-1].get("主力净流入万", rf_sorted[-1].get("主力净流入", 0)) or 0)
            proofs["flow_prev1_wan"] = round(n1, 0)
            proofs["flow_latest_wan"] = round(n0, 0)
            flow_ok = (n1 + n0) > 0 and n0 >= 0
    except Exception as e:
        proofs["flow_err"] = str(e)[:40]
    proofs["p3_flow_continuity"] = flow_ok
    exempt = sector_ok and indep_ok and flow_ok
    return {"exempt": exempt, "proofs": proofs,
            "authority": "V4.2.2豁免通道: 板块庇护(M17:RS前1/3+非downtrend)+个股独立+资金续流 (翔批2026-09-10/09-22)"}


def batch_screen(symbols, with_flow=True, with_exemption=False):
    """#27 batch_screen 批量三问 (2026-09-13 观澜方案+三方会审, 翔批)
    决策层批量补格: funnel(批量过滤)→本命令(批量三问)→position_size(单票定仓)链路贯通.
    单一事实源: 循环调用 stock_screen_v3 / get_capital_flow / _exemption_check 本体函数, 零逻辑分叉.
    P1 pacing 0.35s/票 | P2 单票失败进error整体继续 | P3 MAX_BATCH=30硬编码(防误传300) |
    P4 symbols双形态: list(JSON路径)或逗号串(k=v路径) | P5 data_quality哨兵(失败是响的批量版)
    输出层(观澜18:25签字): summary摘要表 + PASS明细全字段; REJECT只入摘要一行原因.
    with_exemption默认false(会审裁决②: 弱市扫描恰是rotation 2日滞后最危险场景, 要开显式传)."""
    import time as _time
    MAX_BATCH = 30  # P3: 硬编码上限, 理由: 5分钟墙×pacing的3.3倍余量按30只设计(翔裁300000)
    if isinstance(symbols, int):  # M13 fix (Nova r12): M10的auto_type把裸数字转int, 单票int形态归一str——修复T3崩溃('int' object is not iterable)
        symbols = str(symbols)
    if isinstance(symbols, str):
        syms = [s.strip() for s in symbols.split(",") if s.strip()]  # P4: k=v逗号串路径
    else:
        syms = [str(s).strip() for s in (symbols or []) if str(s).strip()]  # P4: JSON数组路径
    syms = [s for s in syms if s.isdigit() and len(s) == 6][:MAX_BATCH]
    if not syms:
        return {"status": "error", "message": "symbols为空或格式无效(需六位代码, 逗号分隔或数组)"}
    summary, details_pass, errors = [], [], []
    flow_alive = 0
    for i, sym in enumerate(syms):
        row = {"symbol": sym}
        try:
            r = stock_screen_v3(sym)
            if i < len(syms) - 1:
                _time.sleep(0.35)  # P1 pacing
            if not isinstance(r, dict):
                raise ValueError(f"stock_screen返回非dict: {type(r).__name__}")
            _d = r.get("details", {})  # 键名适配(实弹验证修正): 本体返回PE_TTM/PB/RSI6, 非pe/pb/rsi6
            row["verdict"] = "PASS" if r.get("pass") else "REJECT"
            row["rejected_by"] = r.get("rejected_by", [])
            row["reason"] = r.get("reason", "")[:60]  # REJECT一行原因入表(输出层签字项)
            row["pe"] = _d.get("PE_TTM", _d.get("pe"))
            row["pb"] = _d.get("PB", _d.get("pb"))
            row["rsi6"] = _d.get("RSI6", _d.get("rsi6"))
            row["close"] = _d.get("close")
            if with_flow:
                try:
                    fl = get_capital_flow(sym)
                    rf = fl.get("recent_flow") or []
                    if len(rf) >= 2:
                        rf_s = sorted(rf, key=lambda x: str(x.get("日期", "")))
                        n1 = float(rf_s[-2].get("主力净流入万", rf_s[-2].get("主力净流入", 0)) or 0)  # M13b
                        n0 = float(rf_s[-1].get("主力净流入万", rf_s[-1].get("主力净流入", 0)) or 0)
                        row["flow_2d_sum"] = round(n1 + n0, 0)
                        if (n1 + n0) != 0:
                            flow_alive += 1
                    else:
                        row["flow_2d_sum"] = None
                except Exception as e:
                    row["flow_2d_sum"] = None
                    row["flow_err"] = str(e)[:40]
            if with_exemption and r.get("pass"):
                try:
                    ex = _exemption_check(sym)
                    row["exemption_proofs"] = ex.get("proofs", {})
                    row["exempt"] = ex.get("exempt", False)
                except Exception as e:
                    row["exemption_proofs"] = {"err": str(e)[:40]}
            summary.append(row)
            if r.get("pass"):
                details_pass.append({"summary": row, "full": r})  # 输出层: PASS才给全字段
        except Exception as e:
            errors.append({"symbol": sym, "error": str(e)[:60]})  # P2: 单票失败不阻塞
    passed = sum(1 for r in summary if r.get("verdict") == "PASS")
    out = {"status": "success",
           "meta": {"count": len(syms), "passed": passed, "rejected": len(syms) - passed - len(errors),
                     "errors": len(errors), "with_flow": with_flow, "with_exemption": with_exemption,
                     "authority": "#27三方会审2026-09-13(瑶序五笔+Nova三增量+翔两裁决), A方案同步30只"},
           "summary": summary, "details_pass": details_pass, "errors": errors}
    # P5: data_quality哨兵 — flow全灭或错误过半时响
    dq = []
    if with_flow and summary and flow_alive == 0:
        dq.append("⚠ data_quality: flow全灭(所有票flow_2d_sum为0或None)——上游数据源可能故障, 本轮flow列不可信, 勿据此筛选(野战案②防御)")
    if errors and len(errors) >= len(syms) / 2:
        dq.append(f"⚠ data_quality: 单票错误率{len(errors)}/{len(syms)}过半——大面积失败, 结果不完整")
    if dq:
        out["data_quality"] = dq
    return out


def _market_factor(symbol=None, full_check=False):
    """V4.2.1: 大盘状态→风险预算系数. 多头1.0 / 缠绕或数据缺失0.7 / 空头0.5
    full_check=True时空头需过豁免三证明, 未过返回None(=拒绝)"""
    try:
        mk = market_check()
        t = mk.get("trend") if isinstance(mk, dict) else None
    except Exception:
        t = None
    if t == "多头排列":
        return 1.0, t, None
    if t == "空头排列":
        if full_check and symbol:
            ex = _exemption_check(symbol)
            if ex.get("exempt"):
                return 0.5, t, ex
            return None, t, ex
        return 0.5, t, None
    return 0.7, t, None


def stock_screen_v3(symbol):
    """选股框架三问 + 禁买清单"""
    result = {
        "symbol": symbol,
        "pass": True,
        "rejected_by": [],
        "details": {}
    }
    
    # === 禁买清单检查 ===
    
    # 1. 基本面数据
    basic = _get_daily_basic(symbol)
    if not basic:
        result["pass"] = False
        result["rejected_by"].append("数据获取失败，无法判断")
        result["verdict"] = "REJECT"
        result["reason"] = "无法获取基本面数据"
        return result
    
    pe_ttm = basic.get("pe_ttm", 0) or 0
    pb = basic.get("pb", 0) or 0
    total_mv = basic.get("total_mv", 0) or 0  # 万元
    turnover = basic.get("turnover_rate", 0) or 0
    close = basic.get("close", 0) or 0
    
    result["details"]["PE_TTM"] = round(pe_ttm, 1)
    result["details"]["PB"] = round(pb, 2)
    result["details"]["total_mv_yi"] = round(total_mv / 10000, 1) if total_mv else None
    result["details"]["turnover"] = round(turnover, 2)
    result["details"]["close"] = close
    
    # 禁买1: 市值<100亿
    if total_mv and total_mv / 10000 < 100:
        result["pass"] = False
        result["rejected_by"].append(f"市值{round(total_mv/10000,1)}亿<100亿")
    
    # 2. 技术面数据
    kline = get_kline_with_indicators(symbol, days=70)
    if "latest" not in kline or "error" in kline:
        result["pass"] = False
        result["rejected_by"].append("技术面数据获取失败")
        result["verdict"] = "REJECT"
        result["reason"] = "技术面数据不足"
        return result
    
    latest = kline["latest"]
    rsi6 = latest.get("RSI", 50)
    ma5 = latest.get("MA5", 0)
    ma10 = latest.get("MA10", 0)
    ma20 = latest.get("MA20", 0)
    ma60 = latest.get("MA60", 0)
    macd_bar = latest.get("MACD柱", 0)
    boll_up = latest.get("BOLL上", 0)
    boll_mid = latest.get("BOLL中", 0)
    boll_dn = latest.get("BOLL下", 0)
    
    result["details"]["RSI6"] = rsi6
    result["details"]["MA_align"] = kline["summary"].get("均线排列", "")
    result["details"]["MACD_signal"] = kline["summary"].get("MACD信号", "")
    result["details"]["MACD_bar"] = macd_bar
    
    # 禁买2: RSI>65 (V4.1校准同步)
    if rsi6 > 65:
        result["pass"] = False
        result["rejected_by"].append(f"RSI6={rsi6}>65超买")
    
    # 禁买3: 价格在布林上轨以上
    if close and boll_up and close > boll_up:
        result["pass"] = False
        result["rejected_by"].append(f"价格{close}>布林上轨{boll_up}")
    
    # 禁买4: 均线空头排列
    if ma5 and ma10 and ma20 and ma60:
        if ma5 < ma20 < ma60:
            result["pass"] = False
            result["rejected_by"].append("均线空头排列")
    
    # === 三问筛选 ===
    q_results = {}
    
    # Q2: 公司能赚钱吗？
    # 需要ROE — Tushare daily_basic没有ROE，用PE/PB反推
    # ROE ≈ PB / PE (近似)
    roe_approx = 0
    if pb > 0 and pe_ttm > 0:
        roe_approx = round(pb / pe_ttm * 100, 2)
    result["details"]["ROE_approx"] = roe_approx
    result["details"]["PB_ROE_ratio"] = round(pb / roe_approx, 3) if roe_approx > 0 else None
    
    q2_pass = True
    q2_reasons = []
    
    if roe_approx > 0 and roe_approx < 3:
        q2_pass = False
        q2_reasons.append(f"ROE约{roe_approx}%<3%（盈利能力差）")
    
    if pe_ttm > 30:
        q2_pass = False
        q2_reasons.append(f"PE {pe_ttm}>30（估值过高）")
    
    # PB动态门槛：PB/ROE ≤ 0.15（即投资回报率≥6.7%）
    pb_roe_ratio = round(pb / roe_approx, 3) if roe_approx > 0 else 99
    if pb_roe_ratio > 0.15:
        q2_pass = False
        q2_reasons.append(f"PB/ROE={pb_roe_ratio}>0.15（投资回报率偏低）")
    
    q_results["Q2_公司能赚钱"] = {
        "pass": q2_pass,
        "reasons": q2_reasons if q2_reasons else ["ROE/PE/PB在合理范围"]
    }
    
    # Q3: 价格合理吗？
    q3_pass = True
    q3_reasons = []
    
    if pe_ttm > 25:
        q3_pass = False
        q3_reasons.append(f"PE {pe_ttm}>25")
    
    if rsi6 > 65:
        q3_pass = False
        q3_reasons.append(f"RSI {rsi6}>65偏强")
    
    if macd_bar < 0:
        q3_pass = False
        q3_reasons.append("MACD死叉")
    
    q_results["Q3_价格合理"] = {
        "pass": q3_pass,
        "reasons": q3_reasons if q3_reasons else ["PE/RSI/MACD在合理范围"]
    }
    
    # Q1: 行业在变好吗？（简化版 — 用均线趋势判断）
    q1_pass = True
    q1_reasons = []
    
    if ma5 and ma20 and ma60:
        if not (ma5 > ma20):
            q1_pass = False
            q1_reasons.append("MA5<MA20趋势偏弱")
    
    if macd_bar < 0:
        q1_pass = False
        q1_reasons.append("MACD柱为负")
    
    q_results["Q1_趋势向上"] = {
        "pass": q1_pass,
        "reasons": q1_reasons if q1_reasons else ["均线和MACD趋势偏多"]
    }
    
    result["three_questions"] = q_results
    
    # === 最终判定 ===
    if not result["pass"]:
        result["verdict"] = "REJECT"
        result["reason"] = "；".join(result["rejected_by"])
    elif not q1_pass or not q2_pass or not q3_pass:
        result["verdict"] = "REJECT"
        all_reasons = []
        for q, v in q_results.items():
            if not v["pass"]:
                all_reasons.extend(v["reasons"])
        result["reason"] = "；".join(all_reasons)
        result["pass"] = False
    else:
        result["verdict"] = "PASS"
        result["reason"] = "通过三问筛选，建议深度分析"
    
    return result



# ========== 选股框架 v4.0 主函数 ==========

def _get_rd_ratio(symbol):
    """从income接口获取研发费用率(年报口径)"""
    ts_code = _ts_code(symbol)
    data = _tushare_api('income', {'ts_code': ts_code},
        'ts_code,end_date,revenue,rd_exp')
    if not data or not data.get('items'):
        return None
    fields = data.get('fields', [])
    rows = [dict(zip(fields, item)) for item in data['items']]
    annual = [r for r in rows if str(r.get('end_date', '')).endswith('1231')]
    row = annual[0] if annual else (rows[0] if rows else None)
    if not row:
        return None
    rd = float(row.get('rd_exp') or 0)
    rev = float(row.get('revenue') or 0)
    if rev > 0:
        return round(rd / rev * 100, 1)
    return None

def stock_screen(symbol):
    """v4.0 - 五风格组分路由 + 三问 + 禁买清单"""
    fv_hash = _generate_fv_hash()
    result = {
        "symbol": symbol,
        "framework_version": "4.1",
        "framework_hash": fv_hash,
        "pass": True,
        "rejected_by": [],
        "details": {},
        "warnings": []
    }

    # --- Step 0: daily_basic ---
    basic = _get_daily_basic(symbol)
    if not basic:
        result["pass"] = False
        result["verdict"] = "REJECT"
        result["reason"] = "无法获取基本面数据"
        return result

    pe_ttm = float(basic.get("pe_ttm", 0) or 0)
    pb = float(basic.get("pb", 0) or 0)
    total_mv = float(basic.get("total_mv", 0) or 0)
    close = float(basic.get("close", 0) or 0)
    dv_ttm = float(basic.get("dv_ratio", 0) or 0)

    result["details"]["PE_TTM"] = round(pe_ttm, 1)
    result["details"]["PB"] = round(pb, 2)
    result["details"]["total_mv_yi"] = round(total_mv / 10000, 1) if total_mv else None
    result["details"]["dv_ttm"] = round(dv_ttm, 2)

    # --- Step 1: industry -> style group ---
    industry = _get_industry(symbol)
    result["details"]["industry"] = industry or "未知"
    style_group = INDUSTRY_STYLE_MAP.get(industry, 'D')
    if industry not in INDUSTRY_STYLE_MAP:
        result["warnings"].append(f"[industry_fallback] '{industry}' not in map, default D")
    result["details"]["style_group"] = style_group
    result["details"]["style_name"] = STYLE_NAMES.get(style_group, '?')

    # --- Step 2: fina_indicator ---
    fina = _get_fina_indicator_v4(symbol)
    roe = float(fina.get('roe', 0) or 0) if fina else 0
    or_yoy = float(fina.get('or_yoy', 0) or 0) if fina else 0
    debt_to_assets = float(fina.get('debt_to_assets', 0) or 0) if fina else 0
    gpm = float(fina.get('grossprofit_margin', 0) or 0) if fina else 0
    ocf_to_debt = float(fina.get('ocf_to_debt', 0) or 0) if fina else 0

    result["details"]["ROE"] = round(roe, 2)
    result["details"]["or_yoy"] = round(or_yoy, 2)
    result["details"]["debt_to_assets"] = round(debt_to_assets, 2)
    result["details"]["gpm"] = round(gpm, 2)

    # report period alignment check (patch 6)
    if fina and basic.get('trade_date') and fina.get('ann_date'):
        try:
            d1 = datetime.strptime(str(basic['trade_date']), '%Y%m%d')
            d2 = datetime.strptime(str(fina['ann_date']), '%Y%m%d')
            diff = abs((d1 - d2).days)
            if diff > 90:
                result["warnings"].append(f"[stale_data] basic {basic['trade_date']} vs fina {fina['ann_date']} diff={diff}d")
        except Exception:
            pass

    # --- Step 3: technicals (keep original logic) ---
    kline = get_kline_with_indicators(symbol, days=70)
    if "latest" not in kline or "error" in kline:
        result["pass"] = False
        result["verdict"] = "REJECT"
        result["reason"] = "技术面数据不足"
        return result

    latest = kline["latest"]
    rsi6 = latest.get("RSI", 50)
    ma5 = latest.get("MA5", 0)
    ma20 = latest.get("MA20", 0)
    ma60 = latest.get("MA60", 0)
    macd_bar = latest.get("MACD柱", 0)
    boll_up = latest.get("BOLL上", 0)

    result["details"]["RSI6"] = rsi6
    result["details"]["MA_align"] = kline["summary"].get("均线排列", "")

    # --- Forbidden list (keep original) ---
    if total_mv and total_mv / 10000 < 100:
        result["pass"] = False
        result["rejected_by"].append(f"市值{round(total_mv/10000,1)}亿<100亿")
    if rsi6 > 65:
        result["pass"] = False
        result["rejected_by"].append(f"RSI6={rsi6}>65超买(V4.1)")
    if close and boll_up and close > boll_up:
        result["pass"] = False
        result["rejected_by"].append(f"价格{close}>布林上轨{boll_up}")
    if ma5 and ma20 and ma60 and ma5 < ma20 < ma60:
        result["pass"] = False
        result["rejected_by"].append("均线空头排列")

    # === Q2: profitability (per-style ROE threshold) ===
    q2_pass = True
    q2_reasons = []
    roe_min_map = {'A': 8, 'B': 10, 'C': 8, 'D': 12, 'E': 8}
    roe_min = roe_min_map.get(style_group, 12)

    if roe <= 0:
        q2_pass = False
        q2_reasons.append(f"ROE={roe}%<=0")
    elif roe < roe_min:
        q2_pass = False
        q2_reasons.append(f"ROE={roe}%<{roe_min}%({style_group}组)")

    if style_group == 'C' and or_yoy < 15:
        q2_pass = False
        q2_reasons.append(f"营收增速{or_yoy}%<15%(成长组)")

    result["Q2_能赚钱"] = {"pass": q2_pass, "reasons": q2_reasons if q2_reasons else [f"ROE={roe}%达标"]}

    # === Q3: valuation (5 routes) ===
    q3_pass = False
    q3_reasons = []
    q3_details = {}
    PHARMA_INDUSTRIES = {'中成药', '化学制药', '生物制药', '医疗保健', '医药商业'}
    BROKERAGE_INDUSTRIES = {'证券'}

    use_peg = (industry in PHARMA_INDUSTRIES) or (style_group == 'C')
    if use_peg:
        # C组/医药 -> PEG route
        g_capped = min(or_yoy, 50) if or_yoy > 0 else 0
        if g_capped <= 0:
            q3_reasons.append(f"营收增速{or_yoy}%<=0, PEG无法计算")
        elif pe_ttm <= 0:
            q3_reasons.append(f"PE={pe_ttm}<=0, PEG无法计算")
        else:
            peg = round(pe_ttm / g_capped, 2)
            q3_details["PEG"] = peg
            q3_details["G_capped"] = f"{g_capped}%(raw={or_yoy}%,cap=50%)"
            if peg <= 1.0:
                q3_pass = True
                q3_reasons.append(f"PEG={peg}<=1.0")
            else:
                q3_reasons.append(f"PEG={peg}>1.0")

    elif style_group == 'A':
        pct = _get_valuation_percentile(symbol, 5)
        if not pct:
            q3_reasons.append("无法获取分位数")
        elif pct['data_points'] < 250:
            q3_reasons.append(f"样本{pct['data_points']}<250")
            result["warnings"].append(f"[INSUFFICIENT_DATA] {pct['data_points']}pts")
        else:
            pe_pct = pct.get('pe_ttm', {}).get('percentile')
            pb_pct = pct.get('pb', {}).get('percentile')
            q3_details["PE_pct"] = pe_pct
            q3_details["PB_pct"] = pb_pct
            pe_ok = pe_pct is not None and pe_pct <= 40
            pb_ok = pb_pct is not None and pb_pct <= 50
            if pe_ok or pb_ok:
                q3_pass = True
                by = []
                if pe_ok: by.append(f"PE分位{pe_pct}%<=40%")
                if pb_ok: by.append(f"PB分位{pb_pct}%<=50%")
                q3_reasons.append(f"周期OR: {', '.join(by)}")
            else:
                q3_reasons.append(f"PE分位{pe_pct}%>40% 且 PB分位{pb_pct}%>50%")

    elif style_group == 'B':
        q3_details["PB"] = pb
        if industry in BROKERAGE_INDUSTRIES:
            # 券商走PB分位数(跟周期股同逻辑, PB合理区间1.0-2.0)
            pct_b = _get_valuation_percentile(symbol, 5)
            if not pct_b:
                q3_reasons.append("无法获取分位数")
            elif pct_b['data_points'] < 250:
                q3_reasons.append(f"样本量{pct_b['data_points']}<250不足")
            else:
                pb_pct_b = pct_b.get('pb', {}).get('percentile')
                q3_details["PB分位"] = f"{pb_pct_b}%"
                if pb_pct_b is not None and pb_pct_b <= 50:
                    q3_pass = True
                    q3_reasons.append(f"券商PB分位{pb_pct_b}%<=50%")
                else:
                    q3_reasons.append(f"券商PB分位{pb_pct_b}%>50%")
        else:
            # 银行/保险走PB绝对值破净
            if 0 < pb <= 1.0:
                q3_pass = True
                q3_reasons.append(f"PB={pb}<=1.0破净")
            else:
                q3_reasons.append(f"PB={pb}>1.0未破净")

    elif style_group == 'D':
        pct = _get_valuation_percentile(symbol, 5)
        if not pct:
            q3_reasons.append("无法获取分位数")
        elif pct['data_points'] < 250:
            q3_reasons.append(f"样本{pct['data_points']}<250")
            result["warnings"].append(f"[INSUFFICIENT_DATA] {pct['data_points']}pts")
        else:
            pe_pct = pct.get('pe_ttm', {}).get('percentile')
            pb_pct = pct.get('pb', {}).get('percentile')
            q3_details["PE_pct"] = pe_pct
            q3_details["PB_pct"] = pb_pct
            pe_ok = pe_pct is not None and pe_pct <= 50
            pb_ok = pb_pct is not None and pb_pct <= 65
            if pe_ok and pb_ok:
                q3_pass = True
                q3_reasons.append(f"PE分位{pe_pct}%<=50% 且 PB分位{pb_pct}%<=65%")
            else:
                fails = []
                if not pe_ok and pe_pct is not None: fails.append(f"PE分位{pe_pct}%>50%")
                if not pb_ok and pb_pct is not None: fails.append(f"PB分位{pb_pct}%>65%")
                q3_reasons.append(f"消费AND未通过: {', '.join(fails)}")

    elif style_group == 'E':
        q3_details["div_yield"] = dv_ttm
        div_ok = dv_ttm >= 3.0
        pct = _get_valuation_percentile(symbol, 5)
        pb_pct = pct.get('pb', {}).get('percentile') if pct else None
        if pb_pct is not None:
            q3_details["PB_pct"] = pb_pct
        pb_ok = pb_pct is not None and pb_pct <= 40
        if div_ok or pb_ok:
            q3_pass = True
            by = []
            if div_ok: by.append(f"股息率{dv_ttm}%>=3%")
            if pb_ok: by.append(f"PB分位{pb_pct}%<=40%")
            q3_reasons.append(f"稳定OR: {', '.join(by)}")
        else:
            q3_reasons.append(f"股息率{dv_ttm}%<3% 且 PB分位{pb_pct}>40%")

    result["Q3_价格合理"] = {"pass": q3_pass, "reasons": q3_reasons, "details": q3_details}

    # === Q5: safety net (per-style, partial Phase 2) ===
    q5_pass = True
    q5_reasons = []
    if style_group == 'A':
        if debt_to_assets > 60:
            q5_pass = False
            q5_reasons.append(f"资产负债率{debt_to_assets}%>60%")
        else:
            q5_reasons.append(f"资产负债率{debt_to_assets}%<=60%")
    elif style_group == 'B':
        q5_reasons.append("[Phase2] 拨备覆盖率待接入")
    elif style_group == 'C':
        rd_ratio = _get_rd_ratio(symbol)
        if rd_ratio is None:
            q5_reasons.append("[数据缺失] 研发费率无法获取")
        elif rd_ratio < 5:
            q5_pass = False
            q5_reasons.append(f"研发费率{rd_ratio}%偏低(<5%)")
        else:
            q5_reasons.append(f"研发费率{rd_ratio}%达标(>=5%)")
    elif style_group == 'D':
        if 0 < gpm < 20:
            q5_pass = False
            q5_reasons.append(f"毛利率{gpm}%偏低(固定阈值20%)[Phase2改行业中位数]")
        else:
            q5_reasons.append(f"毛利率{gpm}%达标(固定阈值20%)[Phase2改行业中位数]")
    elif style_group == 'E':
        ocf_to_or = float(fina.get('ocf_to_or', 0) or 0) if fina else 0
        ocf_pct = round(ocf_to_or * 100, 1)
        if ocf_to_or > 0 and ocf_to_or < 0.05:
            q5_pass = False
            q5_reasons.append(f"经营现金流/营收{ocf_pct}%偏低(<5%)")
        elif ocf_to_or == 0:
            q5_reasons.append("[Phase2] 经营现金流/营收数据缺失")
        else:
            q5_reasons.append(f"经营现金流/营收{ocf_pct}%达标")

    result["Q5_安全垫"] = {"pass": q5_pass, "reasons": q5_reasons}

    # === Q1: trend (simplified original) ===
    q1_pass = True
    q1_reasons = []
    if ma5 and ma20 and not (ma5 > ma20):
        q1_pass = False
        q1_reasons.append("MA5<MA20趋势偏弱")
    if macd_bar < 0:
        q1_pass = False
        q1_reasons.append("MACD柱为负")
    result["Q1_趋势向上"] = {"pass": q1_pass, "reasons": q1_reasons if q1_reasons else ["趋势偏多"]}

    # --- Final verdict ---
    result["three_questions"] = {
        "Q1": result["Q1_趋势向上"],
        "Q2": result["Q2_能赚钱"],
        "Q3": result["Q3_价格合理"],
        "Q5": result["Q5_安全垫"]
    }

    if not result["pass"]:
        result["verdict"] = "REJECT"
        result["reason"] = "；".join(result["rejected_by"])
    elif not all(result["three_questions"][q]["pass"] for q in result["three_questions"]):
        result["verdict"] = "REJECT"
        all_r = []
        for qn, qr in result["three_questions"].items():
            if not qr["pass"]:
                all_r.extend(qr["reasons"])
        result["reason"] = "；".join(all_r)
        result["pass"] = False
    else:
        result["verdict"] = "PASS"
        result["reason"] = f"通过v4.1五风格组筛选 {fv_hash}"

    return result



def main():
    try:
        raw = sys.stdin.read().strip()
        if not raw:
            print(json.dumps({"error": "无输入"}, ensure_ascii=False))
            return

        cmd = json.loads(raw)
        try:
            with open("probe_raw.json", "w", encoding="utf-8") as _f:
                _f.write(raw[:2000])
        except Exception:
            pass
        action = cmd.get("action", "") or cmd.get("command", "")
        symbol = cmd.get("symbol", "")
        symbols = cmd.get("symbols", [])
        # M10b-2026-09-08: symbols单复数容错 -- symbol含逗号且symbols缺省时自动路由
        if not symbols and isinstance(symbol, str) and "," in symbol:
            symbols = [s.strip() for s in symbol.split(",") if s.strip()]

        params = cmd.get("params", {})
        if isinstance(params, str):
            try:
                params = json.loads(params)
                if not isinstance(params, dict):
                    raise ValueError("params JSON必须为对象")
            except Exception:
                # M10-2026-09-08: params静默降级总闸修复
                # 先试k=v逗号串解析, 仍失败则报错拒绝执行(不再静默吞成{})
                parsed = {}
                in_quote = False
                cur_key = ""
                cur_val = ""
                on_key = True
                saw_eq = False
                bad_seg = False
                for ch in params:
                    if ch == chr(34):
                        in_quote = not in_quote
                        continue
                    if ch == "=" and not in_quote and on_key:
                        on_key = False
                        saw_eq = True
                        continue
                    if ch == "," and not in_quote:
                        if cur_key.strip() and saw_eq:
                            parsed[cur_key.strip()] = cur_val.strip()
                        elif cur_key.strip():
                            bad_seg = True
                        cur_key = ""
                        cur_val = ""
                        on_key = True
                        saw_eq = False
                        continue
                    if on_key:
                        cur_key += ch
                    else:
                        cur_val += ch
                if cur_key.strip():
                    if saw_eq:
                        parsed[cur_key.strip()] = cur_val.strip()
                    else:
                        bad_seg = True
                if parsed and not bad_seg:
                    def _auto_type(s):
                        try:
                            return int(s)
                        except ValueError:
                            try:
                                return float(s)
                            except ValueError:
                                return s
                    params = {k: _auto_type(v) for k, v in parsed.items()}
                else:
                    out = {"status": "success", "result": {"error": "params格式无法解析(既非JSON亦非k=v): " + str(params)[:80]}}
                    print(json.dumps(out, ensure_ascii=False))
                    return

        log(f"action={action} symbol={symbol}")

        if action == "realtime_quote":
            out = {"status": "success", "result": get_realtime_quote(symbol)}

        elif action == "batch_quotes":
            if not symbols:
                out = {"status": "success", "result": {"error": "batch_quotes需要symbols参数(逗号分隔,如: 601899,000807)"}}
            else:
                out = {"status": "success", "result": get_batch_quotes(symbols)}

        elif action == "kline_indicators":
            days = params.get("days", 120)
            out = {"status": "success", "result": get_kline_with_indicators(symbol, days)}

        elif action == "risk_halt_reset":
            # 22c gate-2 manual lift - supervised use only (不进日报白名单)
            out = _risk_halt_reset(params.get("cleared_until"), params.get("reset_by"), params.get("evidence"))

        elif action == "position_size":
            # 22c 3/4 ATR sizer - entry可选, 缺省用最新收盘
            out = _position_size(symbol, params.get("entry"))

        elif action == "stock_info":
            out = {"status": "success", "result": get_stock_info(symbol)}

        elif action == "capital_flow":
            out = {"status": "success", "result": get_capital_flow(symbol)}

        elif action == "sector_ranking":
            out = {"status": "success", "result": get_sector_ranking()}

        elif action == "full_analysis":
            kline = get_kline_with_indicators(symbol)
            quote = get_realtime_quote(symbol)

            if "error" in quote and "latest" in kline:
                recent = kline.get("recent_3days", [])
                lk = kline["latest"]
                quote = {"代码": symbol, "最新价": lk.get("收盘", 0), "涨跌幅": 0, "数据来源": "K线降级"}
                if len(recent) >= 2:
                    tc = recent[-1].get("收盘", 0)
                    yc = recent[-2].get("收盘", 0)
                    if yc > 0:
                        quote["涨跌幅"] = round((tc - yc) / yc * 100, 2)

            info = get_stock_info(symbol)
            flow = get_capital_flow(symbol)

            # 附加daily_basic到技术面（PE/PB/换手率/量比）
            basic = _get_daily_basic(symbol)
            if basic and "latest" in kline:
                kline["latest"]["PE_TTM"] = round(basic.get('pe_ttm', 0) or 0, 1)
                kline["latest"]["PB"] = round(basic.get('pb', 0) or 0, 2)
                kline["latest"]["换手率"] = round(basic.get('turnover_rate', 0) or 0, 2)
                kline["latest"]["量比"] = round(basic.get('volume_ratio', 0) or 0, 2)

            out = {"status": "success", "result": {"行情": quote, "技术面": kline, "基本面": info, "资金面": flow}}

        # ===== 新增命令 =====

        elif action == "scan_anomalies":
            out = {"status": "success", "result": scan_anomalies_enhanced(symbols if symbols else None)}

        elif action == "daily_report":
            out = {"status": "success", "result": daily_report()}

        elif action == "watchlist_add":
            name = cmd.get("name", "") or params.get("name", "")
            if not symbol:
                out = {"status": "error", "message": "缺少symbol参数"}
            else:
                out = {"status": "success", "result": watchlist_add(symbol, name)}

        elif action == "watchlist_remove":
            if not symbol:
                out = {"status": "error", "message": "缺少symbol参数"}
            else:
                out = {"status": "success", "result": watchlist_remove(symbol)}

        elif action == "watchlist_show":
            out = {"status": "success", "result": watchlist_show()}

        elif action == "position_add":
            p_name = params.get("name") or cmd.get("name", "")
            p_cost = params.get("cost") or cmd.get("cost", 0)
            p_shares = params.get("shares") or cmd.get("shares", 0)
            p_stop = params.get("stop_loss") or cmd.get("stop_loss", 0)
            p_target = params.get("target") or cmd.get("target", 0)
            p_reason = params.get("reason") or cmd.get("reason", "")
            if not symbol or not p_cost or not p_shares:
                out = {"status": "error", "message": "缺少必要参数: symbol/cost/shares"}
            else:
                out = {"status": "success", "result": position_add(symbol, p_name, p_cost, p_shares, p_stop, p_target, p_reason, params.get("override_market"), params.get("override_budget"), params.get("override_by"), params.get("override_reason"))}

        elif action == "position_close":
            p_price = params.get("sell_price") or cmd.get("sell_price", 0)
            p_shares = params.get("shares") or cmd.get("shares")
            p_reason = params.get("reason") or cmd.get("reason", "")
            p_commission = params.get("commission") or cmd.get("commission", 5)
            if not symbol or not p_price:
                out = {"status": "error", "message": "缺少必要参数: symbol/sell_price"}
            else:
                out = {"status": "success", "result": position_close(symbol, p_price, p_shares, p_reason, p_commission)}

        elif action == "position_update":
            p_stop = params.get("stop_loss") or cmd.get("stop_loss")
            p_target = params.get("target") or cmd.get("target")
            if not symbol:
                out = {"status": "error", "message": "缺少symbol参数"}
            else:
                out = {"status": "success", "result": position_update(symbol, p_stop, p_target)}

        elif action == "position_remove":
            if not symbol:
                out = {"status": "error", "message": "缺少symbol参数"}
            else:
                out = {"status": "success", "result": position_remove(symbol)}

        elif action == "position_show":
            out = {"status": "success", "result": position_show()}

        elif action == "trade_history":
            out = {"status": "success", "result": trade_history(symbol if symbol else None)}

        elif action == "trade_stats":
            out = {"status": "success", "result": trade_stats()}

        elif action == "portfolio_summary":
            out = {"status": "success", "result": portfolio_summary()}

        elif action == "account_set":
            p_capital = params.get("total_capital", 0)
            p_cash = params.get("available_cash")
            if not p_capital:
                out = {"status": "error", "message": "缺少参数: total_capital"}
            else:
                out = {"status": "success", "result": account_set(p_capital, p_cash)}

        elif action == "account_show":
            out = {"status": "success", "result": read_account()}

        elif action == "stock_screen":
            out = {"status": "success", "result": stock_screen(symbol)}

        elif action == "market_check":
            out = {"status": "success", "result": market_check()}

        elif action == "lhb_detail":
            p_days = params.get("days", 5)
            out = {"status": "success", "result": _ak_lhb_detail(symbol, p_days)}

        elif action == "block_trade":
            p_days = params.get("days", 5)
            out = {"status": "success", "result": _ak_block_trade(symbol, p_days)}

        elif action == "share_unlock":
            out = {"status": "success", "result": _ak_share_unlock()}

        elif action == "earnings_forecast":
            p_date = params.get("date", "")
            forecast_data, report_date = _ak_earnings_forecast(p_date if p_date else None)
            out = {"status": "success", "result": {"report_date": report_date, "count": len(forecast_data), "records": forecast_data}}

        elif action == "scan_events":
            p_days = params.get("days", 5)
            out = {"status": "success", "result": scan_events(symbols if symbols else None, p_days)}

        elif action == "sentiment_scan":
            out = {"status": "success", "result": sentiment_scan(symbol if symbol else None, symbols if symbols else None)}

        elif action == "sentiment_rank":
            out = {"status": "success", "result": {"count": 0, "records": _ak_sentiment_market_rank()}}

        elif action == "stress_test":
            p_scenario = params.get("scenario", "crash_2015")
            p_custom = params.get("custom_drop")
            out = {"status": "success", "result": stress_test(p_scenario, None, p_custom)}

        elif action == "sector_rotation":
            out = {"status": "success", "result": sector_rotation()}

        elif action == "market_temperature":
            out = {"status": "success", "result": market_temperature()}

        elif action == "trade_stats_monthly":
            out = {"status": "success", "result": trade_stats_monthly()}

        elif action == "update_trailing_stops":
            out = {"status": "success", "result": update_trailing_stops()}

        elif action == "backtest":
            p_start = params.get("start_date", "20240101")
            p_end = params.get("end_date", "20241231")
            p_strategy = params.get("strategy", "ma_cross")
            p_capital = params.get("initial_capital", 100000)
            out = {"status": "success", "result": backtest(symbol, p_start, p_end, p_strategy, p_capital)}

        elif action == "valuation_percentile":
            p_years = int(params.get("years", 5))
            result = _get_valuation_percentile(symbol, p_years)
            if result:
                out = {"status": "success", "result": result}
            else:
                out = {"status": "error", "message": f"无法获取{symbol}的历史估值数据"}

        elif action == "harvest_judgments":
            # 22a: judgment ledger harvest wrapper (决策: 翔 2026-09-03 "能用插件实现的需求尽量用插件")
            # subprocess keeps harvest_judgments.py independently runnable; PYTHONIOENCODING guards
            # CJK filenames on Windows pipes (GBK default); 110s timeout guards stuck scans (L7: 10s below plugin comm timeout).
            import subprocess as _sp
            try:
                _env = {**os.environ, "PYTHONIOENCODING": "utf-8"}
                _p = _sp.run(
                    [sys.executable, os.path.join(PLUGIN_DIR, "harvest_judgments.py")],
                    capture_output=True, text=True, encoding="utf-8",
                    timeout=110, cwd=PLUGIN_DIR, env=_env)  # L7: 10s headroom below plugin comm timeout so subprocess timeout error returns intact (Nova audit round 3)
                _raw = (_p.stdout or "").strip()
                try:
                    _rpt = json.loads(_raw)
                except Exception:
                    _rpt = {"status": "error", "message": f"harvest output not JSON: {_raw[:200]}"}
                _rpt["exit_code"] = _p.returncode
                if _p.stderr:
                    _rpt["stderr_tail"] = _p.stderr[-300:]
                out = {"status": "success", "result": _rpt}
            except Exception as _e:
                out = {"status": "error", "message": f"harvest_judgments failed: {str(_e)[:120]}"}

        elif action == "exemption_check":
            # #27-③ (2026-09-13 观澜): _exemption_check本为模块级函数(L3278), 本分支仅暴露为可独立调用
            # 单票弱市豁免三证明查询: 板块庇护/个股独立/资金续流 —— batch_screen与单票共用此函数(单一事实源)
            # 闸内调用链 position_add→_market_factor→_exemption_check 零改动
            _sym_exp = str(cmd.get("symbol", "") or params.get("symbol", "")).strip()
            if not (_sym_exp.isdigit() and len(_sym_exp) == 6):
                out = {"status": "error", "message": "exemption_check需要symbol参数(六位代码, 如601899)"}
            else:
                out = {"status": "success", "result": _exemption_check(_sym_exp),
                       "note": "弱市豁免三证明查询; rotation数据滞后约2交易日, 结果带时点性; 仅空头市场有意义(多头全场1.0系数)"}

        elif action == "batch_screen":
            # #27 批量三问 (2026-09-13): symbols支持数组(JSON)与逗号串(k=v)双形态
            _syms = params.get("symbols", cmd.get("symbols", ""))
            _wf = params.get("with_flow", True)
            _we = params.get("with_exemption", False)  # 会审裁决②: 默认false要开显式传
            # M13 fix (Nova r12): M10的auto_type对k=v布尔留字符串, "false"在Python是truthy——
            # 显式转换防语义反转(想关的人传false实际开着, 与裁决②精神相反的暗门)
            if isinstance(_wf, str):
                _wf = _wf.lower() not in ("false", "0", "no")
            if isinstance(_we, str):
                _we = _we.lower() not in ("false", "0", "no")
            # M15-2026-09-21 (翔批21:27授权): 批量三问框架路径异步化(funnel_daily同款模式)
            # 根治裸壳: 十连验证main.py清白, 病灶在框架收割层, 同步stdout单发慢回必死.
            # 毫秒级回running+后台runner跑真身+同参数批号缓存, 原函数本体零改动.
            import hashlib as _h15, subprocess as _sp15
            if isinstance(_syms, str):
                _symlist = [s.strip() for s in _syms.split(",") if s.strip()]
            else:
                _symlist = [str(s).strip() for s in (_syms or []) if str(s).strip()]
            _symlist = [s for s in _symlist if s.isdigit() and len(s) == 6][:30]
            if not _symlist:
                out = {"status": "error", "message": "symbols为空或格式无效(需六位代码, 逗号分隔或数组)"}
            else:
                _key15 = _h15.md5(("|".join(_symlist) + "|" + str(bool(_wf)) + "|" + str(bool(_we))).encode("utf-8")).hexdigest()[:10]
                _rpath = os.path.join(PLUGIN_DIR, "market_data", "batch_result_" + _key15 + ".json")
                _res15 = None
                if os.path.exists(_rpath):
                    try:
                        if time.time() - os.path.getmtime(_rpath) < 600:
                            with open(_rpath, "r", encoding="utf-8") as _f15:
                                _res15 = json.load(_f15)
                            _res15["source"] = "cache"
                    except Exception:
                        _res15 = None
                # M17b-2026-09-22(翔建议): runner刚起跑时插件内轮询等待——GuanLan自取回, PowerShell退出循环
                if _res15 is None:
                    _lf15 = os.path.join(PLUGIN_DIR, "market_data", "batch_" + _key15 + ".log")
                    if os.path.exists(_lf15) and (time.time() - os.path.getmtime(_lf15)) < 150:
                        for _w15 in range(34):
                            time.sleep(5)
                            if os.path.exists(_rpath):
                                try:
                                    with open(_rpath, "r", encoding="utf-8") as _f15:
                                        _res15 = json.load(_f15)
                                    _res15["source"] = "cache"
                                except Exception:
                                    _res15 = None
                                break
                if _res15 is not None:
                    out = {"status": "success", "result": _res15}
                else:
                    _reqj = json.dumps({"symbols": _symlist, "with_flow": bool(_wf), "with_exemption": bool(_we), "out_path": _rpath}, ensure_ascii=False)
                    _env15 = {**os.environ, "PYTHONIOENCODING": "utf-8"}
                    try:
                        _mdir15 = os.path.join(PLUGIN_DIR, "market_data")
                        if not os.path.isdir(_mdir15):
                            os.makedirs(_mdir15)
                        _lfo = open(os.path.join(_mdir15, "batch_" + _key15 + ".log"), "w", encoding="utf-8")
                        _lfe = open(os.path.join(_mdir15, "batch_" + _key15 + "_err.log"), "w", encoding="utf-8")
                        _sp15.Popen([sys.executable, os.path.join(PLUGIN_DIR, "batch_runner.py"), _reqj],
                                    stdout=_lfo, stderr=_lfe, cwd=PLUGIN_DIR, env=_env15,
                                    creationflags=0x00000008)
                        out = {"status": "success", "result": {"status": "running", "batch_id": _key15, "count": len(_symlist), "note": "后台runner已起跑(含库导入约20-40s, 30只约2-3分钟); 同参数重发本命令即取缓存结果; 缓存10分钟新鲜期, 过期自动重跑"}}
                    except Exception as _e15:
                        out = {"status": "error", "message": "runner起跑失败: " + str(_e15)[:120]}

        elif action == "settle_results":
            # 23d收尾 (2026-09-20): 到期判断结算包装为action, 挂日报步骤2.85
            # subprocess保持脚本独立可跑(dry-run/手动); 结算=本地kline库计算秒级, timeout 110s兜底
            import subprocess as _sp
            try:
                _env = {**os.environ, "PYTHONIOENCODING": "utf-8"}
                _p = _sp.run(
                    [sys.executable, os.path.join(PLUGIN_DIR, "settle_results.py")],
                    capture_output=True, text=True, encoding="utf-8",
                    timeout=110, cwd=PLUGIN_DIR, env=_env)
                _raw = (_p.stdout or "").strip()
                try:
                    _rpt = json.loads(_raw)  # settle输出为单一JSON报告(indent多行, 整体解析)
                except Exception:
                    _rpt = {"status": "error", "message": f"settle output not JSON: {_raw[:200]}"}
                _rpt["exit_code"] = _p.returncode
                if _p.stderr:
                    _rpt["stderr_tail"] = _p.stderr[-300:]
                out = {"status": "success", "result": _rpt}
            except Exception as _e:
                out = {"status": "error", "message": f"settle_results failed: {str(_e)[:120]}"}

        elif action == "funnel_daily":
            # V4.3.1 异步化 2026-09-09 翔批: 死锁三角(本体~180s > timeout 110s > 通信墙60s)根治
            # 四路径状态机: A产物在->缓存秒回 / B无产物->后台起跑+秒回running / C运行中->秒回进度 / D标记>10min->僵尸自愈
            # 原则: 产物文件是唯一事实源, 回执只报状态. 日期通道: params.date 或 command暗门(8位数字, 兼容Nova r8旧约)
            import subprocess as _sp
            import datetime as _dt
            try:
                _env = {**os.environ, "PYTHONIOENCODING": "utf-8"}
                _date = None
                if params.get("date"):
                    _d = str(params["date"]).strip()
                    if len(_d) == 8 and _d.isdigit():
                        _date = _d
                _cmd_field = str(cmd.get("command", "") or "")
                if not _date and _cmd_field.strip() and _cmd_field != "funnel_daily":
                    _d = _cmd_field.strip()
                    if len(_d) == 8 and _d.isdigit():
                        _date = _d
                if not _date:
                    _date = _dt.date.today().strftime("%Y%m%d")

                _prod = os.path.join(PLUGIN_DIR, "market_data", f"final_pool_{_date}.json")
                _run_flag = os.path.join(PLUGIN_DIR, "market_data", f".funnel_running_{_date}")

                if os.path.exists(_prod):
                    # 路径A: 缓存命中 - 优先读同日log完整报告, fallback产物计数
                    _summary = None
                    for _flog in (os.path.join(PLUGIN_DIR, f"funnel_{_date}.log"),
                                  os.path.join(PLUGIN_DIR, f"funnel_{_date[4:]}.log")):
                        if os.path.exists(_flog):
                            try:
                                with open(_flog, "r", encoding="utf-8") as _f:
                                    _lines = [l.strip() for l in _f if l.strip()]
                                if _lines:
                                    _summary = json.loads(_lines[-1])
                                    break
                            except Exception:
                                _summary = None
                    if isinstance(_summary, dict):
                        _summary["source"] = "cache"
                        out = {"status": "success", "result": _summary}
                    else:
                        try:
                            with open(_prod, "r", encoding="utf-8") as _f:
                                _pool = json.load(_f)
                            _meta = _pool.get("_meta", {}) if isinstance(_pool, dict) else {}
                            _items = _pool.get("items", []) if isinstance(_pool, dict) else (_pool if isinstance(_pool, list) else [])
                            out = {"status": "success", "result": {"status": "ok", "source": "cache",
                                   "trade_date": _meta.get("trade_date", _date),
                                   "l1": _meta.get("l1"), "l2": _meta.get("l2"), "fina_pool": _meta.get("fina_pool"),
                                   "final_count": len(_items),
                                   "pool_name": "候选池",  # 命名约定(翔2026-09-14): 三层池=候选池->观察池(watchlist)->持仓
                                   "fina_source": _meta.get("fina_source"), "prev_pool_date": _meta.get("prev_pool_date")}}
                        except Exception as _e:
                            out = {"status": "success", "result": {"status": "error", "trade_date": _date, "message": f"产物损坏: {str(_e)[:80]}"}}
                else:
                    _need_start = True
                    _note = None
                    if os.path.exists(_run_flag):
                        try:
                            _age = time.time() - os.path.getmtime(_run_flag)
                        except Exception:
                            _age = 99999.0
                        if _age <= 600:  # L14注记(Nova r11): mtime年龄依赖系统时钟稳定, NTP跳变可致误判重跑(观察级, Windows低概率)
                            # 路径C: 仍在跑
                            _need_start = False
                            out = {"status": "success", "result": {"status": "running", "trade_date": _date, "elapsed_min": round(_age / 60, 1), "note": "产物落盘后再调用本命令取缓存报告"}}
                        else:
                            # 路径D: 僵尸 - 清标记落到B重跑
                            try:
                                os.remove(_run_flag)
                            except Exception:
                                pass
                            _note = f"前次标记超{int(_age / 60)}分钟无产物, 疑似僵尸已清理, 重跑"
                    if _need_start:
                        # 路径B: 冷启动 - 写标记+后台起跑(DETACHED, 父进程退出不杀子)+秒回
                        _lf = _ef = None  # L13 fix (Nova r11): Popen异常时句柄也关 - finally统一收口, 成功/失败两态都关且只关一次
                        try:
                            with open(_run_flag, "w", encoding="utf-8") as _f:
                                _f.write(_dt.datetime.now().isoformat())
                            _flog = os.path.join(PLUGIN_DIR, f"funnel_{_date}.log")
                            _lf = open(_flog, "w", encoding="utf-8")
                            _ef = open(_flog[:-4] + "_err.log", "w", encoding="utf-8")
                            _sp.Popen([sys.executable, os.path.join(PLUGIN_DIR, "funnel_daily.py"), _date],
                                      stdout=_lf, stderr=_ef, cwd=PLUGIN_DIR, env=_env,
                                      creationflags=0x00000008)
                            _res = {"status": "running", "trade_date": _date,
                                        "note": f"已后台起跑, 约3分钟产物落盘(final_pool_{_date}.json), 再调用本命令走缓存路径取报告"}
                            if _note:
                                _res["restart"] = _note
                            out = {"status": "success", "result": _res}
                        except Exception as _pe:
                            try:
                                os.remove(_run_flag)
                            except Exception:
                                pass
                            out = {"status": "success", "result": {"status": "error", "trade_date": _date, "message": f"后台起跑失败: {str(_pe)[:80]}"}}
                        finally:
                            # L13 fix (Nova r11): 成功/异常两态句柄统一收口
                            if _lf is not None:
                                _lf.close()
                            if _ef is not None:
                                _ef.close()
            except Exception as _e:
                out = {"status": "error", "message": f"funnel_daily failed: {str(_e)[:120]}"}

        else:
            out = {"status": "error", "message": f"未知操作: {action}"}

        print(json.dumps(out, ensure_ascii=False, default=str))

    except json.JSONDecodeError as e:
        print(json.dumps({"status": "error", "message": f"JSON错误: {e}"}, ensure_ascii=False))
    except Exception as e:
        print(json.dumps({"status": "error", "message": f"异常: {str(e)[:150]}"}, ensure_ascii=False))


if __name__ == "__main__":
    main()
