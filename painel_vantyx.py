import streamlit as st
import folium
from streamlit_folium import st_folium

from agents.josue_agent import JosueAgent
from agents.caleb_agent import CalebAgent
from agents.salomao_agent import SalomaoAgent


josue = JosueAgent()
caleb = CalebAgent()
salomao = SalomaoAgent()


st.title("🧠 VANTYX AI")
st.subheader("Sistema de Inteligência Imobiliária")


if st.button("Investigar Mercado"):

    
    ads = josue.buscar_ads_meta()
    analise = caleb.analisar(ads)
    
    st.write("### 📊 Análise de anúncios")
    st.write(analise)


if st.button("Gerar Copy de Anúncio"):

    copy = caleb.sugerir_copy()

    st.write("### ✍️ Copy sugerida")
    st.write(copy)


if st.button("Analisar Oportunidade"):

    resultado = salomao.analisar_oportunidade(
        "Porto Belo",
        22000,
        15000
    )
if st.button("🛰️ Radar de Mercado"):

    radar = vantyx.investigar_oportunidade("Porto Belo")

    st.write("### Oportunidade detectada")
    st.write(radar)
    st.write("### 📈 Análise de investimento")
    st.write(resultado)
if st.button("🧠 Estratégia de Vendas"):

    estrategia = vantyx.gerar_estrategia_vendas(
        "Porto Belo",
        850000,
        "Investidores"
    )

    st.write("### Estratégia sugerida")
    st.write(estrategia)

st.write("## 🗺️ Radar de Oportunidades")

mapa = folium.Map(location=[-27.5954, -48.5480], zoom_start=10)

folium.Marker(
    [-27.5954, -48.5480],
    popup="Centro Florianópolis",
    tooltip="Alta liquidez"
).add_to(mapa)

folium.Marker(
    [-27.1086, -48.6167],
    popup="Porto Belo",
    tooltip="Forte valorização"
).add_to(mapa)

folium.Marker(
    [-26.9926, -48.6358],
    popup="Balneário Camboriú",
    tooltip="Mercado de luxo consolidado"
).add_to(mapa)

st_folium(mapa, width=700)
