import random

def rolar_dados(quantidade):
    dados_rolados = []
    for i in range(quantidade):
        dados = random.randint(1,6)
        dados_rolados.append(dados)
    return dados_rolados

def guardar_dado(dados_rolados, dados_guardados, indice):
    dado = dados_rolados[indice]
    nova_lista = []
    for i in range(len(dados_rolados)):
        if i != indice:
            nova_lista.append(dados_rolados[i])
    
    dados_guardados.append(dado)
    return [nova_lista, dados_guardados]

def remover_dado(dados_rolados, dados_guardados, indice):
    dado = dados_guardados[indice]

    nova_lista_guardados = []
    for i in range(len(dados_guardados)):
        if i != indice:
            nova_lista_guardados.append(dados_guardados[i])
    
    dados_rolados.append(dado)
    
    return [dados_rolados, nova_lista_guardados]

def calcula_pontos_regra_simples(lista_face):
    pontuacoes = {}

    for face in range(1, 7):
        soma = 0
        for dado in lista_face:
            if dado == face:
                soma += dado
        pontuacoes[face] = soma

    return pontuacoes

def calcula_pontos_soma(lista_face):
    soma = 0
    for valor in lista_face:
        soma += valor
    return soma

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