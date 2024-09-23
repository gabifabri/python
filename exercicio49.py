def fibonacci(n):
    """
    Calcula a série de Fibonacci até o n-ésimo termo.
    """
    if n <= 0:
        return []
    elif n == 1:
        return [1]
    else:
        fib_list = [1, 1]
        while len(fib_list) < n:
            next_fib = fib_list[-1] + fib_list[-2]
            fib_list.append(next_fib)
        return fib_list

# Exemplo de uso:
n = 10
print(f"Série de Fibonacci até o {n}-ésimo termo: {fibonacci(n)}")