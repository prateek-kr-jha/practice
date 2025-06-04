import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt

# Fetch data
data = yf.download('RELIANCE.NS', start='2023-01-01', end='2024-01-01')
data['SMA20'] = data['Close'].rolling(window=20).mean()
data['SMA50'] = data['Close'].rolling(window=50).mean()

# Generate signals
data['Signal'] = 0
data['Signal'][20:] = data['SMA20'][20:] > data['SMA50'][20:]
data['Position'] = data['Signal'].diff()

# Plot
plt.figure(figsize=(14,6))
plt.plot(data['Close'], label='Close Price', alpha=0.5)
plt.plot(data['SMA20'], label='SMA 20')
plt.plot(data['SMA50'], label='SMA 50')
plt.plot(data[data['Position'] == 1].index, data['SMA20'][data['Position'] == 1], '^', color='g', label='Buy Signal')
plt.plot(data[data['Position'] == -1].index, data['SMA20'][data['Position'] == -1], 'v', color='r', label='Sell Signal')
plt.legend()
plt.title("SMA Crossover Strategy on RELIANCE.NS")
plt.show()

