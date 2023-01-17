import streamlit as st

def filtro_menu(transacao: str, df):
    t = df[df["Tipo de Lancamento"] == transacao]
    t = t.drop(columns = ["Tipo de Lancamento"])
    st.dataframe(t, use_container_width = True)  