# VALOR DIVISIVEL POR 3

numero = int(input("Digite um número: "))

calculo = numero % 3
if calculo == 0:
    print("DIVISÍVEL")
else:
    print(f'NÃO DIVISÍVEL: {numero}')

