import streamlit as st
import pandas as pd
import numpy as np
from pycaret.regression import *
from sklearn.metrics import r2_score


st.set_page_config(layout="wide")

st.header("Checkpoint 2 - Computacao Neuromorfica e Super Computadores")
st.text("\n")
try:
    with st.sidebar:
        st.header("Checkpoint Neuromorfica")
        st.subheader("Henrico - RM95985")
        data = st.file_uploader("Enter Here the CSV File", type = "csv")
        if data:
            st.success("Data Loaded")

    if not data:
        st.warning("Please submit a CSV file")
    else:
        df = pd.read_csv(data)

    with st.expander("See data loaded"):
        if data:
            st.dataframe(df)
        
    with st.expander("See predictions"):
        if data:
            model = load_model("model_pickle")
            preds = predict_model(model, data = df)
            col1, col2 = st.columns([10, 4])
            score = r2_score(y_true = preds["target"], y_pred = preds["prediction_label"])
            col1.dataframe(preds)
            col2.metric("R2 Score", value = round(score, 2))
except:
    st.error("Please submit a valid CSV file")



st.text_input("LOGIN")
st.text_input("Senha")
if st.button("ENVIAR"):
    st.balloons()



