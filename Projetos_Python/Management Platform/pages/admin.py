import streamlit as st
from src.dataframe_functions import get_df


st.header("Painel do Administrador")
with st.expander(label = "Dados Usuarios"):
    st.dataframe(get_df())
