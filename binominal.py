#CALCULADORA FATORIAL

def calcular_fatorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        fatorial = 1
        for i in range(2, n + 1):
            fatorial *= i
        return fatorial

numero1 = int(input("Digite um número inteiro: "))
numero2 = int(input("Digite um outro número inteiro: "))
numero3 = int(numero1 - numero2)

resultado1 = calcular_fatorial(numero1)
resultado2 = calcular_fatorial(numero2)
resultado3 = calcular_fatorial(numero3)
calculo_binominal = resultado1/(resultado2*resultado3)

print(calculo_binominal)





