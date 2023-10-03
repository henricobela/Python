import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

st.header("Finanças")

tab_dash, tab_cadastro_contas, tab_cadastro_cartao = st.tabs(["Dashboard", "Contas", "Cartões"])

with tab_dash:
    chart_data = pd.DataFrame(
    np.random.randn(20, 3),
        columns=['a', 'b', 'c'])
    c = alt.Chart(chart_data).mark_circle().encode(
        x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])
    st.altair_chart(c, use_container_width=True)

with tab_cadastro_contas:

    with st.form(key = "contas_pag_rec"):

        tab_pag, tab_rec = st.tabs(["Contas á Pagar", "Recebimentos"])

        with tab_pag:
            col1, col2, col3 = st.columns([1,1,1])
            with col1:
                nome_conta = st.text_input("Nome da Conta: ")
            with col2:
                descricao_conta = st.text_input("Descrição da Conta")
            with col3:
                valor_conta = st.number_input("Valor da Conta")
            button_send_pag = st.form_submit_button("Enviar Conta")

        with tab_rec:
            st.success("teste recebimentos")
            button_send_rec = st.form_submit_button("Enviar Recebimento")

                    
