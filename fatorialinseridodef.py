# FUNÇÃO DE FATORIAL

def fatorial(n):
    if n == 0:
        return 1
    else:
        return n * fatorial(n - 1)

print(fatorial(5))




# while n >= 0:
#     while n >= 0:
#         fatorial(n)
#         print(fatorial(n))
#         print()
#         n = int(input("Digite um numero: "))
#         if n >= 0:
#             n = n
#         else:
#             n = int(input("Digite um numero maior ou igual a um: !!"))