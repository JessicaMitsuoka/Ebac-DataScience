import streamlit as st
import pandas as pd
import os
from pycaret.classification import load_model, predict_model
import plotly.express as px

st.set_page_config(page_title="Credit Scoring", page_icon="💳", layout="wide")

st.markdown("<h1 style='text-align: center; color: white;'>💳 Credit Scoring - Projeto Final</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Faça o upload de um arquivo CSV para realizar a escoragem dos clientes com modelo LightGBM.</p>", unsafe_allow_html=True)
st.markdown("---")

uploaded_file = st.file_uploader("📂 Upload do arquivo CSV", type=["csv"])

if uploaded_file is not None:

    df_novo = pd.read_csv(uploaded_file)
    st.success(f"✅ Arquivo carregado com {df_novo.shape[0]} linhas e {df_novo.shape[1]} colunas.")

    with st.sidebar:
        st.header("🔍 Filtros")

        idade_min, idade_max = st.slider("Idade", 18, 100, (18, 100))
        renda_min, renda_max = st.slider("Renda", float(df_novo['renda'].min()), float(df_novo['renda'].max()), (float(df_novo['renda'].min()), float(df_novo['renda'].max())))

        tipo_renda = st.multiselect("Tipo de Renda", options=df_novo['tipo_renda'].unique(), default=list(df_novo['tipo_renda'].unique()))
        educacao = st.multiselect("Educação", options=df_novo['educacao'].unique(), default=list(df_novo['educacao'].unique()))
        estado_civil = st.multiselect("Estado Civil", options=df_novo['estado_civil'].unique(), default=list(df_novo['estado_civil'].unique()))
        filhos = st.slider("Quantidade de Filhos", 0, int(df_novo['qtd_filhos'].max()), (0, int(df_novo['qtd_filhos'].max())))

        veiculo = st.radio("Possui veículo?", ["S", "N"])
        imovel = st.radio("Possui imóvel?", ["S", "N"])

    df_filtrado = df_novo[
        (df_novo['idade'] >= idade_min) &
        (df_novo['idade'] <= idade_max) &
        (df_novo['renda'] >= renda_min) &
        (df_novo['renda'] <= renda_max) &
        (df_novo['tipo_renda'].isin(tipo_renda)) &
        (df_novo['educacao'].isin(educacao)) &
        (df_novo['estado_civil'].isin(estado_civil)) &
        (df_novo['qtd_filhos'] >= filhos[0]) &
        (df_novo['qtd_filhos'] <= filhos[1]) &
        (df_novo['posse_de_veiculo'] == veiculo) &
        (df_novo['posse_de_imovel'] == imovel)
    ]

    with st.expander("Visualizar dados filtrados"):
        st.dataframe(df_filtrado.head())

    if not os.path.exists("Final_LGBM_Model_13jul2025.pkl"):
        st.error("❌ Modelo não encontrado! Certifique-se de que o arquivo 'Final_LGBM_Model_13jul2025.pkl' esteja na mesma pasta do app.")
    else:
 
        modelo = load_model("Final_LGBM_Model_13jul2025")

        resultado = predict_model(modelo, data=df_filtrado)

        st.markdown("---")
        st.subheader("Resultado da Escoragem")
        st.dataframe(resultado[['prediction_label', 'prediction_score']])

        st.markdown("### 📊 Distribuição das Previsões")
        fig = px.histogram(resultado, x='prediction_score', color='prediction_label', nbins=50, title="Distribuição da Escoragem")
        st.plotly_chart(fig, use_container_width=True)

        csv_result = resultado.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="📁 Baixar resultado como CSV",
            data=csv_result,
            file_name='resultado_escoragem.csv',
            mime='text/csv'
        )
else:
    st.info("📥 Envie um arquivo CSV para continuar.")

st.markdown("---")
st.markdown(
    "<p style='text-align: center; font-size: 12px;'>Desenvolvido por Jessica Mitsuoka • Projeto Final Módulo 38 • PyCaret + Streamlit</p>",
    unsafe_allow_html=True
)