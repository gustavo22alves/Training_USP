#NUMEROS ORDENADOS POR TAMANHO

def ordena(lista):
    tamanho = len(lista)

    # Percorre a lista até o penúltimo elemento
    for i in range(tamanho - 1):
        # Encontra o índice do menor elemento restante
        indice_min = i
        for j in range(i + 1, tamanho):
            if lista[j] < lista[indice_min]:
                indice_min = j

        # Troca o elemento atual com o menor elemento restante
        lista[i], lista[indice_min] = lista[indice_min], lista[i]

    return lista