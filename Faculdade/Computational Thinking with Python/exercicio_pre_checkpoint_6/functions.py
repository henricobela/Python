
def adicionar(nome, sobrenome, telefone, email, pais, lista):
    x = {
            "Nome": nome,
            "Sobrenome": sobrenome,
            "Telefone": telefone,
            "E-mail": email,
            "País": pais
        }
    return lista.append(x)

def editar(email, nome, sobrenome, telefone, email_alterado, pais, lista):
    x = len(lista)
    for i in range(0,x,1):
        if lista[i]["E-mail"] == email:
            lista[i]["Nome"] = nome
            lista[i]["Sobrenome"] = sobrenome
            lista[i]["Telefone"] = telefone
            lista[i]["E-mail"] = email_alterado
            lista[i]["País"] = pais

                
def excluir(email, lista):
    x = len(lista)
    for i in range(0,x,1):
        if lista[i]["E-mail"] == email:
            del lista[i]
            return True


def ler(lista):
    x = len(lista)
    print("""
-----------------------------------------
                REGISTROS
-----------------------------------------
    """)
    for i in range(0,x,1):
        print(f"""
Email.............:{lista[i]["E-mail"]}
Nome..............:{lista[i]["Nome"]}
Sobrenome.........:{lista[i]["Sobrenome"]}
Telefone..........:{lista[i]["Telefone"]}
País..............:{lista[i]["País"]}
        """)  
    print("""
-----------------------------------------
                REGISTROS
-----------------------------------------
    """)


def pesquisar(email, lista):
    x = len(lista)
    for i in range(0,x,1):
        if lista[i]["E-mail"] == email: 
            print(f"""
-----------------------------------------
            PESQUISA POR EMAIL
-----------------------------------------
Email.............:{lista[i]["E-mail"]}
Nome..............:{lista[i]["Nome"]}
Sobrenome.........:{lista[i]["Sobrenome"]}
Telefone..........:{lista[i]["Telefone"]}
País..............:{lista[i]["País"]}
-----------------------------------------
            PESQUISA POR EMAIL
-----------------------------------------
            """)
            return True
            
         
def menu():

    print("""

     ------ CADASTRO DE CLIENTES ------
    |                                  |
    |      1 - Criar cliente           |
    |      2 - Listar clientes         |
    |      3 - Editar cliente          |
    |      4 - Excluir cliente         |
    |      5 - Pesquisar cliente       |
    |      6 - Sair                    |
    |                                  |
     ----------------------------------

    """)


def clear():

    print("\n"*125)

def verificar(email, lista):
    x = len(lista)
    for i in range(0,x,1):
        if lista[i]["E-mail"] == email:
            return True

def criar():
    nome = input("Qual o nome do seu cliente?.... ")
    sobrenome = input("Qual o sobrenome do seu cliente?.... ")
    telefone = input("Qual o telefone de seu cliente?... ")
    email = input("Qual o E-mail de seu cliente?..... ")
    pais = input("Qual o País de seu cliente?..... ")
    return nome, sobrenome, telefone, email, pais