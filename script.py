from portfolio.portfolio import Portfolio, getPrice

portfolio = Portfolio()

ticker = "AAPL"
price = getPrice(ticker)
portfolio.buyStock(ticker, price, 10)

price = getPrice(ticker)
portfolio.sellStock(ticker, price, 5)

portfolio.showPortfolio()