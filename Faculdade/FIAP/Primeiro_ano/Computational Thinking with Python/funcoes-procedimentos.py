# procedimento nao retorna valores
# funções retornam valores - return - que pode ser reutilizado


# procedimento sem parametro
def saudacao_sem_parametro():
    print("Seja bem-vindo á FIAP")


# procedimento com parametro
def saudacao_com_parametro(x):
    print(f"{x}, Seja bem-vindo á FIAP")


# procedimento com + de 1 parametro
def flor(tipo, cor):
    print(f"A cor da {tipo} é: {cor}")


# procedimento com parametro padrão
def flor(tipo="Rosa", cor="Vermelha"):
    print(f"A cor da {tipo} é: {cor}")


def saudacao3(msg, nome):
    print(f"{msg} {nome}, seja bem-vindo a FIAP")


def saudacao4(hora, nome):
    if hora >= 3 and hora <= 12:
        print(f"Bom dia, {nome}, seja bem vindo á FIAP")
    elif hora >= 12 and hora <= 18:
        print(f"Boa tarde, {nome}, seja bem vindo á FIAP")
    elif hora >= 18 or hora <= 3:
        print(f"Boa noite, {nome}, seja bem vindo á FIAP")


def saudacao5(hora=20, nome="Edson"):
    if hora >= 3 and hora <= 12:
        print(f"Bom dia, {nome}, seja bem vindo á FIAP")
    elif hora >= 12 and hora <= 18:
        print(f"Boa tarde, {nome}, seja bem vindo á FIAP")
    elif hora >= 18 or hora <= 3:
        print(f"Boa noite, {nome}, seja bem vindo á FIAP")


# função sem parametro
def pi():
    return 3.14159


# função com parametro
def media_2n(n1, n2):
    return (n1 + n2) / 2


def prox_num(num):
    return print(f"Retorno: {num + 1}")


def maior_2n(n1, n2):
    if n1 > n2:
        return print(f"Retorno: {n1}")
    else:
        return print(f"Retorno: {n2}")


def maior_3n(n1, n2, n3):
    if n1 > n2:
        return print(f"Retorno: {n1}")
    elif n2 > n3:
        return print(f"Retorno: {n2}")
    else:
        return print(f"Retorno: {n3}")


def prox_mult5(n):
    return print(f"Retorno: {n // 5 * 5 + 5}")


def prox_mult5_v2(num):
    num += 1
    while num % 5 != 0:
        num += 1

    return print(f"Retorno: {num}")


def prox_mult_n(mult, num):
    return print(f"Retorno: {num // mult * mult + mult}")


def fatorial(num):
    result = 1
    for n in range(1, num + 1):
        result *= n
    return print(f"Retorno: {result}")


def potencia(n1, n2):
    # potencia = 1
    # for i in range(n2):
    #     potencia *= n1
    #     i += 1
    return print(f"Retorno: {n1 ** n2}")
    # return print(f"Retorno: {potencia}")


# Programa principal
print("PROCEDIMENTOS:-----------------------------")
saudacao_sem_parametro()
saudacao_com_parametro("Joao")
flor("Orquidea", "Azul")
flor()

print("-" * 50)

saudacao3("Boa noite", "Henrico")
saudacao4(16, "Henrico")
saudacao5(11, "Maria")
saudacao5()

print("-" * 50)
print("FUNCOES:-----------------------------")

raio = 4
area_circunferencia = pi() * raio**2
print(f"Area do circulo: {area_circunferencia}")
print(f"Media = {media_2n(6, 4)}")
print("-" * 50)

prox_num(5)
maior_2n(15, 98)
maior_3n(115, 23, 8)
prox_mult5(20)
prox_mult5_v2(20)
prox_mult_n(10, 2)
fatorial(4)
potencia(2, 4)
