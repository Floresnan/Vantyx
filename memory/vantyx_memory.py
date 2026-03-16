import json
import os


class VantyxMemory:

    def __init__(self):

        self.file_path = "memory/memory.json"

        if not os.path.exists(self.file_path):
            with open(self.file_path, "w") as f:
                json.dump({
                    "ads_analisados": [],
                    "copies_geradas": [],
                    "oportunidades": []
                }, f)


    def carregar_memoria(self):

        with open(self.file_path, "r") as f:
            return json.load(f)


    def salvar_memoria(self, dados):

        with open(self.file_path, "w") as f:
            json.dump(dados, f, indent=4)


    def salvar_ads(self, ads):

        dados = self.carregar_memoria()
        dados["ads_analisados"].append(ads)
        self.salvar_memoria(dados)


    def salvar_copy(self, copy):

        dados = self.carregar_memoria()
        dados["copies_geradas"].append(copy)
        self.salvar_memoria(dados)


    def salvar_oportunidade(self, oportunidade):

        dados = self.carregar_memoria()
        dados["oportunidades"].append(oportunidade)
        self.salvar_memoria(dados)

