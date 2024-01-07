from dataclasses import dataclass
import pandas as pd
from typing import Dict

@dataclass
class Roce:
    roce: Dict[str, float] = None

    def calculate(self, df: pd.DataFrame) -> 'Roce':
        ebit = df.financials['EBIT']
        print(ebit)

        return self