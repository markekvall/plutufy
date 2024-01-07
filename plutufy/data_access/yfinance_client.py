import yfinance as yf

class YFinanceClient:
    stock: yf.Ticker

    def __init__(self, stock_ticker: str,):
        print("retrieving financial data from", stock_ticker)
        self.stock = yf.Ticker(stock_ticker)


    def get_ticker(self) -> yf.ticker:
        return self.stock