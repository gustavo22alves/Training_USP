# CONTADOR DE LINHAS E COLUNAS DE UMA MATRIZ

def dimensoes(matriz):
    linhas = len(matriz)
    colunas = len(matriz[0]) if matriz else 0
    print(f"{linhas}X{colunas}")

# # Exemplo de uso:
# minha_matriz = [[1, 2, 3],[4,5,6]]
# dimensoes(minha_matriz)  #