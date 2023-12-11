# LISTA INVERSO

lista = []
numero = 1
while numero > 0:
    numero = int(input('Digite um número: '))
    if numero > 0:
        lista.append(numero)
else:
    numero = 0
    for i in range(len(lista) - 1, -1, -1):
            print(lista[i])



