import yfinance as yf
import pandas as pd
from preprocess import format_week, format_month
from backtest import predict, backtest

# FETCH DATA
stock = yf.Ticker(ticker)
stock_name = stock.info['longName']
stock_ticker = stock.info['symbol']
stock = stock.history(period="max")

# CHECK IF THE STOCK IS PUBLICLY TRADED FOR MORE THAN 2 YEARS
if stock.shape[0] < 520:
  st.error("The stock is not publicly traded for more than 2 years.")
else:
  
