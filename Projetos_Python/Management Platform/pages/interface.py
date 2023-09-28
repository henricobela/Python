import streamlit as st
from streamlit_extras.switch_page_button import switch_page


st.header("PlatformAI")

option = st.selectbox(options = ["Selecione um dos serviços", "Gerenciamento de Contas", "Gerenciamento de Vendas"], label = "")

if option == "Gerenciamento de Contas":
    switch_page("bills_management")
elif option == "Gerenciamento de Vendas":
    switch_page("sales_management")