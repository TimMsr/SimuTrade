import yfinance as yf

#testing 
def getPrice(ticker):
    stock = yf.Ticker(ticker)
    return stock.history(period="1d")
    
print(getPrice("MSFT"))