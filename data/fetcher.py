"""Data fetching module for OHLC data"""

import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta
import config


class DataFetcher:
    """Fetch OHLC data from various sources"""
    
    def __init__(self, pair, timeframe='1h'):
        """Initialize data fetcher
        
        Args:
            pair (str): Currency pair (e.g., 'EURUSD')
            timeframe (str): Timeframe (e.g., '1h', '4h', '1d')
        """
        self.pair = pair
        self.timeframe = timeframe
        self.data = None
    
    def fetch_yfinance(self, period='1y', interval='1h'):
        """Fetch data using yfinance
        
        Args:
            period (str): Period to fetch ('1d', '5d', '1mo', '3mo', '6mo', '1y')
            interval (str): Interval ('1m', '5m', '15m', '30m', '1h', '1d', '1wk')
            
        Returns:
            pd.DataFrame: OHLC data with columns [Open, High, Low, Close, Volume]
        """
        try:
            # yfinance uses ticker=pair format
            data = yf.download(self.pair, period=period, interval=interval, progress=False)
            self.data = data
            return data
        except Exception as e:
            print(f"Error fetching data from yfinance: {e}")
            return None
    
    def fetch_custom(self, start_date, end_date, interval='1h'):
        """Fetch data for custom date range
        
        Args:
            start_date (str): Start date (YYYY-MM-DD)
            end_date (str): End date (YYYY-MM-DD)
            interval (str): Interval
            
        Returns:
            pd.DataFrame: OHLC data
        """
        try:
            data = yf.download(self.pair, start=start_date, end=end_date, 
                             interval=interval, progress=False)
            self.data = data
            return data
        except Exception as e:
            print(f"Error fetching custom data: {e}")
            return None
    
    def get_latest_candles(self, count=config.LOOKBACK_PERIOD):
        """Get latest N candles
        
        Args:
            count (int): Number of candles to return
            
        Returns:
            pd.DataFrame: Latest OHLC data
        """
        if self.data is None:
            self.fetch_yfinance()
        
        return self.data.tail(count).copy()
    
    def add_indicators(self, df):
        """Add technical indicators to dataframe
        
        Args:
            df (pd.DataFrame): OHLC dataframe
            
        Returns:
            pd.DataFrame: DataFrame with indicators
        """
        # ATR
        df['TR'] = df['High'] - df['Low']
        df['ATR'] = df['TR'].rolling(window=14).mean()
        
        # RSI
        delta = df['Close'].diff()
        gain = (delta.where(delta > 0, 0)).rolling(window=14).mean()
        loss = (-delta.where(delta < 0, 0)).rolling(window=14).mean()
        rs = gain / loss
        df['RSI'] = 100 - (100 / (1 + rs))
        
        # Moving Averages
        df['MA20'] = df['Close'].rolling(window=20).mean()
        df['MA50'] = df['Close'].rolling(window=50).mean()
        df['MA200'] = df['Close'].rolling(window=200).mean()
        
        return df
    
    def clean_data(self, df):
        """Clean and validate data
        
        Args:
            df (pd.DataFrame): Raw OHLC data
            
        Returns:
            pd.DataFrame: Cleaned data
        """
        # Remove NaN values
        df = df.dropna()
        
        # Ensure proper data types
        df['Open'] = pd.to_numeric(df['Open'])
        df['High'] = pd.to_numeric(df['High'])
        df['Low'] = pd.to_numeric(df['Low'])
        df['Close'] = pd.to_numeric(df['Close'])
        
        # Validate data integrity
        df = df[df['High'] >= df['Low']]
        df = df[df['High'] >= df['Open']]
        df = df[df['High'] >= df['Close']]
        df = df[df['Low'] <= df['Open']]
        df = df[df['Low'] <= df['Close']]
        
        return df
