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

def sellStock(self, ticker, numberOfShares):
    price = getPrice(ticker)
    value = price * numberOfShares
    owned = self.stocks[ticker]
    if numberOfShares > owned['shares']:
        print("Not enough shares to sell")
        return
    if ticker not in self.stocks:
        print("You dont own this stock")
        return
    else:
        self.cash+=value
        owned['shares']=owned['shares']-numberOfShares
        self.history.append(f"User sold {numberOfShares} shares of {ticker} at ${price} each")
        if owned['shares'] == 0:
            del self.stocks[ticker]

def portValue(self):
    value = self.cash
    for ticker, data in self.stocks.items():
        price = self.getPrice(ticker)
        shares = data['shares']
        value += price * shares
    return value

def show_portfolio(self):
        print(f"Cash: ${self.cash:.2f}")
        for ticker, data in self.stocks.items():
            print(f"{ticker}: {data['shares']} shares @ avg ${data['avg_price']:.2f}")
        print("----")


def getPrice(self, ticker):
    stock = yf.Ticker(ticker)
    return stock.history(period="1d")