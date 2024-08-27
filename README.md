# Stock Market Trend Prediction &nbsp; [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ianjure/titanic-survivor-prediction/blob/master/Titanic_Survivor_Prediction_Notebook.ipynb)
Let's go back to 1912 and explore the data behind the **Titanic** tragedy. The goal of this project is to create a machine learning model to predict if a passenger will survive the incident. We will utilize classification algorithms and processed data to find the best model. After that, we will create a web application that anyone can use to try and test our model with new data inputs.

## Data Overview
We will be using the [yfinance](https://pypi.org/project/yfinance/) python library to fetch historical stock price data from the [Yahoo Finance](https://finance.yahoo.com/) API. These data contains columns such as the closing and opening prices of any publicly traded stocks.

## Project Method
1. **Fetch the Data:** Collect the data from Yahoo Finance.
2. **Clean the Data:** Select relevant features and fix the index format.
3. **Create new Features:** Make useful features from the existing variables.
4. **Normalize the Data:** Scale original variables to reduce dependency.
5. **Append new Features:** Add economic data as new features.
6. **Build the Model:** Train and find the best algorithm.
7. **Deploy the Model:** Build a web application to test the model.

## Next Steps
1. Introduce more **economic indicators** to improve data quality.
2. Try **tuning** the best model to see improvements in accuracy.

<br>

**This project is inspired by:** [Predict The Stock Market With Machine Learning And Python](https://www.youtube.com/watch?v=1O_BenficgE)
