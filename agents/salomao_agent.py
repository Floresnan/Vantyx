import pandas as pd

class SalomaoAgent:
    """
    Analisa oportunidades de imóveis.
    """

    def __init__(self):
        pass

    def analisar_oportunidades(self, df):
        if df.empty:
            return pd.DataFrame()
        df['classificacao'] = 'OPORTUNIDADE RARA'
        return df
