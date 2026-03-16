class SalesBrain:

    def gerar_estrategia(
        self,
        cidade,
        ticket_medio,
        publico
    ):

        estrategia = {
            "cidade": cidade,
            "ticket_medio": ticket_medio,
            "publico": publico,
            "estrategia_marketing": [
                "Campanhas Meta focadas em investidores",
                "Vídeos curtos mostrando valorização da região",
                "Landing page com contagem regressiva de lançamento",
                "Convite para reunião de apresentação"
            ],
            "mensagem_principal":
            "Invista antes do lançamento e capture a valorização inicial do empreendimento."
        }

        return estrategia
