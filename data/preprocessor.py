"""Data preprocessing module"""

import pandas as pd
import numpy as np


class DataPreprocessor:
    """Preprocess OHLC data for analysis"""
    
    @staticmethod
    def normalize_data(df):
        """Normalize prices for consistent analysis
        
        Args:
            df (pd.DataFrame): OHLC data
            
        Returns:
            pd.DataFrame: Normalized data
        """
        df_norm = df.copy()
        
        for col in ['Open', 'High', 'Low', 'Close']:
            max_val = df_norm[col].max()
            min_val = df_norm[col].min()
            df_norm[col] = (df_norm[col] - min_val) / (max_val - min_val)
        
        return df_norm
    
    @staticmethod
    def calculate_pip_value(close_price, decimal_places=4):
        """Calculate pip value for currency pair
        
        Args:
            close_price (float): Current close price
            decimal_places (int): Decimal places for pair
            
        Returns:
            float: Pip value
        """
        return 1 / (10 ** decimal_places)
    
    @staticmethod
    def convert_to_pips(price_diff, pip_value=0.0001):
        """Convert price difference to pips
        
        Args:
            price_diff (float): Price difference
            pip_value (float): Pip value
            
        Returns:
            int: Number of pips
        """
        return round(price_diff / pip_value)
    
    @staticmethod
    def add_swing_highs_lows(df, window=5):
        """Identify swing highs and swing lows
        
        Args:
            df (pd.DataFrame): OHLC data
            window (int): Lookback window
            
        Returns:
            pd.DataFrame: Data with swing highs/lows
        """
        df['Swing_High'] = df['High'].rolling(window=window, center=True).max()
        df['Swing_Low'] = df['Low'].rolling(window=window, center=True).min()
        
        # Identify actual swing points
        df['Is_Swing_High'] = df['High'] == df['Swing_High']
        df['Is_Swing_Low'] = df['Low'] == df['Swing_Low']
        
        return df
    
    @staticmethod
    def identify_higher_highs_lows(df, min_bars=3):
        """Identify higher highs and higher lows (uptrend) or lower highs and lower lows (downtrend)
        
        Args:
            df (pd.DataFrame): OHLC data with swing points
            min_bars (int): Minimum bars for pattern
            
        Returns:
            dict: Higher highs, higher lows, lower highs, lower lows lists
        """
        swing_highs = df[df['Is_Swing_High']].index.tolist()
        swing_lows = df[df['Is_Swing_Low']].index.tolist()
        
        higher_highs = []
        higher_lows = []
        lower_highs = []
        lower_lows = []
        
        # Check for higher highs
        for i in range(1, len(swing_highs)):
            if df.loc[swing_highs[i], 'High'] > df.loc[swing_highs[i-1], 'High']:
                higher_highs.append(swing_highs[i])
        
        # Check for higher lows
        for i in range(1, len(swing_lows)):
            if df.loc[swing_lows[i], 'Low'] > df.loc[swing_lows[i-1], 'Low']:
                higher_lows.append(swing_lows[i])
        
        # Check for lower highs
        for i in range(1, len(swing_highs)):
            if df.loc[swing_highs[i], 'High'] < df.loc[swing_highs[i-1], 'High']:
                lower_highs.append(swing_highs[i])
        
        # Check for lower lows
        for i in range(1, len(swing_lows)):
            if df.loc[swing_lows[i], 'Low'] < df.loc[swing_lows[i-1], 'Low']:
                lower_lows.append(swing_lows[i])
        
        return {
            'higher_highs': higher_highs,
            'higher_lows': higher_lows,
            'lower_highs': lower_highs,
            'lower_lows': lower_lows
        }
