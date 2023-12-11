# IMPRIMIR MATRIZ

matriz = [[1],[2],[3]]

def imprime_matriz(matriz):
    for linha in matriz:
        for i in range(len(linha)):
            if i == len(linha) - 1:
                print(linha[i], end="")
            else:
                print(linha[i], end=" ")
        print()

print(imprime_matriz(matriz))
