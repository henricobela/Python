import streamlit as st


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