# FUNÇÃO É PRIMO OU NÃO

def eprimo(n):
    fator = 2
    if n == 2:
        return True
    while n % fator != 0 and fator <= n/2:
        fator = fator + 1
    if n % fator == 0:
        return False
    else:
        return True

n = int(input("n: "))

while n > 0:
    if eprimo(n):
        print(n,"é primo")
    else:
        print(n,"não é primo")
    n = int(input("n: "))
