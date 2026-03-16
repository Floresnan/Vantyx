import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium

from agents.alfred_agent import AlfredAgent
from agents.josue_agent import JosueAgent
from agents.caleb_agent import CalebAgent
from agents.salomao_agent import SalomaoAgent
from agents.isaiah_agent import IsaiahAgent
from agents.mateus_agent import MateusAgent

st.title("📊 Painel Estratégico Jarvis")

# Inicialização dos agentes
alfred = AlfredAgent("data/leads_a6.csv")
josue = JosueAgent(["Porto Belo", "Itapema", "Balneario Camboriu", "Florianopolis"])
caleb = CalebAgent()
salomao = SalomaoAgent()
isaiah = IsaiahAgent()
mateus = MateusAgent()

# Pipeline de Leads
st.write("## 📋 Pipeline de Leads")
df_leads = alfred.processar_leads()
st.dataframe(df_leads)

# Radar Josue
st.write("## 🔎 Radar de anúncios")
resultado_radar = josue.executar_radar()
st.write(resultado_radar)

# Análise Caleb
st.write("## 🧠 Análise Caleb")
resultado_caleb = caleb.analisar(resultado_radar)
st.dataframe(resultado_caleb)

# Oportunidades Salomão
st.write("## 📊 Oportunidades")
oportunidades = salomao.analisar_oportunidades(resultado_caleb)
st.dataframe(oportunidades)

# Mensagens Isaiah
st.write("## ✍️ Mensagens")
mensagens = isaiah.gerar_copy(oportunidades)
st.write(mensagens)

# Campanhas Mateus
st.write("## 📢 Campanhas")
campanhas = mateus.criar_campanha(oportunidades)
st.dataframe(pd.DataFrame(campanhas))

# Mapa interativo
st.write("## 🗺️ Mapa de Oportunidades")
mapa = folium.Map(location=[-27.5954, -48.5480], zoom_start=10)
for lat, lon, tooltip in [
    (-27.5954, -48.5480, "Centro Florianópolis - Alta liquidez"),
    (-27.1086, -48.6167, "Porto Belo - Forte valorização"),
    (-26.9926, -48.6358, "Balneário Camboriú - Mercado de luxo consolidado"),
    (-27.452, -48.489, "Itapema - Área promissora")
]:
    folium.Marker([lat, lon], tooltip=tooltip).add_to(mapa)
st_folium(mapa, width=700)
