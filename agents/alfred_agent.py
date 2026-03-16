import pandas as pd

class AlfredAgent:
    """
    Gerencia a base de leads do projeto Vantyx.
    """

    def __init__(self, leads_path):
        self.leads_path = leads_path

    def processar_leads(self):
        try:
            df = pd.read_csv(self.leads_path)
        except FileNotFoundError:
            print("Arquivo de leads não encontrado:", self.leads_path)
            df = pd.DataFrame(columns=["nome", "cidade", "etapa", "interesse", "urgencia"])
        return df
