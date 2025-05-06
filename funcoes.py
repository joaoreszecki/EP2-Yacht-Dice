#Questão 1
import random

def rolar_dados(quantidade):
    dados_rolados = []
    for i in range(quantidade):
        dados = random.randint(1,6)
        dados_rolados.append(dados)
    return dados_rolados

#Questão 2
def guardar_dado(dados_rolados, dados_guardados, indice):
    dado = dados_rolados[indice]
    nova_lista = []
    for i in range(len(dados_rolados)):
        if i != indice:
            nova_lista.append(dados_rolados[i])
    
    dados_guardados.append(dado)
    return [nova_lista, dados_guardados]

#Questão 3
def remover_dado(dados_rolados, dados_guardados, indice):
    dado = dados_guardados[indice]

    nova_lista_guardados = []
    for i in range(len(dados_guardados)):
        if i != indice:
            nova_lista_guardados.append(dados_guardados[i])
    
    dados_rolados.append(dado)
    
    return [dados_rolados, nova_lista_guardados]

#Questão 4
def calcula_pontos_regra_simples(lista_face):
    pontuacoes = {}

    for face in range(1, 7):
        soma = 0
        for dado in lista_face:
            if dado == face:
                soma += dado
        pontuacoes[face] = soma

    return pontuacoes

#Questão 5
def calcula_pontos_soma(lista_face):
    soma = 0
    for valor in lista_face:
        soma += valor
    return soma

#Questão 6
def calcula_pontos_sequencia_baixa(lista_face):
    unicos = []
    for valor in lista_face:
        if valor not in unicos:
            unicos.append(valor)
    
    validos = [
        [1,2,3,4],
        [2,3,4,5],
        [3,4,5,6]
    ]

    for sequencia in validos:
        i = 0
        for numero in sequencia:
            if numero in unicos:
                i += 1
        if i == 4:
            return 15
    return 0

#Questão 7
def calcula_pontos_sequencia_alta(lista_face):
    unicos = []

    for valor in lista_face:
        if valor not in unicos:
            unicos.append(valor)
    validos = [
        [1,2,3,4,5],
        [2,3,4,5,6]
    ]

    for sequencia in validos:
        i = 0
        for numero in sequencia:
            if numero in unicos:
                i += 1
        if i == 5:
            return 30
    return 0

#Questão 8
def calcula_pontos_full_house(lista_face):
    contagem = []

    for i in range(len(lista_face)):
        numero = lista_face[i]
        contador = 0
        for j in range(len(lista_face)):
            if lista_face[j] == numero:
                contador += 1
        if [numero, contador] not in contagem:
            contagem.append([numero, contador])

    tem_3 = False
    tem_2 = False

    for par in contagem:
        if par[1] == 3:
            tem_3 = True
        elif par[1] == 2:
            tem_2 = True

    if tem_3 and tem_2:
        soma = 0
        for valor in lista_face:
            soma += valor
        return soma

    return 0