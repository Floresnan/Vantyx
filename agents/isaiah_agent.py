class IsaiahAgent:
    """
    Gera mensagens e copy para campanhas.
    """

    def __init__(self):
        pass

    def gerar_copy(self, df_oportunidades):
        if df_oportunidades.empty:
            return []
        mensagens = [
            f"🏖️ Viva ou invista em {row['titulo']} com grande potencial de valorização."
            for idx, row in df_oportunidades.iterrows()
        ]
        return mensagens
