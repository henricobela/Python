import streamlit as st
import pandas as pd
import numpy as np
import altair as alt


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
                data_compra = st.text_input("Data da conta (Ex: 10/10/2023): ")
            with col2:
                descricao_conta = st.text_input("Descrição da Conta")
                parcelas = st.number_input("Parcelas: ", step = 1)
            with col3:
                categoria = st.text_input("Categoria: ")
                valor_conta = st.number_input("Valor da Conta")
            button_send_pag = st.form_submit_button("Enviar Conta")

            if button_send_pag:
                data = {
                    "Conta": nome_conta,
                    "Descrição": descricao_conta,
                    "Data": data_compra,
                    "Parcelas": parcelas,
                    "Categoria": categoria,
                    "Valor": valor_conta,
                    "Tipo": "conta"
                }
                df = pd.DataFrame(data, index = [0])
                st.dataframe(df)
                st.balloons()

        with tab_rec:
            col4, col5, col6 = st.columns([1,1,1])
            with col4:
                nome_rec = st.text_input("Nome da Conta: ")
                data_rec = st.text_input("Data da conta (Ex: 10/10/2023): ")
            with col5:
                descricao_rec = st.text_input("Descrição da Conta")
                parcelas_rec = st.number_input("Parcelas: ", step = 1)
            with col6:
                categoria_rec = st.text_input("Categoria: ")
                valor_rec = st.number_input("Valor da Conta")
            button_send_rec = st.form_submit_button("Enviar Conta")

            if button_send_rec:
                data = {
                    "Conta": nome_rec,
                    "Descrição": descricao_rec,
                    "Data": data_rec,
                    "Parcelas": parcelas_rec,
                    "Categoria": categoria_rec,
                    "Valor": valor_rec,
                    "Tipo": "recebimento"
                }
                df = pd.DataFrame(data, index = [0])
                st.dataframe(df)
                st.balloons()

            st.success("teste recebimentos")
            button_send_rec = st.form_submit_button("Enviar Recebimento")


                    
