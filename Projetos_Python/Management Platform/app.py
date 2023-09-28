import streamlit as st
from src.login import login
from streamlit_extras.switch_page_button import switch_page
import time 

st.header("PlatformAI")


with st.form(key = "login"):

    user = st.text_input("Usuario: ")
    password = st.text_input("Senha: ", type = "password")
    
    if st.form_submit_button("Entrar"):
        if login(user, password) == True:
            st.success(f"User: {user} Authorized!")
            time.sleep(1)
            switch_page("interface")
        else:
            st.error(f"User: {user} not authorized!")
