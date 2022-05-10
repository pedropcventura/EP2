import random
def sorteia_pais(dic_paises):
    lista = []
    for paises, dados in dic_paises.items():
        lista.append(paises)
    return random.choice(lista)