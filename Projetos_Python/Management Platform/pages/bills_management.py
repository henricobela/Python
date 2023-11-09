import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
from streamlit_extras.switch_page_button import switch_page
from src.bills_database import Bills_Database


db = Bills_Database(path_to_db = "utils/data/db_bills.db")
conn, cursor = db.get_cursor_conn()

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


col_header, col_voltar = st.columns([1, 0.2])
col_header.header("Finanças")

if col_voltar.button("Voltar"):
    switch_page("interface")

st.markdown("---", unsafe_allow_html = True)

tab_dash, tab_cadastro_contas, tab_cadastro_cartao = st.tabs(["Dashboard", "Contas", "Cartões"])

with tab_dash:

    df_from_db_despesa = db.execute_query_df("SELECT * FROM bills_despesa")
    df_from_db_receb = db.execute_query_df("SELECT * FROM bills_recebimento")

    with st.expander("Contas"):
        col_desp, col_receb = st.columns([1, 1])
        with col_desp:
            st.error("Despesas")
            st.dataframe(df_from_db_despesa)
        with col_receb:
            st.success("Recebimentos")
            st.dataframe(df_from_db_receb)

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
                nome_conta = st.text_input("Nome da Conta: ", key = "nome_conta_key")
                data_compra = st.text_input("Data da conta (Ex: 10/10/2023): ", key = "data_compra_key")
                parcelas = st.number_input("Parcelas: ", step = 1, key = "parcelas_pag_key")
            with col2:
                descricao_conta = st.text_input("Descrição da Conta", key = "descricao_conta_key")
                despesa = st.selectbox("Tipo Despesa", ("Fixa", "Variável"), placeholder = "Selecione o Tipo de Despesa")
            with col3:
                categoria = st.text_input("Categoria: ", key = "categoria_pag_key")
                valor_conta = st.number_input("Valor da Conta", key = "valor_conta_key")
                if valor_conta != 0:
                    valor_parcela = valor_conta / parcelas 

            button_send_pag = st.form_submit_button("Enviar Conta")
            if button_send_pag:
                data_pag = {
                    "Conta": nome_conta,
                    "Descrição": descricao_conta,
                    "Data": data_compra,
                    "Tipo despesa": despesa,
                    "Parcelas": parcelas,
                    "Categoria": categoria,
                    "Valor": valor_conta,
                    "Valor das Parcelas": valor_parcela,
                }
                df_pag = pd.DataFrame(data_pag, index = [0])
                df_pag.to_sql('bills_despesa', conn, index=False, if_exists='append')
                st.success("Despesa Cadastrada")
                

        with tab_rec:
            col4, col5, col6 = st.columns([1,1,1])
            with col4:
                nome_rec = st.text_input("Nome da Conta: ", key = "nome_rec_key")
                data_rec = st.text_input("Data da conta (Ex: 10/10/2023): ", key = "data_rec_key")
                tipo_recebimento = st.selectbox("Tipo de Recebimento", ["Fixo", "Variável"])
            with col5:
                descricao_rec = st.text_input("Descrição da Conta", key = "descricao_rec_key")
                parcelas_rec = st.number_input("Parcelas: ", step = 1, key = "parcelas_rec_key")
            with col6:
                categoria_rec = st.text_input("Categoria: ", key = "categoria_rec_key")
                valor_rec = st.number_input("Valor da Conta", key = "valor_rec_key")
                if valor_rec != 0:
                    valor_parcela_rec = valor_rec / parcelas_rec

            button_send_rec = st.form_submit_button("Enviar Recebimento")
            if button_send_rec:
                data_receb = {
                    "Conta": nome_rec,
                    "Descrição": descricao_rec,
                    "Data": data_rec,
                    "Tipo de Recebimento": tipo_recebimento,
                    "Parcelas": parcelas_rec,
                    "Categoria": categoria_rec,
                    "Valor": valor_rec,
                    "Valor das Parcelas": valor_parcela_rec,
                    "Tipo": "recebimento"
                }
                df_rec = pd.DataFrame(data_receb, index = [0])
                df_rec.to_sql('bills_recebimento', conn, index=False, if_exists='append')
                st.success("Recebimento Cadastrado")


            
            


                    
