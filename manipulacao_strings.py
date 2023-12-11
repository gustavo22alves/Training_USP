# MANIPULAÇÃO DE STRINGS

'amora'
"amora"

print(type('amora'))
print('legal ' * 3)

time = 'Corinthians'

print(time.upper())
print(time.lower())

print('ana gosta de banana'.capitalize())
print('BRASIL'.capitalize())
print('    gustavodeoliveira_sj@hotmail.com    '.strip()) # remove espacos
print('ana gosta de banana'.count('a')) # quantas x a letra aparece
print('ana gosta de banana'.count('n'))

#troca uma parte do string
print('eu torço para o corinthians'.replace('corinthians','sao paulo'))

#centraliza e tambem pode concatenar as mesmas
print('ana gosta de banana'.capitalize().center(50))

texto = 'minha terra tem palmeiras onde o mar goljeia'

#encontrar caracteris na string
print(texto.find('m'))
print(texto.find('ma'))
print(texto.find('bom')) #nao tem na string

fruta = 'amora'

print(fruta[:4])
print(fruta[:1])
print(fruta[2:4])













