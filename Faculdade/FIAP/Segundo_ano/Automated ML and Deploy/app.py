import streamlit as st
import time

col1, col2, col3 = st.columns(3)

with col1:
    for i in range(100):
        time.sleep(1)
        col1.success("Coluna {} sucesso!!!".format(i))

with col2:
    col2.error("Coluna 2 Error!!!")

with col3:
    col3.warning("Coluna 3 Warning")
