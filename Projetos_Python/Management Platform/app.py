import streamlit as st
from src.login import login, check_login
from streamlit_extras.switch_page_button import switch_page
import time 

st.header("PlatformAI")


with st.form(key = "login"):

    tab_login, tab_register = st.tabs(["Login", "Registrar-se"])

    with tab_login:
        user = st.text_input("Usuario: ", key = "log")
        password = st.text_input("Senha: ", type = "password", key = "log_pass")
        if st.form_submit_button("Entrar"):
            if login(user, password) == True:
                st.success(f"Usuario: {user} autorizado!")
                time.sleep(1)
                switch_page("interface")
            else:
                st.error(f"Usuario: {user} nao autorizado!")

    with tab_register:
        user = st.text_input("Usuario: ", key = "create")
        password = st.text_input("Senha: ", type = "password", key = "create_pass")
        if st.form_submit_button("Cadastrar"):
            if check_login(user, password) == True:
                st.success(f"Usuario: {user} Criado!")
                time.sleep(1)
                switch_page("interface")
            else:
                st.error(f"Usuario: {user} já possui uma conta!")