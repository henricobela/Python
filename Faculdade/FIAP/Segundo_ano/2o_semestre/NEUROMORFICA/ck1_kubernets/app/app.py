import streamlit as st
import pandas as pd
import numpy as np
from pycaret.regression import *
from sklearn.metrics import r2_score
import requests as req
from datetime import datetime
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(layout = "wide")

st.header("Global Solutions - Computação Neuromófica")
st.text("\n")

def organize_data(df):

    df_true = df.copy()

    df.drop("entry_id", axis = 1, inplace = True)
    df["created_at"] = df["created_at"].apply(lambda x: datetime.strptime(x, "%Y-%m-%dT%H:%M:%SZ").strftime("%Y-%m-%d"))
    df["date"] = np.nan * len(df)
    df["time"] = np.nan * len(df)
    df["local"] = np.nan * len(df)
    for idx, value in enumerate(df.created_at):
        df["date"][idx] = df["created_at"][idx].split("-")[0]
    for idx, value in enumerate(df.created_at):
        df["time"][idx] = df["created_at"][idx].split("-")[1]
    for idx, value in enumerate(df.created_at):
        df["local"][idx] = df["created_at"][idx].split("-")[-1]
    df.drop("created_at", axis = 1, inplace = True)
    df = df.reindex(["date", "time", "local", "field2", "field3", "field4", "field5", "field6", "field7", "field8", "field1"], axis = 1)
    df = df.rename(columns = {"field6": "target"})
    df.local = df.local.apply(lambda x: 0 if x == "UTC" else 1)
    for col in df.columns:
        df[col] = df[col].astype(float)

    
    return df, df_true


try:
    with st.sidebar:
        st.header("GS Neuromorfica")
        data = req.get("https://api.thingspeak.com/channels/2167188/feeds.json").json()["feeds"]
        if data:
            st.success("Data Loaded")

    if not data:
        st.warning("Please submit a CSV file")
    else:
        df = pd.DataFrame(data)
        df, df_true = organize_data(df)

    with st.expander("See data loaded"):
        if data:
            st.dataframe(df)
        
    with st.expander("See predictions"):
        if data:
            model = load_model("app/model_pickle")
            preds = predict_model(model, data = df)
            col1, col2 = st.columns([10, 4])
            score = r2_score(y_true = preds["target"], y_pred = preds["prediction_label"]) * 100
            col1.dataframe(preds)
            col2.metric("R2 Score", value = round(score, 2))
    
    with st.expander("See Results"):
        col_graf_1, col_graf_2 = st.columns([1,1])
        with col_graf_1:
            sample_y = df_true["created_at"].sample(20) 
            sample_x = df_true["field1"].sample(20) 
            fig, ax = plt.subplots()
            ax.set_title("TEMPERATURE DHT")
            ax = sns.lineplot(y = sample_y, x = sample_x)
            plt.ylabel("Date&Time")
            plt.xlabel("FIELD 1")
            st.pyplot(fig)

        with col_graf_2:
            sample_y = df_true["created_at"].sample(20) 
            sample_x = df_true["field5"].sample(20) 
            fig, ax = plt.subplots()
            ax.set_title("TEMPERATURE BMP")
            ax = sns.lineplot(y = sample_y, x = sample_x)
            plt.ylabel("Date&Time")
            plt.xlabel("FIELD 5")
            st.pyplot(fig)

except Exception as e:
    st.error(e)



