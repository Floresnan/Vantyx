import random


class MarketRadar:

    def investigar_cidade(self, cidade):

        preco_medio = random.randint(14000, 22000)

        novo_lancamento = random.randint(13000, 20000)

        oportunidade = preco_medio - novo_lancamento

        resultado = {
            "cidade": cidade,
            "preco_medio_m2": preco_medio,
            "novo_lancamento_m2": novo_lancamento,
            "potencial_valorizacao": oportunidade
        }

        return resultado
