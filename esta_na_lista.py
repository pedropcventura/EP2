def esta_na_lista(nome, lista):
    i = 0
    for pais in lista:
        if nome == pais[0]:
            return True
    else:
        return False