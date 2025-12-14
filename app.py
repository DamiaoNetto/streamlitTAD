import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


st.title("Meu primeiro app com Streamlit🚀")


url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv"
df = pd.read_csv(url)

st.write(df)
st.sidebar.header("Filtros")

# Criando um filtro por dia da semana
dia_selecionado = st.sidebar.selectbox(
    "Selecione o dia:",
    df['day'].unique()
)

# Aplicando o filtro
df_filtrado = df[df['day'] == dia_selecionado]

# --- EXIBIÇÃO DOS DADOS ---
st.subheader(f"Dados filtrados para o dia: {dia_selecionado}")
st.write(df_filtrado)

# --- HISTOGRAMA ---
st.subheader("Histograma da Conta Total")

fig, ax = plt.subplots()
sns.histplot(data=df_filtrado, x='total_bill', kde=True, ax=ax)
ax.set_xlabel("Valor da conta")
ax.set_ylabel("Frequência")

st.pyplot(fig)