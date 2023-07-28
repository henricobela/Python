#!pip install streamlit
import streamlit as st
import pandas as pd
import numpy as np
import pickle
from pycaret.classification import *
from sklearn.metrics import accuracy_score
import altair as alt


# def color_pred(val):
#     color = 'olive' if val > treshold else 'orangered'
#     return f'background-color: {color}'

def get_values():
    return pd.read_csv("data/data.csv")


def convert_values(df):
    df['ID'] = [0] * len(df)
    df.Year_Birth = df.Year_Birth.astype("int64")
    df.Income = df.Income.astype("float64")
    df.Kidhome = df.Kidhome.astype("int64")
    df.Teenhome = df.Teenhome.astype("int64")
    df.Recency = df.Recency.astype("int64")
    df.MntWines = df.MntWines.astype("int64")
    df.MntFruits = df.MntFruits.astype("int64")
    df.MntMeatProducts = df.MntMeatProducts.astype("int64")
    df.MntFishProducts = df.MntFishProducts.astype("int64")
    df.MntSweetProducts = df.MntSweetProducts.astype("int64")
    df.MntGoldProds = df.MntGoldProds.astype("int64")
    df.NumDealsPurchases = df.NumDealsPurchases.astype("int64")
    df.NumWebPurchases = df.NumWebPurchases.astype("int64")
    df.NumCatalogPurchases = df.NumCatalogPurchases.astype("int64")
    df.NumStorePurchases = df.NumStorePurchases.astype("int64")
    df.NumWebVisitsMonth = df.NumWebVisitsMonth.astype("int64")
    df.AcceptedCmp3 = df.AcceptedCmp3.astype("int64")
    df.AcceptedCmp4 = df.AcceptedCmp4.astype("int64")
    df.AcceptedCmp5 = df.AcceptedCmp5.astype("int64")
    df.AcceptedCmp1 = df.AcceptedCmp1.astype("int64")
    df.AcceptedCmp2 = df.AcceptedCmp2.astype("int64")
    df.Complain = df.Complain.astype("int64")
    df.Z_CostContact = df.Z_CostContact.astype("int64")
    df.Z_Revenue = df.Z_Revenue.astype("int64")

    return df


st.set_page_config( page_title = 'Deploy - Checkpoint AutoML',
                    page_icon = 'images/logo_fiap.png',
                    layout = 'wide',
                    initial_sidebar_state = 'expanded')

st.title('Checkpoint AutoML - Deploy')

tab_predictions, tab_analytics = st.tabs(["Predictions", "Analytics"])

with st.sidebar:
    c1, c2 = st.columns(2)
    c1.image('images/logo_fiap.png', width = 100)
    c2.write('')
    c2.subheader('Auto ML - Fiap [v1]')

    database = st.radio('Choose one way to get data:', ('CSV', 'Link', 'Online'))

    if database == 'CSV':
        st.info('CSV file upload')
        file = st.file_uploader('Choose a CSV file', type = 'csv', accept_multiple_files = False)
    
    if database == "Link":
        link = st.text_input("Link it bellow:")
        if st.button("Submit"):
            if link:
                st.success("linked!")
            else:
                st.error("Please enter a valid link.")


with tab_predictions:

    with st.expander('App Description', expanded = False):
        var_test = 5
        st.write('The main objective of this app is predict and deploy!')

    if database == 'CSV':
        if file:
            df = pd.read_csv(file)

            check_index = ['ID', 'Year_Birth', 'Dt_Customer', 'Z_CostContact', 'Z_Revenue', 'Response']

            for index in check_index:
                if index not in df.columns:
                    df[index] = [0] * len(df)

            model = load_model('model/model_pickle')

            predictions = predict_model(model, data = df, raw_score = True)

            with st.expander('View CSV loaded:', expanded = False):
                c1, _ = st.columns([2,4])
                qtd_linhas = c1.slider('View CSV lines:', 
                                        min_value = 5, 
                                        max_value = df.shape[0], 
                                        step = 10,
                                        value = 5)
                st.dataframe(df.head(qtd_linhas))

            with st.expander('View Predictions:', expanded = False):

                c1, _, c2, c3, c4 = st.columns([2,.5,1,1,1])

                form = c1.form("form")
                score = accuracy_score(y_pred = predictions["prediction_label"], y_true = predictions["Response"])

                treshold = c1.slider('Treshold (ponto de corte para considerar predição como True)',
                        min_value = 0.0,
                        max_value = 1.0,
                        step = .1,
                        value = 0.9)
                
                qtd_true = predictions.loc[predictions['Response'] > treshold].shape[0]

                c2.metric('Qtd clientes True', value = qtd_true)
                c3.metric('Qtd clientes False', value = len(predictions) - qtd_true)
                c4.metric('Score', value = round(score * treshold, 2))

                
                # with form:
                    
                    # button_score = form.form_submit_button("See score")
                    # if button_score:
                    #     if score > .80:
                    #         st.success(f"Score: {score}")
                    #         st.balloons()
                    #     elif .50 < score < .80:
                    #         st.warning(f"Score: {score}")
                    #     else:
                    #         st.error(f"Score: {score}")
                        
                
                st.header("Dataframe with predictions")
                st.dataframe(predictions)
                

                csv = predictions.to_csv(sep = ';', decimal = ',', index = True)
                st.markdown(f'CSV shape which will be downloaded: {predictions.shape}')
                st.download_button(label = 'Download CSV',
                                data = csv,
                                file_name = 'Predicoes.csv',
                                mime = 'text/csv')

            
        else:
            st.warning('Please submit a CSV file')

    elif database == "Link":
        if link:
            st.warning("Dev")

    elif database == "Online":
        with st.sidebar:
            lista = ['Year_Birth', 'Education', 'Marital_Status', 'Income', 'Kidhome',
            'Teenhome', 'Dt_Customer', 'Recency', 'MntWines', 'MntFruits',
            'MntMeatProducts', 'MntFishProducts', 'MntSweetProducts',
            'MntGoldProds', 'NumDealsPurchases', 'NumWebPurchases',
            'NumCatalogPurchases', 'NumStorePurchases', 'NumWebVisitsMonth',
            'AcceptedCmp3', 'AcceptedCmp4', 'AcceptedCmp5', 'AcceptedCmp1',
            'AcceptedCmp2', 'Complain', 'Z_CostContact', 'Z_Revenue']
            
            dicionario = {i : [] for i in lista}

            help_df = get_values()
            help_df.drop(columns = ["ID", "Response"], inplace = True)
            
            lista_values = []
            for col in help_df.columns:
                lista_values.append(help_df[col].sample().values[0])

            for idx, value in enumerate(lista):
                slide = st.text_input(value, value = lista_values[idx])
                dicionario[value].append(slide)

        df = pd.DataFrame(dicionario)
        df = convert_values(df)
        model = load_model('model/model_pickle')
        predictions = predict_model(model, data = df, raw_score = True)

        with st.expander('View Data Inputed:', expanded = False):
            c1, _ = st.columns([2,4])
            qtd_linhas = c1.slider('View Dataframe lines:', 
                                    min_value = 5, 
                                    max_value = df.shape[0], 
                                    step = 10,
                                    value = 5)
            st.dataframe(df.head(qtd_linhas))

        with st.expander('View Predictions:', expanded = False):

            c1, _, c2, c3, c4 = st.columns([2,.5,1,1,1])

            treshold = c1.slider('Treshold (ponto de corte para considerar predição como True)',
                    min_value = 0.0,
                    max_value = 1.0,
                    step = .1,
                    value = .5)
            
            qtd_true = predictions.loc[predictions['prediction_score_1'] > treshold].shape[0]

            c2.metric('Qtd clientes True', value = qtd_true)
            c3.metric('Qtd clientes False', value = len(predictions) - qtd_true)

            st.header("Dataframe with predictions")

            predictions = predictions.drop(columns = ['ID'])
            st.dataframe(predictions)

            csv = predictions.to_csv(sep = ';', decimal = ',', index = True)
            st.markdown(f'CSV shape which will be downloaded: {predictions.shape}')
            st.download_button(label = 'Download CSV',
                            data = csv,
                            file_name = 'Predicoes.csv',
                            mime = 'text/csv')


with tab_analytics:

    if database == "Online":
        st.warning("This view is only avaiable in CSV Mode!")
    else:
        try:
            chart = alt.Chart(df).mark_boxplot(extent='min-max').encode(
                x='Response:O',
                y='Income:Q'
            )

            st.altair_chart(chart, theme="streamlit", use_container_width=True)

            chart_hist = alt.Chart(df).mark_bar().encode(
                alt.X("Response:Q", bin=True),
                y='count()',
            )

            st.altair_chart(chart_hist, theme="streamlit", use_container_width=True)
        except:
            st.error("Please submit a CSV file")









