# IMPRIMIR ORDEM INVERSA

def imprimir_inverso():
    numeros = []
    numero = 1
    if numero > 0: 
        while True:
            numero = input("Digite um número inteiro (ou 'fim' para encerrar): ")
            if numero == 0:
                break
            numeros.append(int(numero))

    else:
        print("Valores em ordem inversa:")
        for i in range(len(numeros) - 1, -1, -1):
            print(numeros[i])

imprimir_inverso()