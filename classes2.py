#EXEMPLO DE UTILIZAÇÃO DE CLASSES

# class Cachorro:
#   def __init__(self, raça, idade, nome, cor):
#     self.raça = raça
#     self.idade = idade
#     self.nome = nome
#     self.cor = cor
    
# rex = Cachorro('vira-lata', 2, 'Bobby', 'marrom')

# print(rex.idade)
# print(rex.raça)
# print(rex.cor)
# print(rex.nome)


class Lista:
  def append(self, elemento):
    return "Oops! Este objeto não é uma lista"
    
lista = []

a = Lista()
b = a.append(7)

lista.append(b)

print(lista)
