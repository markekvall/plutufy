import pandas as pd
from flask import jsonify

from plutufy.domain.models.stock_statement import StockStatement

class Controller:

    def process_data(self, stock_df, stock_ticker) -> str:
        #create calculator class that builds stock statement
        stock_statement: StockStatement = StockStatement(stock_ticker=stock_ticker)
        stock_statement: StockStatement = stock_statement.calculate(df=stock_df)
         
        return self._statement_to_json(stock_statement)
    

    def _statement_to_json(self, stock_statement: StockStatement) -> str:
        stock_statement_dict = {
            'stock_ticker': stock_statement.stock_ticker,
            'financial_ratios': [df.to_json(orient='split', date_format='iso') for df in stock_statement.financial_ratios],
        }
        print(stock_statement_dict)
        return jsonify(stock_statement_dict)

