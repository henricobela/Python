import sqlite3 as sqlite
import pandas as pd
import numpy as np


class Database():
    def __init__(self, db, path_to_db) -> None:
        self.db = db
        self.path_to_db = path_to_db


    def __get_connection(self) -> sqlite.connect:
        try:
            connection = self.db.connect(self.path_to_db)
            return connection
        except sqlite.DatabaseError as err:
            raise err
        

    def check_connection(self) -> bool:
        try:
            self.__get_connection.cursor()
            return True
        except Exception as ex:
            return False
        

    def get_cursor_conn(self) -> sqlite.Cursor:
        if self.check_connection() == True:
            conn = self.__get_connection()
            cursor = conn.cursor()
            return conn, cursor
        

    def execute_query(self, query) -> bool:
        conn, cursor = self.get_cursor_conn()

            
        
           

    

