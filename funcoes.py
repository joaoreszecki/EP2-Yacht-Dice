import random

def rolar_dados(quantidade):
    dados_rolados = []
    for i in range(quantidade):
        dados = random.randint(1,6)
        dados_rolados.append(dados)
    return dados_rolados