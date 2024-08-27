# Stock Market Trend Prediction &nbsp; [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ianjure/stock-market-trend-prediction/blob/main/Stock_Market_Trend_Prediction_Notebook.ipynb)
The **stock market** is a volatile market where people buy and sell stocks. The goal of this project is to create a machine learning model to predict a weekly and monthly trend for a publicly traded stock. The model will forecast whether the stock price will go up or down by next week and next month. We will utilize historical stock price data in order to train a number of classification models and find the most accurate one. After that, we will create a web application that anyone can use to test our model with up-to-date stock price data.

## Data Overview
We will be using the [yfinance](https://pypi.org/project/yfinance/) library to fetch historical stock price data from the [Yahoo Finance](https://finance.yahoo.com/) API. These data contains columns such as the closing and opening prices of any publicly traded stocks. We will also retrieve economic data from [FRED](https://fred.stlouisfed.org/docs/api/fred/#API) that we can add to our dataset as additional indicators.

## Project Method
1. **Fetch the Data:** Collect the data from Yahoo Finance.
2. **Clean the Data:** Select relevant features and fix the index format.
3. **Create new Features:** Make useful features from the existing variables.
4. **Normalize the Data:** Scale original variables to reduce dependency.
5. **Append new Features:** Add economic data from FRED as new features.
6. **Build the Model:** Train and find the best algorithm.
7. **Deploy the Model:** Build a web application to test the model.

## Next Steps
1. Introduce more **economic indicators** to improve data quality.
2. Try **tuning** the best model to see improvements in accuracy.

<br>

**This project is inspired by:** [Predict The Stock Market With Machine Learning And Python](https://www.youtube.com/watch?v=1O_BenficgE)
