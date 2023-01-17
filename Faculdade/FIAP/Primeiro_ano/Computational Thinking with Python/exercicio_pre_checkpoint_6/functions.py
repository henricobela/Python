import random


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

     ---------- CADASTRO DE CLIENTES ----------
    |                                          |
    |      1 - Adicionar um novo contato       |
    |      2 - Lista de contatos               |
    |      3 - Editar um contato               |
    |      4 - Apagar um contato               |
    |      5 - Pesquisar um contato            |
    |      6 - Voltar                          |
    |                                          |
     ------------------------------------------

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






def menu_captcha():
    print("""

                    CAPTCHAS
    
    1 - Com 10 caracteres
    2 - Definindo a quantidade de caracteres
    3 - Definindo os caracteres
    4 - Gravando/Exibindo em uma lista
    5 - Gravando/Exibindo em um arquivo
    0 - Voltar

    """)

def menu_captcha_dinamico():
    print("""
Tipos de caracteres:    
    (l)etras minusculas
    (L)etras maiusculas
    (d)igitos
    (e)speciais
    
    """)

def captcha(size = 10):
    text = "abcdefghijklmnopqrstuvwxyz"
    nums = "0123456789"
    punct = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'

    chars = text + nums + punct
    return ''.join(random.choice(chars) for _ in range(size))


def captcha_dinamico(size, escolha):
    text = "abcdefghijklmnopqrstuvwxyz"
    nums = "0123456789"
    punct = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'

    lista = []

    for i in escolha:
        if i == "l":
            lista.append(text)
        elif i == "L":
            lista.append(text.upper())
        elif i == "d":
            lista.append(nums)
        elif i == "e":
            lista.append(punct)

    chars = ""
    for x in lista: 
        chars += x

    return ''.join(random.choice(chars) for _ in range(size))


def escrever_arquivo(lista):
    count = 0
    with open("lista_captchas.txt", "w") as file:
        for captcha in lista:
            count += 1
            file.write(f"Captcha {count}: " + captcha + "\n")


def ler_arquivo():
    with open("lista_captchas.txt", "r") as file:
        x = file.readlines()
    return "\n".join(x)


def v5(lista):
    escrever_arquivo(lista)
    y = ler_arquivo()
    return y
