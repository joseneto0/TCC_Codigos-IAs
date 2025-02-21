# Lendo o valor inicial de N
N = int(input())

# Inicializando a lista para armazenar a sequência
sequencia = []

# Gerando a sequência
while N != 1:
    sequencia.append(N)
    if N % 2 == 0:
        N = N // 2  # Se N é par
    else:
        N = 3 * N + 1  # Se N é ímpar

# Adicionando o último valor (1) à sequência
sequencia.append(1)

# Imprimindo a sequência
for numero in sequencia:
    print(numero)