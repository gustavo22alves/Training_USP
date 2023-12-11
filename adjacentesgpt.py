#FUNÇÃO PARA ENCONTRAR NUMEROS ADJACENTES 

def encontrar_numeros_adjacentes(sequencia):
    for i in range(len(sequencia) - 1):
        if sequencia[i] == sequencia[i + 1]:
            return sequencia[i], sequencia[i + 1]
    return None

# EXEMPLO DE USO

numeros = [1, 2, 3, 4, 5, 5, 6]
resultado = encontrar_numeros_adjacentes(numeros)

if resultado:
    print(f"Os números adjacentes são: {resultado[0]} e {resultado[1]}")
else:
    print("Não foram encontrados números iguais adjacentes.")