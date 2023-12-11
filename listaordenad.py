# ORDENAÇÃO DE LISTA

lista = [10,10,25,25,30,8,5,6,7,10,16,8,5,90,54,54,58,35]

print(sorted(lista))

print(lista)

lista.sort()

print(lista)

def remove_repetidos(lista):
    lista_sem_repetidos = list(set(lista))  # Remove elementos duplicados usando um conjunto
    lista_sem_repetidos.sort()  # Ordena a lista sem repetições
    return lista_sem_repetidos

print(remove_repetidos(lista))








