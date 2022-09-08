

def preenche_lista(lista):
    for i in range(0,10,1):
        elemento = float(input(f"Digite o {i+1}º elemento: "))
        lista.append(elemento)


def exibir_lista(lista):
    for i in range(0,10,1):
        print(f"Elemento {i + 1} vale: {lista[i]}")


def menu():
    print("="*10 + " Menu " + "="*10 + 
          "\n" + 
          "1 - preencher a lista\n" + 
          "2 - Exibir o conteudo da lista\n" + 
          "0 - Para sair\n")
####

lista = []

while True:
    menu()
    opcao = int(input())

    if opcao == 1:
        preenche_lista(lista)
    if opcao == 2:
        exibir_lista(lista)

    if opcao == 0:
        break



