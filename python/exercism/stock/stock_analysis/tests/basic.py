import pytest
from src.analyzer import StockAnalyzer

def test_analyzer_initialization():
    analyzer = StockAnalyzer('AAPL')
    assert analyzer.symbol == 'AAPL'
    assert analyzer.data is None

def test_fetch_data():
    analyzer = StockAnalyzer('AAPL')
    data = analyzer.fetch_data('2024-01-01', '2024-01-31')
    assert not data.empty
    assert 'Close' in data.columns