def adiciona_em_ordem(nome, distancia, lista):
    lista_n = []
    lista_n == lista_n.append(nome)
    lista_n == lista_n.append(distancia)

    i = 1
    j = 0
    
    if len(lista) == 0:
        lista.append(lista_n)
    for pais in lista:
        if nome in pais:
            return lista 
    for pais in lista:
        if pais[i] > distancia:
            lista.insert(j,lista_n)
            return lista
        elif pais[i] < distancia:
            lista.insert(j+1,lista_n)
            return lista
        j += 1