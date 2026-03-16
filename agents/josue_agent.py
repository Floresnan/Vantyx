import pandas as pd

class JosueAgent:
    """
    Agente Josue - Captura anúncios imobiliários para análise.
    """

    def __init__(self, cidades=None):
        if cidades is None:
            cidades = ["Florianopolis", "Porto Belo", "Balneario Camboriu", "Itapema"]
        self.cidades = cidades

    def buscar_ads_meta(self):
        """
        Simula a captura de anúncios do Meta Ads para as cidades do radar.
        Retorna um DataFrame de exemplo.
        """
        dados = []
        for cidade in self.cidades:
            # Simulação de anúncios
            for i in range(1, 4):
                dados.append({
                    "cidade": cidade,
                    "titulo": f"Anúncio {i} em {cidade}",
                    "descricao": f"Descrição do anúncio {i} em {cidade}",
                    "preco": 500000 + i * 10000,
                    "link": f"http://exemplo.com/{cidade}/anuncio{i}"
                })
        df = pd.DataFrame(dados)
        return df
