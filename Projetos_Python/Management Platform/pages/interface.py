import streamlit as st
from streamlit_extras.switch_page_button import switch_page
from src.database import Database


st.header("PlatformAI")

option = st.selectbox(options = ["Selecione", "Gerenciamento de Contas", "Gerenciamento de Vendas"], 
                      label = "Selecione um dos serviços")

if option == "Gerenciamento de Contas":
    switch_page("bills_management")
elif option == "Gerenciamento de Vendas":
    switch_page("sales_management")
