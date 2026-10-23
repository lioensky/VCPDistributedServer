"""GuanLan environment configuration.

VCP supplies declared configSchema keys to plugin subprocesses.
This module does not load files or mutate os.environ.
Never include credential values in diagnostics.
"""
import math
import os
from pathlib import Path


class ConfigError(ValueError):
    """Invalid deployment configuration; messages contain names, not values."""


def _number(env, key, default, upper, allow_zero=True):
    raw = env.get(key)
    if raw is None:
        return default
    if isinstance(raw, bool):
        raise ConfigError("Invalid numeric configuration: " + key)
    try:
        value = float(raw)
    except (TypeError, ValueError, OverflowError):
        raise ConfigError("Invalid numeric configuration: " + key) from None
    lower_ok = value >= 0 if allow_zero else value > 0
    if not math.isfinite(value) or not lower_ok or value > upper:
        raise ConfigError("Out-of-range configuration: " + key)
    return value


def read_fee_config(env=None):
    """Preserve existing production defaults; reject malformed overrides.

    Bounds are input-sanity guards, not recommendations about broker fees.
    Taxes and transfer-fee rules remain in the shared fee engine.
    """
    env = os.environ if env is None else env
    return {
        "stock_rate": _number(
            env, "BROKER_COMMISSION_STOCK", 0.00025, 0.01),
        "etf_rate": _number(
            env, "BROKER_COMMISSION_ETF", 0.00025, 0.01),
        "minimum": _number(
            env, "BROKER_MIN_COMMISSION", 5.0, 1000.0),
    }


def read_tushare_token(env=None, required=False):
    env = os.environ if env is None else env
    raw = env.get("TUSHARE_TOKEN", "")
    if not isinstance(raw, str):
        raise ConfigError("Invalid configuration: TUSHARE_TOKEN")
    token = raw.strip()
    if required and not token:
        raise ConfigError("Missing configuration: TUSHARE_TOKEN")
    return token


def read_diary_config(plugin_dir, env=None):
    env = os.environ if env is None else env

    def text(key, default):
        raw = env.get(key, default)
        if not isinstance(raw, str) or not raw.strip():
            raise ConfigError("Invalid configuration: " + key)
        return raw.strip()

    agent = text("GUANLAN_AGENT_NAME", "观澜")
    model = text("GUANLAN_MODEL_VERSION", "glm-5.3")
    override = env.get("GUANLAN_DIARY_DIR", "")
    if not isinstance(override, str):
        raise ConfigError("Invalid configuration: GUANLAN_DIARY_DIR")
    if override.strip():
        diary_dir = Path(override.strip())
        if not diary_dir.is_absolute():
            raise ConfigError("GUANLAN_DIARY_DIR must be absolute")
    else:
        # An agent name is one directory component, not a path.
        if agent in (".", "..") or any(c in agent for c in ("/", "\\", ":")):
            raise ConfigError("Invalid directory component: GUANLAN_AGENT_NAME")
        diary_dir = Path(plugin_dir).resolve().parent.parent / "dailynote" / agent
    return {"agent": agent, "model_version": model, "diary_dir": diary_dir}