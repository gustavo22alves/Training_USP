# FUNÇÃO PARA DESCOBRIR QUAL É O NOME MAIS CURTO

# escreva uma funçao que recebe uma 
# lista de strings contendo nomes de pessoas
# como parametro e devolva o nome mais curto.
# a funçao deve ignorar espaços antes de depois do nome 
# e deve devolver nome 'capitalizado', i.e. ,
# apenas com a primeira letra maiuscula'

nomes = ['ana','gustavo','matheus','custodio','daguilar','ba']

def mais_curto(nomes):
    for nome in nomes:
        nome = nome.strip()
        nome = nome.capitalize()

        if nome is None or len(nome) < len(nomes):
            nomes = nome
    return nomes

print(mais_curto(nomes))
