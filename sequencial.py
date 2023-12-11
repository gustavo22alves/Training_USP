# USANDO BUSCA SEQUENCIAL


# def busca_sequencial(seq, x):
#     ''' (list, float) -> booll '''
#     for i in range(len(seq)):
#         if seq[i] == x: 
#             return True
#     return False


# class Musica:
#     def __init__(self, titulo, interprete, compositor, ano):
#         self.titulo = titulo
#         self.interprete = interprete
#         self.compositor = compositor
#         self.ano = ano
        
# class Buscador:
#     def busca_por_titulo(self, playlist, titulo):
#         for i in range(len(playlist)):
#             if playlist [i].titulo == titulo:
#                 return i
#         return -1
    
#     # def vamos_buscar(self):
#     #     playlist = [Musica('ponta de areia','Milton Nascimento','Milton Nascimento',1955)
#     #                 Musica('podres poderes','Caeteno veloso','caetano veloso',1988)
#     #                 Musica('baby','Gal costa','caetano veloso',1969)]
    
#     # onde_achou = self.busca_por_titulo(playlist, 'baby')

#     # if onde_achou == -1:
#     #     print('Minha musica favorita nao esta na playlist')
#     # else :
#     #     preferida = playlist[onde_achou]
#     #     print(preferida.titulo, preferida.interprete, preferida.compositor, preferida.ano, sep = ', ');

# lista = [1,2,3,4,5,6,7,8,9,10]


def busca(lista, elemento):
    for i in range(len(lista)):
        if lista[i] == elemento:
            return i
    return False

# print(busca(lista,11))










