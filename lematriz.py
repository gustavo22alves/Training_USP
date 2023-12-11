#LEITURA DE MATRIZES

def cria_matriz(n_linhas,n_colunas):
    matriz = []   #lista vazia
    for i in range(n_linhas):
        #cria a linha i
        linha = []  # lista vazia 
        
        for j in range(n_colunas):
        
            valor = int(input("Digite o valor: [" + str(i)+ "][" + str(j)+ "]"))
            linha.append(valor)
            
        matriz.append(linha)
        
        
    return matriz

def dimensoes(matriz):
    linhas = len(matriz)
    colunas = len(matriz[0]) if matriz else 0
    print(f"{linhas}X{colunas}")

# def cria_matriz(num_linhas, num_colunas):
#     matriz = []  #lista vazia
#     for i in range(num_linhas):
#         linha = []
#         for j in range(num_colunas):
#             linha.append(0)
#         matriz.append(linha)

#     for i in range(num_colunas):
#         for j in range(num_linhas):
#             matriz[j][i] = int(input("Digite o elemento [" + str(j) + "][" + str(i) + "]: "))

#     return matriz

def le_matriz():
    lin = int(input('numero linhas: '))
    col = int(input('numero colunas: '))
    return cria_matriz(lin, col)
    
print(le_matriz())

print(dimensoes(le_matriz))






