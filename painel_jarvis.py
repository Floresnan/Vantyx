import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium

# Importação dos agentes
from agents.alfred_agent import AlfredAgent
from agents.josue_agent import JosueAgent
from agents.caleb_agent import CalebAgent
from agents.salomao_agent import SalomaoAgent
from agents.isaiah_agent import IsaiahAgent
from agents.mateus_agent import MateusAgent

st.set_page_config(page_title="Painel Jarvis", layout="wide")
st.title("🤖 Painel Estratégico Jarvis")

# === Pipeline de Leads ===
st.write("## 📋 Pipeline de Leads")

# Inicializa o Alfred
alfred = AlfredAgent("data/leads_a6.csv")
df_leads = alfred.processar_leads()
st.dataframe(df_leads)

# === Josue - Radar de anúncios ===
st.write("## 🔎 Josue - Investigando anúncios imobiliários")
josue = JosueAgent(["Porto Belo","Itapema","Balneario Camboriu","Florianopolis"])
resultado_radar = josue.buscar_ads_meta()
st.write(resultado_radar)

# === Caleb - Análise de anúncios ===
st.write("## 🧠 Caleb - Análise de anúncios")
caleb = CalebAgent()
resultado_caleb = caleb.analisar(resultado_radar)
st.dataframe(resultado_caleb)

# === Salomão - Identificação de oportunidades ===
st.write("## 📊 Salomão - Oportunidades")
salomao = SalomaoAgent()
oportunidades = salomao.analisar_oportunidades(df_leads)
st.dataframe(oportunidades)

# === Isaiah - Criação de copy persuasiva ===
st.write("## ✍️ Isaiah - Copy de marketing")
isaiah = IsaiahAgent()
mensagens = isaiah.gerar_copy(oportunidades)
st.dataframe(mensagens)

# === Mateus - Criação de campanhas ===
st.write("## 📣 Mateus - Criação de campanhas")
mateus = MateusAgent()
campanhas = mateus.criar_campanha(mensagens)
st.dataframe(campanhas)

# === Mapa interativo de oportunidades ===
st.write("## 🗺️ Mapa de Oportunidades")
mapa = folium.Map(location=[-27.5954, -48.5480], zoom_start=10)

# Lista de cidades com tooltip
cidades_tooltip = [
    (-27.5954, -48.5480, "Centro Florianópolis - Alta liquidez"),
    (-27.1086, -48.6167, "Porto Belo - Forte valorização"),
    (-26.9926, -48.6358, "Balneário Camboriú - Mercado de luxo consolidado"),
    (-27.0792, -48.6131, "Itapema - Crescimento acelerado")
]

for lat, lon, tooltip in cidades_tooltip:
    folium.Marker(location=[lat, lon], tooltip=tooltip).add_to(mapa)

st_folium(mapa, width=700, height=500)
