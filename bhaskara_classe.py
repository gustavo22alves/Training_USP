#CALCULO DE BHASKARA (CLASSE)

import math

class Bhaskara:
    
    #CALCULO DELTA DE BHASKARA
    def delta(self, a , b , c):
        return b ** 2 - 4 * a * c
    
    #PRIMEIRA A FUNCIONAR E POSTERIORMENTE SEGUE
    def main(self):  
        a_digitado = float(input('DIGITE O VALOR DE A: '))
        b_digitado = float(input('DIGITE O VALOR DE B: '))
        c_digitado = float(input('DIGITE O VALOR DE C: '))
        print(self.calcula_raizes(a_digitado, b_digitado, c_digitado))
        
    #CÁLCULO DAS RAÍZES
    def calcula_raizes(self , a , b , c):
        d = self.delta(a , b , c)
        if d == 0:
            raiz1 = (- b + math.sqrt(d)) / (2 * a)
            return 1, raiz1
        else:
            if d < 0:
                return 0
            else:
                raiz1 = (- b + math.sqrt(d)) / (2 * a)
                raiz2 = (- b - math.sqrt(d)) / (2 * a)
                return 2, raiz1, raiz2
            


