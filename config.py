"""Configuration settings for Forex Analyzer"""

# Data Settings
DATA_SOURCE = 'yfinance'  # or 'ccxt', 'oanda'
LOOKBACK_PERIOD = 500  # Number of candles for analysis

# Market Structure Settings
MIN_SWING_SIZE = 5  # Minimum bars for swing detection
TREND_CONFIRMATION_BARS = 3  # Bars needed to confirm trend
RANGE_THRESHOLD = 0.60  # Percentage within range to classify as ranging (0-1)

# SMC Settings
ORDER_BLOCK_LOOKBACK = 20  # Bars to look back for order blocks
MITIGATION_THRESHOLD = 0.8  # Percentage of OB that needs mitigation (0-1)
CHOCH_CONFIRMATION = 2  # Bars to confirm CHoCH

# FVG Settings
FVG_MIN_SIZE = 0.0010  # Minimum gap size as percentage
FVG_LOOKBACK = 30  # Bars to identify FVGs
FVG_MITIGATION_THRESHOLD = 0.5  # Mitigation threshold

# Trade Signal Settings
RISK_REWARD_MINIMUM = 1.5  # Minimum acceptable RR ratio
TRADE_CONFIDENCE_MIN = 0.65  # Minimum confidence level (0-1)

# TP/SL Calculation Settings
SL_ATR_MULTIPLIER = 1.5  # ATR multiplier for SL
TP_ATR_MULTIPLIER = 3.0  # ATR multiplier for TP
TP_CALCULATION_METHOD = 'fvg'  # 'fvg', 'atr', 'fibonacci'

# Risk Management
RISK_PERCENT = 2.0  # Risk percentage per trade
MAX_POSITION_SIZE = 100000  # Maximum position size in units
MAX_DAILY_LOSS = 5.0  # Maximum daily loss percentage

# Backtesting Settings
BACKTEST_START_DATE = '2023-01-01'
BACKTEST_END_DATE = '2024-12-31'
INITIAL_BALANCE = 10000.0
COMMISSION = 0.0002  # 0.02% commission

# Logging
LOG_LEVEL = 'INFO'
LOG_FILE = 'logs/analyzer.log'

# Output Settings
DISPLAY_CHARTS = True
SAVE_ANALYSIS_PLOTS = True
PLOT_DIR = 'plots/'
