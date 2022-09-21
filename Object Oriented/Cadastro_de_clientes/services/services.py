import sqlite3

banco = sqlite3.connect("C:\\Users\\henri\\Github\\Python\\Object Oriented\\Cadastro_de_clientes\\database\\database.db", check_same_thread = False)

cursor = banco.cursor()