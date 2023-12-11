def contar_dezenas(numero):
    # VERIFICA SE O NÚMERO É INTEIRO
    if not isinstance(numero, int):
        raise ValueError("O argumento deve ser um número inteiro")

    # CALCULA A QUANTIDADE DE DEZENAS
    quantidade_dezenas = abs(numero) // 10

    return quantidade_dezenas

def main():
    try:
        # SOLICITA AO USUÁRIO UM NUMERO INTEIRO
        numero_informado = int(input("Digite um número inteiro: "))
        # CHAMA A FUNÇÃO PRA REALIZAR O CALCULO
        resultado = contar_dezenas(numero_informado)
        # EXIBE O RESULTADO
        print(f"O número {numero_informado} contém {resultado} dezenas.")
    except ValueError as ve:
        print(ve)

# CHAMA A FUNÇÃO PRINCIPAL
if __name__ == "__main__":
    main()
