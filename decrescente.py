# IDENTIFICADOR DE VALOR CRESCENTE

decrescente = True
anterior = int(input("Digite o primeiro número: "))
valor = 1

while valor != 0 and decrescente:
    valor = int(input("Digite o próximo valor: "))
    if valor > anterior:
        decrescente = False
    anterior = valor

if decrescente:
    print("A sequência está em valor decrescente, parabéns... !!")
else:   
    print("Ops valor está em valor crescente agora...")

