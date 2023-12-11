# SEQUENCIA DE FIBONACCI

def fibonacci(n):
    fib_sequence = [0, 1]
    
    while len(fib_sequence) < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    
    return fib_sequence[:n]

n = 10
resultado = fibonacci(n)
print(f"Sequência de Fibonacci até o {n}-ésimo termo: {resultado}")

    