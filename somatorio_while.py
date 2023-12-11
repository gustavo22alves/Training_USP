#CALCULADORA UTILIZANDO WHILE

print("Digite uma sequencia de valores terminada em zero.")
soma = 0
valor  = 1

while valor != 0:
    valor = int(input("Digite um valor: "))
    soma = soma + valor
    print(f'A soma dos valores digitados são:{soma}')
    



