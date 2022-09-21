import sqlite3

banco = sqlite3.connect("C:\\Users\\henri\\Github\\Python\\Object Oriented\\Cadastro_de_clientes\\database.db")

cursor = banco.cursor()

#create
# id = str(6)
# nome = "Joao da Silva Pereira"
# empresa = "FIAP"
# email = "joaodasilvaPereira@email.com"
# comentario = "sem comentarios, apenas decepcoes"
# cursor.execute("INSERT INTO cliente VALUES ('"+id+"', '"+nome+"', '"+empresa+"', '"+email+"', '"+comentario+"')")
# banco.commit()
# cursor.execute(f"INSERT INTO cliente VALUES ('{id}', '{nome}', '{empresa}', '{email}', '{comentario}')")
# banco.commit()
# cursor.execute("INSERT INTO cliente VALUES (2, 'Carla Ferreira', 'Santos FC', 'carla@email.com', 'otimos produtos')")
# banco.commit()

#Read
# cursor.execute("SELECT * FROM cliente")
# print(cursor.fetchall())


#Update
# cursor.execute("UPDATE cliente SET nome = 'Fabio Denis' WHERE nome = 'Joao da Silva Pereira'")
# banco.commit()


#Delete
# try:
#     banco = sqlite3.connect("C:\\Users\\henri\\Github\\Python\\Object Oriented\\Cadastro_de_clientes\\database.db")

#     cursor = banco.cursor()

#     cursor.execute("DELETE from cliente WHERE empresa = 'Santos FC'")
#     banco.commit()
#     banco.close()

#     print("dados excluidos")
# except sqlite3.Error() as erro:
#     print("não foi excluido", erro)


