import pandas as pd
import streamlit as st
from fredapi import Fred

API_KEY = st.secrets['API_KEY_FRED']
fred = Fred(api_key=API_KEY)

def format_week(stock):

    # CLEANING
    del stock["Dividends"]
    del stock["Stock Splits"]
    stock.index = stock.index.strftime('%Y-%m-%d')
    stock.index = pd.to_datetime(stock.index)
    stock_date = pd.date_range(start="1990-01-01", end=stock.index[-1].tz_localize(None), freq="W-FRI")
    stock = stock.reindex(stock_date, method="ffill")

    # FEATURE ENGINEERING
    stock["Next Week"] = stock["Close"].shift(-1)
    stock["Target"] = (stock["Next Week"] > stock["Close"]).astype(int)

    horizons = [4,13,26,52,208]

    for horizon in horizons:
      rolling_averages = stock.rolling(horizon).mean()

      ratio_column = f"Close_Ratio_{horizon}"
      stock[ratio_column] = stock["Close"] / rolling_averages["Close"]

      trend_column = f"Trend_{horizon}"
      stock[trend_column] = stock.shift(1).rolling(horizon).sum()["Target"]

    stock = stock.dropna(subset=['Close_Ratio_4', 'Trend_4', 'Close_Ratio_13', 'Trend_13', 'Close_Ratio_26', 'Trend_26', 'Close_Ratio_52', 'Trend_52', 'Close_Ratio_208', 'Trend_208'])

    # ADDING FEATURES
    crude_oil = fred.get_series('DCOILWTICO').rename('Price')
    crude_oil = crude_oil.reindex_like(stock)
    stock['Crude Oil'] = crude_oil
    stock['Crude Oil'] = crude_oil.ffill()
    stock = stock.dropna(subset=['Crude Oil'])

    effective_rate = fred.get_series('DFF').rename('Rate')
    effective_rate = effective_rate.reindex_like(stock)
    stock['Effective Rate'] = effective_rate
    stock['Effective Rate'] = effective_rate.ffill()

    interest_rate = fred.get_series('T10Y3M').rename('Rate')
    interest_rate = interest_rate.reindex_like(stock)
    stock['Interest Rate'] = interest_rate
    stock['Interest Rate'] = interest_rate.ffill()

    return stock

def format_month(stock):

    # CLEANING
    del stock["Dividends"]
    del stock["Stock Splits"]
    stock.index = stock.index.strftime('%Y-%m-%d')
    stock.index = pd.to_datetime(stock.index)
    stock_date = pd.date_range(start="1990-01-01", end=stock.index[-1].tz_localize(None), freq="M")
    stock = stock.reindex(stock_date, method="ffill")
    stock["Next Month"] = stock["Close"].shift(-1)
    stock["Target"] = (stock["Next Month"] > stock["Close"]).astype(int)

    # FEATURE ENGINEERING
    horizons = [2,6,12,30,60]

    for horizon in horizons:
      rolling_averages = stock.rolling(horizon).mean()

      ratio_column = f"Close_Ratio_{horizon}"
      stock[ratio_column] = stock["Close"] / rolling_averages["Close"]

      trend_column = f"Trend_{horizon}"
      stock[trend_column] = stock.shift(1).rolling(horizon).sum()["Target"]

    stock = stock.dropna(subset=['Close_Ratio_2', 'Trend_2', 'Close_Ratio_6', 'Trend_6', 'Close_Ratio_12', 'Trend_12', 'Close_Ratio_30', 'Trend_30', 'Close_Ratio_60', 'Trend_60'])

    # ADDING FEATURES
    crude_oil = fred.get_series('DCOILWTICO').rename('Price')
    crude_oil = crude_oil.reindex_like(stock)
    stock['Crude Oil'] = crude_oil
    stock['Crude Oil'] = crude_oil.ffill()
    stock = stock.dropna(subset=['Crude Oil'])

    effective_rate = fred.get_series('DFF').rename('Rate')
    effective_rate = effective_rate.reindex_like(stock)
    stock['Effective Rate'] = effective_rate
    stock['Effective Rate'] = effective_rate.ffill()

    interest_rate = fred.get_series('T10Y3M').rename('Rate')
    interest_rate = interest_rate.reindex_like(stock)
    stock['Interest Rate'] = interest_rate
    stock['Interest Rate'] = interest_rate.ffill()

    return stock
