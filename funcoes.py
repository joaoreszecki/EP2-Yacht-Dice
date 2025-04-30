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