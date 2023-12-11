# def eprimo(n):
#     fator = 2
#     if n == 2:
#         return True
#     while n % fator != 0 and fator <= n/2:
#         fator = fator + 1
#     if n % fator == 0:
#         return False
#     else:
#         return True

# limite = int(input("Limite máximo: "))

# n = 2
# while n < limite:
#     if eprimo(n):
#         print(n, end = ", ")
#     n = n + 1

primos = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47,]

# print(primos[1:2])
# print(primos[1:5])
# print(primos[:12])
# print(primos[12:])
final = primos[12:]

# print(primos)
# print(final)

lista1 = ['vermelho','verde','azul']
lista2 = lista1

lista2[0] = "rosa"

print(lista2)

# def clone(lista):
#     clone = []
#     for objeto in lista;
#         clone.append(objeto)
# #     return clone

# lista2 = lista1[:]
# lista2[0] = "vermelho"

# print(lista2)

# print("rosa" in lista2)

# if 'rosa' in lista2:
#     print("esta")
# else:
#     print('nao esta')

a = [1,2,3,4,5,6,4,5,6]
b = [5,6,4,8,7,5,3,2,4,5]

# print(a + b)
# print(a +b + a)
# a.append('gato')
# print(a)

# b = a + [5]
# print(b)

# triplicado = a * 3

# print(triplicado)

# print(len(triplicado))
print(a)
del a[1]
print(a)
del a[1:3]
print(a)








