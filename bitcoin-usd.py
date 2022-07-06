import yfinance as yf
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.dates import DateFormatter

BTC_USD = yf.download("BTC-USD", start='2020-01-01', end='2020-12-31', interval='1d')
BTC_USD.head()
