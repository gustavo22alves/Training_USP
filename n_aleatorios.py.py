# CRIA QUANTIDADE ALEATORIA DE NUMEROS

import random
def lista_grande(n):
    lista = []
    for _ in range (n):
        numero = random.randint(1,100)
        lista.append(numero)
    return lista
