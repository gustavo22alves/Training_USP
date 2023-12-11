# IMPARES

n = int(input("Digite um número inteiro positivo: "))
contador = 1
impares = 0

while impares < n:
    if contador % 2 != 0:
        print(contador)
        impares += 1

    contador += 1