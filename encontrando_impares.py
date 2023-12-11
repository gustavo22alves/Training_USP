# ENCONTRANDO IMPARES

lista = [1,2,3,4,5,6,8,7,9,10]

# def soma_lista(lista):
#     if not lista:
#         return 0
#     else:
#         return lista[0] + soma_lista(lista[1:])

# # print(soma_lista(lista))

def encontra_impares(lista):
    if not lista:
        return []  # Lista vazia, retorna uma lista vazia

    if lista[0] % 2 != 0:
        return [lista[0]] + encontra_impares(lista[1:])  # Adiciona o número ímpar e chama a função recursivamente para o restante da lista
    else:
        return encontra_impares(lista[1:])  # Chama a função recursivamente para o restante da lista

# print(encontra_impares(lista))

