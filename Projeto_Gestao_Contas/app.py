import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

recebimentos, despesa_fixa, despesa_variavel, despesa_gerencia, imposto, imobiliaria = st.tabs(
    ["Recebimentos", 
    "Despesas Fixas",
    "Despesas Variaveis", 
    "Despesas Gerencia", 
    "Imposto", 
    "Imobiliária"])


with recebimentos:
    df = {"Data": "10/10/1996",
          "Descrição": "Bla bla bla"}
    df = pd.DataFrame(df, index = [0])
    st.dataframe(df)

    

with despesa_fixa:
    st.warning("DESPESAS FIXASSSSS UHUUUUULLLLL")

with despesa_variavel:
    st.warning("DESPESAS VARIAVEIIIISSS UHUUUUULLLLL")

with despesa_gerencia:
    st.info("DESPESAS GERENCIAAAA UHUUUUULLLLL")

with imposto:
    st.success("IMPOSTOSSSSSS UHUUUUULLLLL")

with imobiliaria:
    st.success("IMOBILIARIAAAAAAAAAAAAAAAAA UHUUUUULLLLL")