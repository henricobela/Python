

def separador(texto):
    """
    Esta funcao retorna uma separação de texto personalizada
    """
    print("-" * 100)
    print(texto)
    print("-" * 100)


def remover_menor_nota(c1, c2, c3):
    """
    Esta funcao retorna uma lista com as duas maiores notas de checkpoints
    """
    checkpoints = [c1, c2, c3]
    min_grade = None
    for i in checkpoints:
        if (min_grade is None or i < min_grade):
            min_grade = i
    checkpoints.remove(min_grade)
    return checkpoints


def calcular_media_trabalhos(lista):
    """
    Esta funcao retorna o calculo da media dos trabalhos (checkpoints e Sprints)
    """
    num = 0
    for i in lista:
        num += i / 2
    return num


# def calcular_media_sprints(lista):
#     """
#     Esta funcao retorna o calculo da media dos sprints
#     """
#     num = 0
#     for i in lista:
#         num += i / 2
#     return num 
#     return (s1 + s2) / 2


# def prova_semestral_1(nota):
#     nota * 0.6
#     return nota


def media_semestral_1(media_check, media_sprint, prova_semestral):
    """
    Esta funcao retorna a media total semestral do 1o semestre, onde recebe como parametros, 
    a media dos checkpoints, a media dos sprints e a prova semestral
    """
    media_trabalhos = (media_check + media_sprint) / 2
    media_total = (media_trabalhos + prova_semestral) * 0.4
    return media_total


def media_semestral_2(media_check, media_sprint, prova_semestral):
    """
    Esta funcao retorna a media total semestral do 2o semestre, onde recebe como parametros, 
    a media dos checkpoints, a media dos sprints e a prova semestral
    """
    media_trabalhos = (media_check + media_sprint) / 2
    media_total = (media_trabalhos + prova_semestral) * 0.6
    return media_total


def media_anual(media_semestral_1, media_semestral_2):
    """
    Esta funcao retorna a media total anual
    """
    return (media_semestral_1 + media_semestral_2) / 2


def verificar_nota_valida(nota):
    """
    Esta funcao retorna se a nota digitada é valida
    """
    if nota >= 0 and nota <= 10:
        return True
    else:
        return print("Digite uma nota valida")



def receber_notas_1o_sem():
    """
    Esta funcao recebe todos os dados, e os guarda em variaveis do tipo lista, 
    e tambem solicita a verificacao de outra funcao para validar os dados fornecidos
    """
    lista_ck = []
    lista_sp = []
    listao = []
    if receber_notas_1o_sem:
        ck1 = float(input("Digite o 1o checkpoint do 1o semestre: "))
        if verificar_nota_valida(ck1) == True:
            lista_ck.append(ck1)
        ck2 = float(input("Digite o 2o checkpoint do 1o semestre: "))
        if verificar_nota_valida(ck2) == True:
            lista_ck.append(ck2)
        ck3 = float(input("Digite o 3o checkpoint do 1o semestre: "))
        if verificar_nota_valida(ck3) == True:
            lista_ck.append(ck3)
        sp1 = float(input("Digite o 1o sprint do 1o semestre: "))
        if verificar_nota_valida(sp1) == True:
            lista_sp.append(sp1)
        sp2 = float(input("Digite o 2o sprint do 1o semestre: "))
        if verificar_nota_valida(sp2) == True:
            lista_sp.append(sp2)
        gs1 = float(input("Digite o 1o Global Solution do 1o semestre: "))
        if verificar_nota_valida(gs1) == True:
            listao.append(gs1)

        listao.append(lista_ck)
        listao.append(lista_sp)
    
    return listao


def receber_notas_2o_sem():
    """
    Esta funcao recebe todos os dados, e os guarda em variaveis do tipo lista, 
    e tambem solicita a verificacao de outra funcao para validar os dados fornecidos
    """
    lista_ck = []
    lista_sp = []
    listao = []
    if receber_notas_2o_sem:
        ck1 = float(input("Digite o 1o checkpoint do 2o semestre: "))
        if verificar_nota_valida(ck1) == True:
            lista_ck.append(ck1)
        ck2 = float(input("Digite o 2o checkpoint do 2o semestre: "))
        if verificar_nota_valida(ck2) == True:
            lista_ck.append(ck2)
        ck3 = float(input("Digite o 3o checkpoint do 2o semestre: "))
        if verificar_nota_valida(ck3) == True:
            lista_ck.append(ck3)
        sp1 = float(input("Digite o 1o sprint do 2o semestre: "))
        if verificar_nota_valida(sp1) == True:
            lista_sp.append(sp1)
        sp2 = float(input("Digite o 2o sprint do 2o semestre: "))
        if verificar_nota_valida(sp2) == True:
            lista_sp.append(sp2)
        gs1 = float(input("Digite o 1o Global Solution do 2o semestre: "))
        if verificar_nota_valida(gs1) == True:
            listao.append(gs1)

        listao.append(lista_ck)
        listao.append(lista_sp)
    
    return listao


def verificar_se_passou(media_ano):
    """
    Esta funcao retorna se o aluno foi aprovado ou nao, e em exame tambem
    """
    if media_ano < 4:
        print(f"Voce foi reprovado! Nota: {media_ano}")
    elif media_ano >= 6:
        print(f"Voce foi aprovado!!! Nota: {media_ano}")
    elif media_ano > 4 or media_ano <= 6:
        exame = int(input("Digite a nota de prova de exame: "))
        media_final = (media_ano + exame) / 2
        if media_final >= 6:
            print(f"Aprovado em EXAME! Nota: {media_final}")
        else:
            print(f"Reprovado em EXAME! Nota: {media_final}")



#####################################################################################################
separador("1o Semestre")

lista = []

lista.append(receber_notas_1o_sem())

lista_gs_1o_Sem = lista[0][0]
lista_ck_1o_Sem = lista[0][1]
lista_sp_1o_Sem = lista[0][2]

print(f"Global Solution 1o Semestre: {lista_gs_1o_Sem}")
print(f"Checkpoints 1o Semestre: {lista_ck_1o_Sem}")
print(f"Sprints 1o Semestre: {lista_sp_1o_Sem}")

#checkpoint 1o semestre
nota_ck_1o_Sem = remover_menor_nota(lista_ck_1o_Sem[0], lista_ck_1o_Sem[1], lista_ck_1o_Sem[2])
media_ck_1o_sem = calcular_media_trabalhos(nota_ck_1o_Sem)
print(f"Media Checkpoints 1o semestre = {media_ck_1o_sem:.1f}")

#sprints 1o semestre
media_sp_1o_Sem = calcular_media_trabalhos(lista_sp_1o_Sem)
print(f"Media Sprints 1o semestre = {media_sp_1o_Sem:.1f}")

#Global Solution 1o semestre
nota_gs_1o_sem = lista_gs_1o_Sem

#media 1o semestre
media_total_1o_Sem = media_semestral_1(media_check = media_ck_1o_sem, 
                                       media_sprint = media_sp_1o_Sem, 
                                       prova_semestral = nota_gs_1o_sem)

print(f"Media do primeiro semestre = {media_total_1o_Sem:.1f}")
############################################################
separador("Segundo Semestre")
############################################################
lista_2 = []

lista_2.append(receber_notas_2o_sem())

lista_gs_2o_Sem = lista[0][0]
lista_ck_2o_Sem = lista[0][1]
lista_sp_2o_Sem = lista[0][2]

print(f"Global Solution 2o Semestre: {lista_gs_2o_Sem}")
print(f"Checkpoints 2o Semestre: {lista_ck_2o_Sem}")
print(f"Sprints 2o Semestre: {lista_sp_2o_Sem}")

#checkpoint 2o semestre
nota_ck_2o_Sem = remover_menor_nota(lista_ck_2o_Sem[0], lista_ck_2o_Sem[1], lista_ck_2o_Sem[2])
media_ck_2o_sem = calcular_media_trabalhos(nota_ck_2o_Sem)
print(f"Media Checkpoints 2o semestre = {media_ck_2o_sem:.1f}")

#sprints 2o semestre
media_sp_2o_Sem = calcular_media_trabalhos(lista_sp_2o_Sem)
print(f"Media Sprints 2o semestre = {media_sp_2o_Sem:.1f}")

#Global Solution 2o semestre
nota_gs_2o_sem = lista_gs_2o_Sem

#media 2o semestre
media_total_2o_Sem = media_semestral_2(media_check = media_ck_2o_sem, 
                                       media_sprint = media_sp_2o_Sem, 
                                       prova_semestral = nota_gs_2o_sem)

print(f"Media do segundo semestre = {media_total_2o_Sem:.1f}")


#media anual
media_ano = media_anual(media_total_1o_Sem, media_total_2o_Sem)

print(f"Media Anual: {media_ano:.1f}")

#final
separador("STATUS")

verificar_se_passou(media_ano)


#FIM