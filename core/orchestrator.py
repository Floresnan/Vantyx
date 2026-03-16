from agents.josue_agent import JosueAgent
from agents.caleb_agent import CalebAgent
from agents.salomao_agent import SalomaoAgent

from core.memory import VantyxMemory

from engine.sales_simulator import SalesSimulator
from radar.market_radar import MarketRadar
from brain.sales_brain import SalesBrain


class VantyxOrchestrator:

    def __init__(self):

        self.josue = JosueAgent()
        self.caleb = CalebAgent()
        self.salomao = SalomaoAgent()

        self.memory = VantyxMemory()

        self.simulator = SalesSimulator()
        self.radar = MarketRadar()
        self.brain = SalesBrain()


    def investigar_ads(self):

        ads = self.josue.buscar_ads_meta()

        analise = self.caleb.analisar_ads(ads)

        return analise


    def gerar_copy(self):

        return self.caleb.sugerir_copy()


    def analisar_investimento(self, cidade, preco, mercado):

        return self.salomao.analisar_oportunidade(
            cidade,
            preco,
            mercado
        )


    def simular_lancamento(self, unidades, ticket, investimento):

        return self.simulator.simular_lancamento(
            unidades,
            ticket,
            investimento
        )


    def radar_mercado(self, cidade):

        return self.radar.investigar_cidade(cidade)


    def estrategia_vendas(self, cidade, ticket, publico):

        return self.brain.gerar_estrategia(
            cidade,
            ticket,
            publico
        )
