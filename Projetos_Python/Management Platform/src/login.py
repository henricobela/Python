from src.database import Database
import streamlit as st

db = Database(path_to_db = "utils/data/db.db")

def login(user, password) -> bool:
    check = db.execute_query_login(user = user, password = password)
    if check == True: 
        return True
    elif check == False:
        return False
    else:
        st.warning(check)


def check_login(user, password) -> bool:
    check_reg = db.register_user(user, password)
    if check_reg == True:
        return True
    else:
        return False