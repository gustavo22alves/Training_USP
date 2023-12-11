# FUNÇÃO DE FATORIAL RECURSIVO

def fatorial(n):
    if n < 1: # BASE RECURSIVA
        return 1
    else:
        return n * fatorial(n-1) #CHAMADA RECURSIVA

import pytest


@pytest.mark.parametrize('entrada, esperado' ,[
    (0,1),
    (1,1),
    (2,2),
    (3,6),
    (4,24),
    (5,120), 
])

def testa_fatorial(entrada, esperado):
    assert fatorial(entrada) == esperado