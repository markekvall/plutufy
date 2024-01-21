from plutufy.application.business_logic.controller import Controller
from plutufy.data_access.yfinance_client import YFinanceClient
from flask import Flask, render_template, jsonify
from plutufy.domain.models.stock_statement import StockStatement
import yfinance as yf
import pandas as pd

app = Flask(__name__, template_folder=".")

@app.route('/api/calculated-data')
def api_calculated_data():
    calculated_data = {'labels': ['A', 'B', 'C', 'D', 'E'],
                    'values': [30, 45, 12, 60, 25]}
    
    stock_ticker: str = "AAPL"

    yf_client: YFinanceClient = YFinanceClient(stock_ticker)
    stock_df: pd.DataFrame = yf_client.get_ticker()
    controller: Controller = Controller()
    stock_statement: str = controller.process_data(stock_df=stock_df, stock_ticker=stock_ticker)
    print(stock_statement.get_data(as_text=True))

    #return jsonify(calculated_data)
    return stock_statement.get_data(as_text=True)

@app.route('/')
def main_route():


    return render_template('index2.html')



if __name__ == "__main__":
    app.run(debug=True)