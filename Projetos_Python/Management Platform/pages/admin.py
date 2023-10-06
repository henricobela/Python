import streamlit as st
from src.dataframe_functions import get_df


st.markdown(
    """
        <style>
            [data-testid="collapsedControl"] {
                display: none
            }
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
        </>
    """,
    unsafe_allow_html = True)


st.header("Painel do Administrador")
with st.expander(label = "Dados Usuarios"):
    st.dataframe(get_df())
