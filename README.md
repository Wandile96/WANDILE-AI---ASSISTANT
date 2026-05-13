# WANDILE AI - Forex SMC Analyzer Assistant

## Overview
An intelligent Forex pairs analyzer that reads market structure, Smart Money Concepts (SMC), Fair Value Gaps (FVG), and Order Blocks to generate accurate trade signals with full entry, take-profit (TP), and stop-loss (SL) levels.

## Features

### 📊 Market Analysis
- **Market Structure Detection**: Identifies trending vs ranging markets
- **Smart Money Concepts (SMC)**:
  - Higher Highs and Lower Lows detection
  - Order Block identification
  - CHoCH (Change of Character) detection
  - Mitigation Blocks
  
- **Fair Value Gap (FVG)** Detection
  - Bullish and Bearish FVGs
  - FVG levels tracking
  - FVG mitigation analysis

- **Trade Signal Generation**:
  - Entry points with precision
  - Take Profit levels (Full TP calculation)
  - Stop Loss levels
  - Risk:Reward ratio analysis

### 🚫 Range Detection
- Automatically identifies ranging structures
- Returns "NO TRADE" signal for ranging markets

## Installation

```bash
pip install -r requirements.txt
```

## Project Structure

```
.
├── README.md
├── requirements.txt
├── config.py                 # Configuration settings
├── data/
│   ├── fetcher.py           # OHLC data fetching
│   └── preprocessor.py      # Data preprocessing
├── analysis/
│   ├── market_structure.py   # Market structure analysis
│   ├── smc_detector.py       # SMC detection
│   ├── fvg_detector.py       # FVG detection
│   └── order_blocks.py       # Order block analysis
├── trading/
│   ├── signal_generator.py   # Trade signal generation
│   ├── level_calculator.py   # Entry, TP, SL calculation
│   └── risk_manager.py       # Risk management
├── analyzer.py               # Main analyzer class
├── backtester.py            # Backtesting engine
└── main.py                  # Entry point
```

## Usage

### Basic Analysis

```python
from analyzer import ForexAnalyzer

# Initialize analyzer
analyzer = ForexAnalyzer(pair='EURUSD', timeframe='1H')

# Get analysis
analysis = analyzer.analyze()

print(analysis)
```

### Output Example

```
{
    "pair": "EURUSD",
    "timeframe": "1H",
    "market_structure": "UPTREND",
    "signal": "BUY",
    "entry": 1.0850,
    "tp1": 1.0870,
    "tp2": 1.0890,
    "tp_full": 1.0910,
    "sl": 1.0830,
    "risk_reward": 4.0,
    "confidence": 0.87,
    "details": {
        "order_blocks": [...],
        "fvg_levels": [...],
        "smc_signals": [...]
    }
}
```

## Configuration

Edit `config.py` to customize:
- Data source (OHLC provider)
- Indicator parameters
- Risk management settings
- TP/SL calculation methods

## Supported Pairs

All major forex pairs: EURUSD, GBPUSD, USDJPY, AUDUSD, NZDUSD, etc.

## Timeframes

M5, M15, M30, H1, H4, D1, W1

## Future Enhancements

- [ ] Multi-timeframe analysis
- [ ] Machine learning trade signal optimization
- [ ] Real-time alerts
- [ ] Integration with MT4/MT5
- [ ] Performance statistics tracking

## Disclaimer

**IMPORTANT**: This tool is for educational purposes only. Forex trading involves substantial risk. Always use proper risk management and never risk more than you can afford to lose.

## License

MIT License
