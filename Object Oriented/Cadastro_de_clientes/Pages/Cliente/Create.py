import streamlit as st
import Controllers.ClienteController as ClienteController
import models.Cliente as cliente
import pandas as pd
from streamlit_option_menu import option_menu as om


def create_cliente():
    st.title("Formulário")

    with st.form(key = "inserir"):
        id = st.number_input(label = "Digite seu id", format = "%d", step = 1)
        nome = st.text_input(label = "Digite seu nome")
        empresa = st.text_input(label = "Digite sua empresa")
        email = st.text_input(label = "Digite seu email")
        comentario = st.text_area(label = "Comentario")
        submit = st.form_submit_button("Enviar")

    if submit:
        ClienteController.Incluir(cliente.Cliente(id, nome, empresa, email, comentario))
        st.success("Cliente Cadastrado com sucesso")
