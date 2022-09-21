from math import cos
import sqlite3
import services.services as db
import models.Cliente as cliente

def Incluir(cliente):
    try:
        db.cursor.execute("""
        INSERT INTO cliente (id, nome, empresa, email, comentario) 
        VALUES (?, ?, ?, ?, ?)""",
        (cliente.id, cliente.nome, cliente.empresa, cliente.email, cliente.comentario)).rowcount
        db.banco.commit()
    except sqlite3.Error as error:
        print(f"Erro ao inserir dados, erro: {error}")


def Read():
    try:
        db.cursor.execute("""
        SELECT * FROM cliente
        """)
        costumer_list = []
        for row in db.cursor.fetchall():
            costumer_list.append(cliente.Cliente(row[0], row[1], row[2], row[3], row[4], ))
        
        return costumer_list

    except sqlite3.Error as error:
        print(f"Erro ao ler dados, erro: {error}")


def Update(cliente):
    ...


def Delete(cliente):
    ...