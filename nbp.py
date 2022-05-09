def normaliza(dicionario):
    novo_dic = {}
    for cont, paises in dicionario.items():
        for pais, dados in paises.items():
            novo_dic[pais] = dados
            novo_dic[pais]["continente"] = cont
    return novo_dic