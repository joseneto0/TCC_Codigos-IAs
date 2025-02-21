def calcular_sequencia(N):
    count = 1  # Começa com 1 para contar o número inicial
    while N > 1:
        N = N // 2  # Dividir por 2 e descartar a parte decimal
        count += 1  # Incrementar o contador
    return count

# Entrada
N = int(input())

# Saída
print(calcular_sequencia(N))