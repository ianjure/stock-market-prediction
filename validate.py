import yfinance as yf

with open('stocks_raw.txt', 'r') as file:
    symbols_list = []
    for line in file:
        symbol = line.split("|")[0]
        symbols_list.append(symbol)

new_list = []
for ticker in symbols_list:
    stock = yf.Ticker(ticker)
    stock_hist = stock.history(period="max")
    if stock_hist.shape[0] > 1050:
        try:
            stock_website = stock.info['website']
            stock_sector = stock.info['sector']
            stock_industry = stock.info['industry']
            com_name = stock.info['shortName']
            com_name = com_name.replace("-", "").replace(".", "")
            new_list.append(f"{ticker} - {com_name}")
        except:
            continue

list_str = "|".join(new_list)

f = open("stocks_clean.txt", "x")
f.write(list_str)
f.close()