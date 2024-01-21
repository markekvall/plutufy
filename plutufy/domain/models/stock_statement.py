
from dataclasses import dataclass, field
from typing import Dict, List
import pandas as pd

from plutufy.domain.models.roce import Roce

@dataclass
class StockStatement:
    stock_ticker: str
    financial_ratios: List[pd.DataFrame] = field(default_factory=list)

    def calculate(self, df: pd.DataFrame) -> 'StockStatement':

        self._calculate_roce(df=df)
        self._calculate_gross_margin(df=df)
        self._calculate_operating_profit_margin(df=df)
        self._calculate_cash_conversion(df=df)

        return self
    
    def _calculate_roce(self, df: pd.DataFrame):
        ebit = df.financials.loc['EBIT']
        total_assets = df.balance_sheet.loc['Total Assets']
        current_liabilities = df.balance_sheet.loc['Current Liabilities']
        roce = ebit/(total_assets - current_liabilities)
        roce.name = 'ROCE'
        self.financial_ratios.append(roce)

    def _calculate_gross_margin(self, df: pd.DataFrame):
        gross_profit = df.financials.loc['Gross Profit']
        total_revenue = df.financials.loc['Total Revenue']
        df.name = 'Gross Margin'
        gross_margin = gross_profit/total_revenue
        self.financial_ratios.append(gross_margin)

    def _calculate_operating_profit_margin(self, df: pd.DataFrame):
        ebit = df.financials.loc['EBIT']
        total_revenue = df.financials.loc['Total Revenue']
        df.name = 'Operating Profit Margin'
        operating_profit_margin = ebit/total_revenue
        self.financial_ratios.append(operating_profit_margin)

    def _calculate_cash_conversion(self, df: pd.DataFrame):
        operating_cash_flow = df.cash_flow.loc['Operating Cash Flow']
        ebitda = df.financials.loc['EBITDA']
        df.name = 'Cash Conversion'
        cash_conversion = operating_cash_flow/ebitda
        self.financial_ratios.append(cash_conversion)
        
