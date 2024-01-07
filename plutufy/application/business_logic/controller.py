import pandas as pd

from plutufy.domain.models.stock_statement import StockStatement

class Controller:
    
    def process_data(self, stock_df) -> StockStatement:
        processed_data: StockStatement = StockStatement()
        return processed_data.calculate(stock_df=stock_df)

