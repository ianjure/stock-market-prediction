import yfinance as yf
import streamlit as st
from sklearn.linear_model import LogisticRegression
from preprocess import format_week, format_month
from backtest import backtest
from streamlit_extras.stylable_container import stylable_container

# PAGE CONFIGURATIONS
st.set_page_config(page_title="Stock Trend Forecaster", page_icon="🏛️", layout="centered", initial_sidebar_state="collapsed")

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
st.markdown("<p style='text-align: center; font-size: 6rem; line-height: 0;'>🕵️</p>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 3.4rem; font-weight: 800; line-height: 0.8; text-shadow: 0px -5px 10px #000000, 0px 0px 15px black,  0px 0px 5px black, 0px 0px 5px black;, 0px 0px 5px black;'>Stock Trend Forecaster</p>", unsafe_allow_html=True)

# SUBTITLE
st.markdown("<p style='text-align: center; font-size: 1rem; font-weight: 500; line-height: 1.2;'>Predicts market movements based on historical and economic data.</p>", unsafe_allow_html=True)

# SIDEBAR
with st.sidebar:
        with stylable_container(
                key = "dev_button",
                css_styles = """
                div[data-testid="stMarkdownContainer"] {
                        color: black;
                }
                """
                ):
                        st.link_button("**Developer:** Ian Jure Macalisang", "https://github.com/ianjure", type="primary", use_container_width=True)
        b1_col, b2_col = st.columns(2)
        with b1_col:
                repo_button = st.link_button("SOURCE CODE", "https://github.com/ianjure/stock-market-trend-forecast", use_container_width=True)
        with b2_col:
                notebook_button = st.link_button("NOTEBOOK", "https://colab.research.google.com/github/ianjure/stock-market-trend-forecast/blob/master/Stock_Market_Trend_Forecast_Notebook.ipynb", use_container_width=True)

# GET ALL TICKER SYMBOLS
text = open("stocks_clean.txt", "r")
all_stocks = text.read().split("|")
text.close()

# MAIN UI
with st.container(border=True):
    tickers = st.selectbox("SELECT A STOCK", all_stocks)
    timeframe = st.selectbox("CHOOSE A TIMEFRAME", ("Week", "Month"))
    col1, col2 = st.columns(2)

with col1:
    chart_btn = st.button("**SHOW INFO**", type="secondary", use_container_width=True)\
    
with col2:
        with stylable_container(
                key = "pred_button",
                css_styles = """
                button[data-testid="stBaseButton-primary"] {
                        color: black;
                }
                """
                ):
                        predict_btn = st.button("PREDICT TREND", type="primary", use_container_width=True)

info = False
if chart_btn:
    with st.spinner('Fetching stock information...'):
        ticker = tickers.split("-")[0].replace(" ", "")
        stock = yf.Ticker(ticker)
        stock_name = stock.info['shortName']
        try:
                stock_website = stock.info['website']
                stock_sector = stock.info['sector']
                stock_industry = stock.info['industry']
                info = True
        except:
                stock_volume = stock.info['volume']
                stock_category = stock.info['category']
                stock_price = stock.info['open']
                info = False
            
        stock = stock.history(period="max")

        with st.container(border=True):
                info_1, info_2 = st.columns(2)

        if info:     
                with info_1:
                    st.write(f"**Company Name:** {stock_name}")
                    st.write(f"**Website:** {stock_website}")
        
                with info_2:
                    st.write(f"**Sector:** {stock_sector}")
                    st.write(f"**Industry:** {stock_industry}")
        else:  
                with info_1:
                    st.write(f"**Company Name:** {stock_name}")
                    st.write(f"**Volume:** {stock_volume} Shares")
        
                with info_2:
                    st.write(f"**Category:** {stock_category}")
                    st.write(f"**Price:** ${stock_yield}")
                        
        st.dataframe(stock.tail(), use_container_width=True)
        st.line_chart(data=stock, x=None, y='Close', x_label='Years', y_label='Price', use_container_width=True)

if predict_btn:
    
    ticker = tickers.split("-")[0].replace(" ", "")
    stock = yf.Ticker(ticker)
    stock_name = stock.info['shortName']
    stock_ticker = stock.info['symbol']
    stock = stock.history(period="max")
    
    # CHECK IF THE STOCK IS PUBLICLY TRADED FOR MORE THAN 4 YEARS
    if stock.shape[0] < 1040:
        st.warning("**Insufficient Data:** The stock is not publicly traded for more than 4 years.")
    else:
        with st.spinner('Calculating the prediction...'):
            stock = format_week(stock) if timeframe == 'Week' else format_month(stock)

            if timeframe == 'Week':
                predictors = ['Close_Ratio_4', 'Trend_4', 'Close_Ratio_13', 'Trend_13', 'Close_Ratio_26', 'Trend_26', 'Close_Ratio_52', 'Trend_52', 'Close_Ratio_208', 'Trend_208', 'Crude Oil', 'Effective Rate', 'Interest Rate']
            else:
                predictors = ['Close_Ratio_2', 'Trend_2', 'Close_Ratio_6', 'Trend_6', 'Close_Ratio_12', 'Trend_12', 'Close_Ratio_30', 'Trend_30', 'Close_Ratio_60', 'Trend_60', 'Crude Oil', 'Effective Rate', 'Interest Rate']
            
            model = LogisticRegression(random_state=1)
            result = backtest(stock, model, predictors, timeframe)

            with st.container(border=True):
                if timeframe == 'Week':
                    if result['Predictions'][-1] > 0:
                        st.success(f"**{stock_name} ({stock_ticker})** stock price will go up next week.", icon="✔️")
                        st.info(f"**Confidence:** {round(result['Confidence'][-1] * 100)}%")
                    else:
                        st.error(f"**{stock_name} ({stock_ticker})** stock price will go down next week.", icon="🔻")
                        st.info(f"**Confidence:** {round((1 - result['Confidence'][-1]) * 100)}%")
                else:
                    if result['Predictions'][-1] > 0:
                        st.success(f"**{stock_name} ({stock_ticker})** stock price will go up next month.", icon="✔️")
                        st.info(f"**Confidence:** {round(result['Confidence'][-1] * 100)}%")
                    else:
                        st.error(f"**{stock_name} ({stock_ticker})** stock price will go down next month.", icon="🔻")
                        st.info(f"**Confidence:** {round((1 - result['Confidence'][-1]) * 100)}%")
