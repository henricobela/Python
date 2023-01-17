import streamlit as st
import Controllers.ClienteController as ClienteController
import models.Cliente as cliente
import pandas as pd
from streamlit_option_menu import option_menu as om



def read_clientes():
    st.title("Clientes")
    costumer_list = []
    for item in ClienteController.Read():
        costumer_list.append([item.id, item.nome, item.empresa, item.email, item.comentario])  
    df = pd.DataFrame(costumer_list, columns = ["id", "Nome", "Empresa", "Email", "Cometario"])
    st.table(df)
