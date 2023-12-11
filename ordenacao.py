# FUNÇÃO PARA ORDENAR NÚMEROS ALEATÓRIOS

lista = [6,4,7,3,2,7,8,454,3,567,3434,7875]

class ordenador:
    def selecao_direta(self, lista):

        fim = len (lista)

        for i in range(fim - 1):
            #  INICIALEMENTE, O MENOR ELEMENTO JA VISTO É O I-ÉSIMO
            posicao_do_minimo = i

            for j in range(i + 1, fim):
                if lista[j] < lista[posicao_do_minimo]:
                    posicao_do_minimo = j

            # COLOCA O MENOR ELEMENTO ENCONTRADAO NO INICIO DA SUBLISTA
            # PARA ISSO, TROCA DE LUGAR OS ELEMENTOS NAS POSIÇOES I E  POSIÇAO MINIMO.
            lista[i], lista[posicao_do_minimo] = lista[posicao_do_minimo], lista[i]
