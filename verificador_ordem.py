# VERIFICA SE A LISTA ESTA EM ORDEM

lista = [1,2,3,4,5,6,7,8,9]
lista1 = [1,3,4,5,2,7,8,9,12,11,10]

def ordenada(lista):
    for i in range(len(lista) - 1):
        if lista[i] > lista[i + 1]:
            return False
    return True

print(ordenada(lista))
print(ordenada(lista1))