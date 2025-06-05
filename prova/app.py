import streamlit as st
import pandas as pd

st.title("Análise de Frequência: País e Produto")

df = pd.read_csv("MS_Financial_Sample.csv", sep=';', on_bad_lines='skip')
df.columns = df.columns.str.strip()

st.subheader("Cabeçalhos detectados")
st.write(df.columns.tolist())

if 'Country' in df.columns and 'Product' in df.columns:
    st.subheader("Prévia dos dados")
    st.dataframe(df.head())

    top_country = df['Country'].value_counts().idxmax()
    country_count = df['Country'].value_counts().max()

    top_product = df['Product'].value_counts().idxmax()
    product_count = df['Product'].value_counts().max()

    st.subheader("Insights Gerados")
    st.markdown(f"""
    - País mais presente: {top_country} ({country_count} ocorrências)
    - Produto mais presente: {top_product} ({product_count} ocorrências)
    """)

    st.subheader("Frequência por País")
    st.bar_chart(df['Country'].value_counts())

    st.subheader("Frequência por Produto")
    st.bar_chart(df['Product'].value_counts())
else:
    st.error("As colunas 'Country' e 'Product' não foram encontradas. Veja os nomes detectados acima.")
