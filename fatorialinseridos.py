# FUNÇÃO DE FATORIAL POREM COM INSERÇÃO DE N

n = int(input("Digite um numero inteiro positivo: "))
  
while n >= 0:
    fatorial = 1
    while n > 1:
        fatorial = fatorial * n
        n = n - 1
    print(fatorial)
    print() 
    n = int(input("Digite um numero inteiro positivo: "))
    if n >= 0:
        n = n
    else:
        n = int(input("Digite um numero maior ou igual a um: !!"))
        
