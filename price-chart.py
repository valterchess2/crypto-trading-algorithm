import yfinance as yf
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.dates import DateFormatter

BTC_USD = yf.download("BTC-USD", start='2022-01-01', end='2022-12-31', interval='1d')

BTC_USD.head()

fig, ax = plt.subplots(dpi=200)

# Formatting the date axis
date_format = DateFormatter("%h-%d-%y")
ax.xaxis.set_major_formatter(date_format)
ax.tick_params(axis='x', labelsize=9)
fig.autofmt_xdate()

# Plotting the closing price against the date (1 - day interval)
ax.plot(BTC_USD['Close'], lw=0.75)

# Adding labels and title to the plot
ax.set_ylabel('Price of Bitcoin (USD)')
ax.set_title('Bitcoin to USD Exchange Rate')
ax.grid()  # adding a grid

# Displaying the price chart
plt.show()
