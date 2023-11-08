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


st.success("Sales")

if st.button("Voltar"):
    switch_page("interface")