# alfabeto = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

# print(len(alfabeto))
# print(alfabeto[13:])
# print(alfabeto[0:13])
# letras = alfabeto[1:10]
# print(letras)
# letras = alfabeto[:]
# print(letras)
# print(alfabeto[:13])
# print(alfabeto[13:27])

# carnes = ["picanha", "alcatra", "filé mignon", "cupim"]
# carnes2 = carnes
# carnes2.append("ponta de alcatra")

# print(carnes)
# print(carnes2)

# carnes = ["picanha", "alcatra", "filé mignon", "cupim"]
# carnes2 = []
# for cns in carnes:
#     carnes2.append(cns)
# carnes2.append("ponta de alcatra")

carnes = ["picanha", "alcatra", "filé mignon", "cupim"]
carnes2 = carnes[:]
carnes2.append("ponta de alcatra")

print(carnes)
print(carnes2)
