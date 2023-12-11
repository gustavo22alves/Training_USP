# CONTADOR DE VOGAIS EM UMA FRASE

def conta_letras(frase, contar="vogais"):
    if contar == "vogais":
        vogais = "aeiouAEIOU"
        contador = sum(1 for letra in frase if letra in vogais)
    elif contar == "consoantes":
        consoantes = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
        contador = sum(1 for letra in frase if letra in consoantes)
    else:
        raise ValueError("O parâmetro 'contar' deve ser 'vogais' ou 'consoantes'.")
    return contador

escrito = 'Quero ser rico, rico de felicidade'

print(conta_letras(escrito))