# CALCULO DE FATORIAL

n = int(input("Digite um número natural: "))
i = 1
fatorial = 1

while i <= n:
    fatorial *= i
    i = i + 1

print(fatorial)

