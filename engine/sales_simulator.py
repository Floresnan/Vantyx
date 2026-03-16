class SalesSimulator:

    def simular_lancamento(
        self,
        unidades,
        ticket_medio,
        investimento_marketing,
        taxa_conversao=0.02
    ):

        leads_necessarios = int(unidades / taxa_conversao)

        custo_por_lead = investimento_marketing / leads_necessarios

        faturamento_total = unidades * ticket_medio

        roi = faturamento_total / investimento_marketing

        meses_venda = unidades / 10

        resultado = {
            "unidades": unidades,
            "ticket_medio": ticket_medio,
            "faturamento_total": faturamento_total,
            "leads_necessarios": leads_necessarios,
            "custo_por_lead": round(custo_por_lead, 2),
            "roi_marketing": round(roi, 2),
            "meses_estimados_venda": round(meses_venda, 1)
        }

        return resultado
