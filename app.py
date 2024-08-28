import yfinance as yf
import streamlit as st
from sklearn.linear_model import LogisticRegression
from preprocess import format_week, format_month
from backtest import backtest

# PAGE CONFIGURATIONS
st.set_page_config(page_title="Stock Trend Predictor", page_icon="📊", layout="centered", initial_sidebar_state="collapsed")

top = """
        <style>
        .block-container {
                padding-top: 5rem;
                padding-bottom: 5rem;
                margin-top: 0rem;
        }
        </style>
        """
st.markdown(top, unsafe_allow_html=True)

hide = """
        <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        </style>
        """
st.markdown(hide, unsafe_allow_html=True)

# TITLE
st.markdown("<h1 style='text-align: center; color: white;'>Stock Trend Predictor</h1>", unsafe_allow_html=True)

# SIDEBAR
with st.sidebar:
        st.info("Creator: Ian Jure Macalisang")
        b1_col, b2_col = st.columns(2)
        with b1_col:
                repo_button = st.link_button("SOURCE CODE", "https://github.com/ianjure/stock-market-trend-prediction", use_container_width=True)
        with b2_col:
                notebook_button = st.link_button("NOTEBOOK", "https://colab.research.google.com/github/ianjure/stock-market-trend-prediction/blob/master/Stock_Market_Trend_Prediction_Notebook.ipynb", use_container_width=True)

# MAIN UI
stocks = ('GOOG', 'AAPL', 'MSFT', 'ALAB','BTC-USD')
ticker = st.selectbox("SELECT A STOCK", stocks)
timeframe = st.selectbox("PREDICTION TIMEFRAME", ("Week", "Month"))
col1, col2 = st.columns(2)
with col1:
    chart_btn = st.button("SHOW INFO", type="secondary", use_container_width=True)
with col2:
    predict_btn = st.button("PREDICT TREND", type="primary", use_container_width=True)

if chart_btn:

    # FETCH DATA
    stock = yf.Ticker(ticker)
    stock_name = stock.info['longName']
    stock_ticker = stock.info['symbol']
    stock = stock.history(period="max")

    # CHECK IF THE STOCK IS PUBLICLY TRADED FOR MORE THAN 2 YEARS
    if stock.shape[0] < 520:
        with st.spinner('Fetching stock information...'):
            st.dataframe(stock.tail(), use_container_width=True)
    else:
        with st.spinner('Fetching stock information...'):
            stock = format_week(stock) if timeframe == 'Week' else format_month(stock)
            st.dataframe(stock.tail(), use_container_width=True)
            st.line_chart(data=stock, x=None, y=['Close','Interest Rate', 'Effective Rate', 'Crude Oil'], x_label='Years', y_label='Price', use_container_width=True)

if predict_btn:
    
    # FETCH DATA
    stock = yf.Ticker(ticker)
    stock_name = stock.info['longName']
    stock_ticker = stock.info['symbol']
    stock = stock.history(period="max")

    # CHECK IF THE STOCK IS PUBLICLY TRADED FOR MORE THAN 2 YEARS
    if stock.shape[0] < 520:
        st.warning("**Insufficient Data Error:** The stock is not publicly traded for more than 2 years.")
    else:
        with st.spinner('Calculating the prediction...'):
            stock = format_week(stock) if timeframe == 'Week' else format_month(stock)

            if timeframe == 'Week':
                predictors = ['Close_Ratio_4', 'Trend_4', 'Close_Ratio_13', 'Trend_13', 'Close_Ratio_26', 'Trend_26', 'Close_Ratio_52', 'Trend_52', 'Close_Ratio_208', 'Trend_208', 'Crude Oil', 'Effective Rate', 'Interest Rate']
            else:
                predictors = ['Close_Ratio_2', 'Trend_2', 'Close_Ratio_6', 'Trend_6', 'Close_Ratio_12', 'Trend_12', 'Close_Ratio_30', 'Trend_30', 'Close_Ratio_60', 'Trend_60', 'Crude Oil', 'Effective Rate', 'Interest Rate']
            
            model = LogisticRegression(random_state=1)
            result = backtest(stock, model, predictors, timeframe)

            if timeframe == 'Week':
                if result['Predictions'][-1] > 0:
                    st.success(f"**{stock_name} ({stock_ticker})** stock price will go up next week.", icon="📈")
                    st.info(f"**Confidence:** {round(result['Confidence'][-1] * 100)}%")
                else:
                    st.error(f"**{stock_name} ({stock_ticker})** stock price will go down next week.", icon="📉")
                    st.info(f"**Confidence:** {round((1 - result['Confidence'][-1]) * 100)}%")
            else:
                if result['Predictions'][-1] > 0:
                    st.success(f"**{stock_name} ({stock_ticker})** stock price will go up next month.", icon="📈")
                    st.info(f"**Confidence:** {round(result['Confidence'][-1] * 100)}%")
                else:
                    st.error(f"**{stock_name} ({stock_ticker})** stock price will go down next month.", icon="📉")
                    st.info(f"**Confidence:** {round((1 - result['Confidence'][-1]) * 100)}%")