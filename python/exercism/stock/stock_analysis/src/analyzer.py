from typing import Optional
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt

class StockAnalyzer:
    def __init__(self, symbol: str):
        self.symbol = symbol
        self.data: Optional[pd.DataFrame] = None
        
    def fetch_data(self, start_date: str, end_date: str) -> pd.DataFrame:
        """Fetch historical stock data"""
        self.data = yf.download(self.symbol, start=start_date, end=end_date)
        return self.data
    
    def calculate_indicators(self, short_window: int = 20, long_window: int = 50) -> None:
        """Calculate technical indicators"""
        if self.data is None:
            raise ValueError("No data available. Call fetch_data first.")
            
        self.data[f'SMA{short_window}'] = self.data['Close'].rolling(window=short_window).mean()
        self.data[f'SMA{long_window}'] = self.data['Close'].rolling(window=long_window).mean()
        
    def generate_signals(self) -> None:
        """Generate trading signals based on SMA crossover"""
        if self.data is None:
            raise ValueError("No data available. Call fetch_data first.")
            
        self.data['Signal'] = 0
        self.data.loc[self.data['SMA20'] > self.data['SMA50'], 'Signal'] = 1
        self.data['Position'] = self.data['Signal'].diff()
        
    def plot_analysis(self) -> None:
        """Plot the analysis with buy/sell signals"""
        if self.data is None:
            raise ValueError("No data available. Call fetch_data first.")
            
        plt.figure(figsize=(14,6))
        plt.plot(self.data['Close'], label='Close Price', alpha=0.5)
        plt.plot(self.data['SMA20'], label='SMA 20')
        plt.plot(self.data['SMA50'], label='SMA 50')
        
        plt.plot(self.data[self.data['Position'] == 1].index, 
                self.data['SMA20'][self.data['Position'] == 1], 
                '^', color='g', label='Buy Signal')
                
        plt.plot(self.data[self.data['Position'] == -1].index, 
                self.data['SMA20'][self.data['Position'] == -1], 
                'v', color='r', label='Sell Signal')
                
        plt.legend()
        plt.title(f"SMA Crossover Strategy on {self.symbol}")
        plt.show()