import yfinance as yf

with open('stocks_raw.txt', 'r') as file:
    symbols_list = []
    for line in file:
        symbol = line.split("|")[0]
        symbols_list.append(symbol)

new_list = []
for ticker in symbols_list:
    try:
        com_name = yf.Ticker(ticker).info['shortName']
        new_list.append(f"{ticker} - {com_name}")
    except:
        continue

list_str = "|".join(new_list)

f = open("stocks_clean.txt", "x")
f.write(list_str)
f.close()