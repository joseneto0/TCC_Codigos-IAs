def calcular_sequencia(N):
    sequencia = []
    
    while N != 1:
        sequencia.append(N)
        if N % 2 == 0:
            N //= 2
        else:
            N = 3 * N + 1
    
    # Adiciona 1 ao final da sequência
    sequencia.append(1)
    
    return sequencia

# Leitura da entrada
N = int(input().strip())

# Calcula a sequência
sequencia = calcular_sequencia(N)

# Imprime a sequência
for numero in sequencia:
    print(numero)