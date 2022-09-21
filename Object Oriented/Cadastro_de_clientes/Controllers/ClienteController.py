import sqlite3
import services.services as db

def Incluir(cliente):
    try:
        db.cursor.execute("""
        INSERT INTO cliente (id, nome, empresa, email, comentario) 
        VALUES (?, ?, ?, ?, ?)""",
        (cliente.id, cliente.nome, cliente.empresa, cliente.email, cliente.comentario)).rowcount
        db.banco.commit()
    except sqlite3.Error as error:
        print(f"Erro ao inserir dados, erro: {error}")


def Read(cliente):
    ...


def Update(cliente):
    ...


def Delete(cliente):
    ...