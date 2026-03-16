import pandas as pd

class MateusAgent:
    """
    Cria campanhas a partir de insights.
    """

    def __init__(self):
        pass

    def criar_campanha(self, df_insights):
        campanhas = []
        for idx, row in df_insights.iterrows():
            campanhas.append({
                "cidade": row.get("titulo", "Desconhecida"),
                "mensagem": f"Campanha destacando: {row.get('insight', '')}"
            })
        return campanhas
