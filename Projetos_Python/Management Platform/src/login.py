from src.database import Database
import streamlit as st

db = Database(path_to_db = "utils/data/db.db")

def login(user, password) -> bool:
    sql = f"SELECT * FROM usuario WHERE login = '{user}' AND senha = '{password}';"
    if db.execute_query_login(query = sql): return True