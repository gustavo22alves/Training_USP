# INSERTION SORT

def insertion_sort(lista):
    # Percorre a lista a partir do segundo elemento
    for i in range(1, len(lista)):
        chave = lista[i]
        j = i - 1

        # Move os elementos maiores que a chave para a direita
        while j >= 0 and lista[j] > chave:
            lista[j + 1] = lista[j]
            j -= 1

        # Insere a chave na posição correta
        lista[j + 1] = chave

    return lista