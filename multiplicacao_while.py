# UTILIZAÇÃO DE WHILE

tamanho = int(input("Digite o tamanho da sequencia de numeros: "))

produto  = 1
i = 0

while i < tamanho:
    valor = int(input("Digite um valor a ser multiplicado: "))
    produto = produto * valor
    i = i + 1

print("A produto do valores digitados é:",produto)
    
