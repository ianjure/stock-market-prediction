import pandas as pd

def predict(train, test, predictors, model):
    model.fit(train[predictors], train["Target"])
    preds = model.predict_proba(test[predictors])[:,1]
    conf = preds.copy()
    conf = pd.Series(conf, index=test.index, name="Confidence")
    preds[preds >= .6] = 1
    preds[preds < .6] = 0
    preds = pd.Series(preds, index=test.index, name="Predictions")
    combined = pd.concat([test["Target"], preds], axis=1)
    combined = pd.concat([combined, conf], axis=1)
    return combined

def backtest(data, model, predictors, timeframe):
    all_predictions = []
    if timeframe == 'Week':
        for i in range(520, data.shape[0], 52):
            train = data.iloc[0:i].copy()
            test = data.iloc[i:(i+52)].copy()
            predictions = predict(train, test, predictors, model)
            all_predictions.append(predictions)
    else:
        for i in range(120, data.shape[0], 12):
            train = data.iloc[0:i].copy()
            test = data.iloc[i:(i+12)].copy()
            predictions = predict(train, test, predictors, model)
            all_predictions.append(predictions)
    combined = pd.concat(all_predictions)
    return combined