import random

def sorteia_letra(palavra, restrita):
    lista = []
    especiais = ['.', ',', '-', ';', ' ']
    for character in palavra:
        character = character.lower()
        if character not in restrita and character not in especiais:
            lista.append(character)
    if len(lista) == 0:
        return ''
    return random.choice(lista)