import streamlit as st
from src.dataframe_functions import get_df
from streamlit_extras.switch_page_button import switch_page


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


if st.button("Voltar"):
    switch_page("interface")

st.header("Painel do Administrador")
with st.expander(label = "Dados Usuarios"):
    st.dataframe(get_df())
