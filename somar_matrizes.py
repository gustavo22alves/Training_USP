# SOMANDO MATRIZES

# m1 = [[1,2],[3,4],[5,6]]
# m2 = [[1,2],[5,6]]

def soma_matrizes(m1, m2):
    if len(m1) != len(m2) or len(m1[0]) != len(m2[0]):
        return False
    
    resultado = []
    for i in range(len(m1)):
        linha = []
        for j in range(len(m1[0])):
            soma = m1[i][j] + m2[i][j]
            linha.append(soma)
        resultado.append(linha)
    
    return resultado

# print(soma_matrizes(m1,m2))
