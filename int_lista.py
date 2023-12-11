# INTRODUÇÃO A LISTAS

aluno = ["Fulano de Tal", 25, "Rua xyz, 123", "São Paulo", 3, "Matemática", 7.5, "Português", 6.6, "Artes", 10]

print(type(aluno[-1]))
print(type(aluno[4]))
print(len(aluno))
aluno[1] = aluno[1] + 1
print(aluno)


flores = ["margarida", "rosa", "tulipa", "cravo"]
tam = len(flores) - 1
while tam >= 0:
    print(flores[tam], end=", ")
    tam = tam - 1
