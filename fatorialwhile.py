#FATORIAL UTILIZANDO WHILE

n = int(input("Digite o valor de n: "))
fatorial = 1
i = 1

while i <= n:
    fatorial *= i
    i = i + 1

print(fatorial)
