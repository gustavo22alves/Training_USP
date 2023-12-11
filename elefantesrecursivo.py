#RESOLUÇÃO NÚMERO UM

def incomodam(n):
    if not isinstance(n, int) or n <= 0:
        return ""
    elif n == 1:
        return "incomodam "
    else:
        return "incomodam " + incomodam(n - 1)

def elefantes(n):
    if not isinstance(n, int) or n == 0:
        return ""
    elif n == 1:
        return "Um elefante incomoda muita gente\n"
    else:
        frase_anterior = elefantes(n - 1)
        frase_atual = f"{n} elefantes {incomodam(n)}muito mais\n"
        proxima_frase = f"{n} elefantes incomodam muita gente\n"
        return frase_anterior + frase_atual + proxima_frase
 


# RESOLUÇÃO NÚMERO DOIS

def incomodam(n: int) -> str:
    # RETORNA UMA STRING CONTENDO A PALAVRA "INCOMODAM" n VEZES
    mstr = ""

    if n > 0:
        mstr += "incomodam "
        return mstr + incomodam(n-1)

    return mstr


def elefantes(n: int, max=None) -> str:
    # DEVOLVE UMA STRING COM A LETRA DA MÚSICA
      
    if not max:
        max, n = n, 2

    if n <= max:
        if n == 2:
            mstr = "Um elefante incomoda muita gente\n"
            mstr += "{} elefantes {}muito mais\n".format(n, incomodam(n))
        else:
            mstr = "{} elefantes {}muito mais\n".format(n, incomodam(n))

        if n < max:
            mstr += "{} elefantes incomodam muita gente\n".format(n)

        return mstr + elefantes(n+1, max)

    return ""

print(elefantes(n=10))