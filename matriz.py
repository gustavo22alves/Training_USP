def criar_matriz(n_linhas,n_colunas,valor):
    matriz = []
    for i in range(n_linhas):
        
        linha = []
        
        for j in range(n_colunas):
        
            linha.append(valor)
        
        matriz.append(linha)
        
        
    return matriz

x = int(input('numero linhas: '))
y = int(input('numero colunas: '))
z = int(input('numero valor: '))

print(criar_matriz(x,y,z))

