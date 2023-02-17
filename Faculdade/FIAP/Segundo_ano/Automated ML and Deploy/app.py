import streamlit as st
import time

col1, col2, col3 = st.columns(3)

with col1:
    col1.success("Coluna sucesso!!!")

with col2:
    col2.error("Coluna 2 Error!!!")

with col3:
    col3.warning("Coluna 3 Warning")
