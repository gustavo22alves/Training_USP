# MULTIPLICAÇÃO EM MATRIZES


# A = [[1,2,3],[4,5,6]]
# B = [[1,2,],[4,5],[6,7]]


def mat_mul(A, B):
    num_linhas_A, num_colunas_A = len(A), len(A[0])
    num_linhas_B, num_colunas_B = len(B), len(B[0])
    assert num_linhas_A == num_colunas_B

    C = []
    for linha in range(num_linhas_A):
    #  COMEÇANDO UMA NOVA LINHA
        C.append([])
        for coluna in range(num_colunas_B):
        #  ADICIONANDO UMA NOVA COLLUNA NA LINHA
            C[linha].append(0)
            for k in range(num_colunas_A):
                C[linha][coluna] += A[linha][k] * B[k][coluna]
    return C
# print(mat_mul(A, B))



