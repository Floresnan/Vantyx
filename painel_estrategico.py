import streamlit as st
from agents.josue_agent import JosueAgent
from agents.caleb_agent import CalebAgent
from agents.salomao_agent import SalomaoAgent
from agents.isaiah_agent import IsaiahAgent
from agents.mateus_agent import MateusAgent
import folium
from streamlit_folium import st_folium

# Inicialização dos agentes
josue = JosueAgent()
caleb = CalebAgent()
salomao = SalomaoAgent()
isaiah = IsaiahAgent()
mateus = MateusAgent()

st.set_page_config(page_title="VANTYX AI - Painel Estratégico", layout="wide")
st.title("🧠 VANTYX AI - Painel Estratégico")
st.subheader("Sistema de Inteligência Imobiliária")

# === Seção 1: Radar de Anúncios ===
st.write("## 📊 Radar de Anúncios Imobiliários")
if st.button("Investigar Mercado"):
    ads = josue.buscar_ads_meta()
    analise = caleb.analisar_ads(ads)
    st.write("### Resultado da análise de anúncios")
    st.write(analise)

# === Seção 2: Gerar Copy ===
st.write("## ✍️ Copy e Marketing")
if st.button("Gerar Copy de Anúncio"):
    copy = caleb.sugerir_copy()
    st.write("### Copy sugerida")
    st.write(copy)

# === Seção 3: Análise de Investimento ===
st.write("## 📈 Análise de Investimento")
if st.button("Analisar Oportunidade"):
    resultado = salomao.analisar_oportunidade(
        "Porto Belo",
        22000,
        15000
    )
    st.write("### Resultado da análise")
    st.write(resultado)

# === Seção 4: Previsão de Valorização ===
st.write("## 🔮 Previsão de Valorização")
if st.button("Rodar Profecia"):
    profecia = isaiah.analisar_regiao("Porto Belo", 14000, 8)
    tendencias = isaiah.detectar_tendencia()
    st.write("### Resultado da Profecia")
    st.write(profecia)
    st.write("### Tendências detectadas")
    st.write(tendencias)

# === Seção 5: Investidores Ideais ===
st.write("## 🎯 Investidores Ideais")
if st.button("Identificar Investidores"):
    investidores = mateus.identificar_investidores("Florianópolis")
    st.write("### Perfis encontrados")
    st.write(investidores)
    st.write("### Estratégia de abordagem")
    st.write(mateus.estrategia_abordagem())

# === Seção 6: Mapa de Oportunidades ===
st.write("## 🗺️ Radar de Oportunidades")
mapa = folium.Map(location=[-27.5954, -48.5480], zoom_start=10)
folium.Marker([-27.5954, -48.5480], popup="Centro Florianópolis", tooltip="Alta liquidez").add_to(mapa)
folium.Marker([-27.1086, -48.6167], popup="Porto Belo", tooltip="Forte valorização").add_to(mapa)
folium.Marker([-26.9926, -48.6358], popup="Balneário Camboriú", tooltip="Mercado de luxo consolidado").add_to(mapa)
st_folium(mapa, width=700)
