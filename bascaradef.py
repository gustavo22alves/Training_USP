#FORMULA DE BHASKARA

import math

a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))

def raizes (a , b , c):
    delta = (b**2) - (4*a*c)   
    
    if delta < 0:
        return "A equação não possui raízes reais."
    elif delta == 0:
        x = -b / (2*a)
        return "A equação possui uma raiz real: x = {}".format(x)
    else :
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)
        return "A equação possui duas raízes reais: x1 = {}, x2 = {}".format(x1, x2)

resultado = raizes(a, b, c)
print(resultado)








