import pandas as pd
import streamlit as st
from src.database import Database


def get_df() -> pd.DataFrame:
    db = Database(path_to_db = "utils/data/db.db")
    sql = "SELECT * FROM usuario"
    df = db.execute_query_df(query = sql)
    return df