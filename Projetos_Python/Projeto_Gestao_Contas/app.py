import streamlit as st
import pandas as pd
from functions.functions import *

df = pd.read_excel("data.xlsx", index_col=0)
df.Data = df.Data.astype(str)


st.set_page_config(layout="wide")


(
    recebimentos,
    despesa_fixa,
    despesa_variavel,
    despesa_gerencia,
    imposto,
    imobiliaria,
) = st.tabs(
    [
        "Recebimentos",
        "Despesas Fixas",
        "Despesas Variaveis",
        "Despesas Gerencia",
        "Imposto",
        "Imobiliária",
    ]
)


with recebimentos:
    filtro_menu("Recebimentos", df)

with despesa_fixa:
    filtro_menu("Despesas fixas", df)

with despesa_variavel:
    filtro_menu("Despesas variáveis", df)

with despesa_gerencia:
    filtro_menu("Pessoas", df)

with imposto:
    filtro_menu("Impostos", df)

with imobiliaria:
    filtro_menu("Recebimentos", df)
