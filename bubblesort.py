#ORDENA PALAVRAS EM ORDEM ALFABETICA

def bubble_sort(lista):
    n = len(lista)
    
    #ITERA POR TODA A LISTA
    for i in range(n - 1):
        # ULTIMOS i ELEMENTOS JA ESTAO NO LUGAR CERTO
        for j in range(n - 1 - i):
            # COMPARAR ELEMENTOS ADJACENTES
            if lista[j] > lista[j + 1]:
                # TROCAR ELEMENTOS DE POSIÇÃO
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                # IMPRIMIR O ESTADO ATUAL DA LISTA
                print(lista)
    
    return lista


lista = ['carro','arroz','feijao','abacate','laranja']
print(bubble_sort(lista))

