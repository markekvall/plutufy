
from dataclasses import dataclass
from typing import Dict
import pandas as pd

from plutufy.domain.models.roce import Roce

@dataclass
class StockStatement:
    roce: Dict[str, float] = None

    def calculate(self, df: pd.DataFrame) -> 'StockStatement':
        roce = Roce()
        roce.calculate(df=df)

        self._calculate_roce(df=df)

        return self
    
    def _calculate_roce(self, df: pd.DataFrame):
        self.roce = Dict()