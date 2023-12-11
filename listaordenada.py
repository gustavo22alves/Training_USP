#LISTA ORDENADA 2

lista = []

def remove_repetidos(lista):
    lista_sem_repetidos = list(set(lista))  # Remove elementos duplicados usando um conjunto
    lista_sem_repetidos.sort()  # Ordena a lista sem repetições
    return lista_sem_repetidos

print(remove_repetidos(lista))