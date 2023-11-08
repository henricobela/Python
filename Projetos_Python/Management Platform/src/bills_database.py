import sqlite3 as sqlite
import pandas as pd
import numpy as np



class Bills_Database():
    def __init__(self, path_to_db) -> None:
        self.path_to_db = path_to_db

    
    def check_connection(self) -> bool:
        try:
            sqlite.connect(self.path_to_db)
            return True
        except Exception as err:
            raise err
        

    def get_cursor_conn(self) -> tuple:
        if self.check_connection() == True:
            conn = sqlite.connect(self.path_to_db)
            cursor = conn.cursor()
            return conn, cursor
        
    
    def execute_query_df(self, query) -> pd.DataFrame:
        try:
            conn, cursor = self.get_cursor_conn()
            cursor.execute(query)
            data = cursor.fetchall()
            df = pd.DataFrame(data, columns=[col[0] for col in cursor.description])
            cursor.close()
            conn.close()
            return df
        except Exception as err:
            raise err
