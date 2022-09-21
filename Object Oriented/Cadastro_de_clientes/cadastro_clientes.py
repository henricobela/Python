import streamlit as st
import Controllers.ClienteController as ClienteController
import models.Cliente as cliente


st.title("Formulario doido")

with st.form(key = "inserir"):
    id = st.number_input(label = "Digite seu id", format = "%d", step = 1)
    nome = st.text_input(label = "Digite seu nome")
    empresa = st.text_input(label = "Digite sua empresa")
    email = st.text_input(label = "Digite seu email")
    comentario = st.text_area(label = "Comentario")
    submit = st.form_submit_button("Enviar")

if submit:
    cliente.id = id
    cliente.nome = nome
    cliente.empresa = empresa
    cliente.email = email
    cliente.comentario = comentario

    ClienteController.Incluir(cliente)


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


