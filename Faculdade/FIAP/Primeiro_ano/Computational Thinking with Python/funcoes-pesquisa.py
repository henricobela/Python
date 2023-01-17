def contar_elem(lista):
    elem = 0
    for i in lista:
        elem += 1
    return elem

def procurar_lista(lista, elem):
    elemento = False
    for i in range(contar_elem(lista)):
        if lista[i] == elem:
            elemento = True
            break
            
    return (elemento)


def ordenar_lista_crescente(lista):
    for travado in range(0, 10, 1):
        for proximo in range(travado + 1, 11, 1):
            if lista[travado] > lista[proximo]:
                aux = lista[travado]
                lista[travado] = lista[proximo]
                lista[proximo] = aux

    return lista


def ordenar_lista_decrescente(lista):
    for travado in range(0, 10, 1):
        for proximo in range(travado + 1, 11, 1):
            if lista[travado] < lista[proximo]:
                aux = lista[travado]
                lista[travado] = lista[proximo]
                lista[proximo] = aux

    return lista


def ordenar_lista(lista, ordem = True):
    if ordem == True:
        ordenar_lista_crescente(lista)
    else:
        ordenar_lista_decrescente(lista)
    
    return lista
        

def procurar_lista_quebra(lista, elem):
    inicio = 0
    fim = 9
    encontrou = False
    for i in range(inicio, fim + 1):
        quebra = (inicio + fim) // 2
        if elem == lista[quebra]:
            encontrou = True
            break
        elif elem > lista[quebra]:
            inicio = quebra + 1
        else:
            fim = quebra - 1

    return encontrou



lista = [1, 4, 88, 6, 9, 10, 55, 265, 333, 1000, 2556]
ordem = True

print(contar_elem(lista))

print(procurar_lista(lista, 55))

print(ordenar_lista_crescente(lista))

print(ordenar_lista_decrescente(lista))

print(ordenar_lista(lista, ordem))

print(procurar_lista_quebra(lista, 1000))
