from plutufy.application.business_logic.controller import Controller
from plutufy.data_access.yfinance_client import YFinanceClient
import yfinance as yf
import pandas as pd

def main():
    stock_ticker: str = "NIBE-B.ST"

    yf_client: YFinanceClient = YFinanceClient(stock_ticker)
    stock_df: pd.DataFrame = yf_client.get_ticker()
    #controller: Controller = Controller()
    #controller.process_data(stock_df=stock_df)
    ebit = stock_df.financials.loc['EBIT']
    total_assets = stock_df.balance_sheet.loc['Total Assets']
    current_liabilities = stock_df.balance_sheet.loc['Current Liabilities']

    print(ebit/(total_assets - current_liabilities))



if __name__ == "__main__":
    main()