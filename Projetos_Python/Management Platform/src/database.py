import sqlite3 as sqlite
import pandas as pd
import numpy as np
import bcrypt, base64


class Database():
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
        
        
    def execute_query_login(self, user, password) -> bool or str:
        conn, cursor = self.get_cursor_conn()
        cursor.execute("SELECT senha FROM usuario WHERE login = ?", (user,))
        resultado = cursor.fetchone()
        cursor.close()
        conn.close()
        if resultado:
            senha_hash_armazenada = resultado[0]
            if bcrypt.checkpw(password.encode('utf-8'), senha_hash_armazenada.encode('utf-8')):
                return True
            else:
                return False
        else:
            return "Usuario não encontrado."


    def check_user(self, user):
        conn, cursor = self.get_cursor_conn()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM usuario WHERE login = ?", (user,))
        result = cursor.fetchone()
        if result:
            return True
        else:
            return False
        

    def register_user(self, user, password) -> bool:
        salt = bcrypt.gensalt()
        password = bcrypt.hashpw(password.encode('utf-8'), salt).decode('utf-8')
        conn, cursor = self.get_cursor_conn()
        if self.check_user(user) == False:
            try:
                cursor.execute("INSERT INTO usuario (login, senha) VALUES (?, ?)", (user, password))
                conn.commit()
                cursor.close()
                conn.close()
                return True
            except Exception as err:
                print(err)
        else:
            return False


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

        
           

    

