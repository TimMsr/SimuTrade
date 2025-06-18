import yfinance as yf
def __init__(self, startingCash=10000):
    self.cash = startingCash
    self.stocks = {}
    self.history = []

def buyStock(self, ticker, numberOfShares):
    price = getPrice(ticker)
    cost = price * numberOfShares
    if cost>self.cash:
        print("Not Enough Cash!")
    else:
        self.cash-=cost
        if ticker not in self.stocks:
            self.stocks[ticker]={"shares" : 0, "avgPrice" : 0}
        owned = self.stocks[ticker]
        totalShares = owned["shares"] + numberOfShares
        owned['avgPrice'] = owned['avgPrice'] + (cost/totalShares)
        owned['shares'] = totalShares
        self.history.append(f"User bought {numberOfShares} shares of {ticker} at ${price} each")

        




def getPrice(self, ticker):
    stock = yf.Ticker(ticker)
    return stock.history(period="1d")