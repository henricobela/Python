import streamlit as st
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



st.header("PlatformAI")

option = st.selectbox(options = ["Selecione", "Gerenciamento de Contas", "Gerenciamento de Vendas", "Admin"], 
                      label = "Selecione um dos serviços")

if option == "Gerenciamento de Contas":
    switch_page("bills_management")
elif option == "Gerenciamento de Vendas":
    switch_page("sales_management")
elif option == "Admin":
    switch_page("admin")