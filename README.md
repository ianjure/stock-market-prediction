# Stock Market Trend Prediction &nbsp; [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ianjure/stock-market-trend-prediction/blob/main/Stock_Market_Trend_Prediction_Notebook.ipynb)
The **stock market** is known for its volatility, characterized by the buying and selling of stocks. This project aims to develop a machine learning model that predicts weekly and monthly trends for publicly traded stocks. The model will forecast whether stock prices will rise or fall in the upcoming week or month. To train various classification models and identify the most accurate one, we will use historical stock price and economic data. Following this, we will build a web application that allows users to test our model with up-to-date data.

## Data Overview
We will use the **[yfinance](https://pypi.org/project/yfinance/)** library to fetch historical stock price data from the **Yahoo Finance API**. This data includes columns such as closing and opening prices for publicly traded stocks. Additionally, we will retrieve economic data, such as interest rates, from **[FRED](https://fred.stlouisfed.org/docs/api/fred/#API)** to include as supplementary indicators in our dataset.

## Project Method
1. **Fetch the Data:** Collect stock price data from Yahoo Finance.
2. **Clean the Data:** Select relevant features and standardize the index format.
3. **Create New Features:** Derive useful features from the existing variables.
4. **Normalize the Data:** Scale the original variables to minimize dependency.
5. **Append New Features:** Integrate economic data from FRED as additional features.
6. **Build the Model:** Train various algorithms to identify the most effective one.
7. **Deploy the Model:** Develop a web application to allow users to test the model.

## Next Steps
* **Introduce** additional economic indicators to enhance data quality.
* **Tune** the best-performing model to improve accuracy.

<br>

**This project is inspired by:** [Predict The Stock Market With Machine Learning And Python](https://www.youtube.com/watch?v=1O_BenficgE)
