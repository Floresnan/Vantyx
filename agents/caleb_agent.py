import pandas as pd

class CalebAgent:
    """
    Analisa anúncios capturados pelo Josue e gera insights.
    """

    def __init__(self):
        pass

    def analisar(self, dados_radar):
        arquivo = dados_radar.get('arquivo')
        if not arquivo:
            print("Dados de radar vazios.")
            return pd.DataFrame()

        try:
            df = pd.read_csv(arquivo)
        except FileNotFoundError:
            print("Arquivo de radar não encontrado:", arquivo)
            return pd.DataFrame()

        if 'titulo' not in df.columns:
            df['titulo'] = df.get('descricao', 'Sem título')

        df['insight'] = df['titulo'].apply(lambda x: f"O anúncio '{x}' tem bom potencial de engajamento")
        return df
