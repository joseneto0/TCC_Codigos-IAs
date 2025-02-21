# Leitura do número de pessoas
N = int(input())

# Leitura das prioridades
prioridades = [int(input()) for _ in range(N)]

# Ordenação das prioridades em ordem crescente
prioridades.sort()

# Impressão das prioridades ordenadas
for prioridade in prioridades:
    print(prioridade)
