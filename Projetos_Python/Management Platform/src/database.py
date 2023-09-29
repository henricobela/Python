import sqlite3 as sqlite
import pandas as pd
import numpy as np


class Database():
    def __init__(self, path_to_db) -> None:
        self.path_to_db = path_to_db


    def __get_connection(self) -> sqlite.connect:
        try:
            connection = sqlite.connect(self.path_to_db)
            return connection
        except sqlite.DatabaseError as err:
            raise err
    
    def __get_cursor(self) -> sqlite.Cursor:
        try:
            conn = self.__get_connection()
            cursor = conn.cursor()
            return cursor
        except sqlite.DatabaseError as err:
            raise err
        

    def check_connection(self) -> bool:
        try:
            self.__get_connection()
            return True
        except Exception as ex:
            raise ex
        

    def get_cursor_conn(self) -> tuple:
        if self.check_connection() == True:
            conn = self.__get_connection()
            cursor = self.__get_cursor()
            return conn, cursor
        
        
        

    def execute_query_login(self, query) -> bool:
        try:
            conn, cursor = self.get_cursor_conn()
            cursor.execute(query)
            conn.commit()
            conn.close()
            cursor.close()
            return True
        except sqlite.DatabaseError as err:
            raise err


    def execute_query_df(self, query) -> pd.DataFrame:
        try:
            conn, cursor = self.get_cursor_conn()
            cursor.execute(query)
            data = cursor.fetchall()
            df = pd.DataFrame(data, columns=[col[0] for col in cursor.description])
            conn.close()
            cursor.close()
            return df
        except sqlite.DatabaseError as err:
            raise err

        
           

    

