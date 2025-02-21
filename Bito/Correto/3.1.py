# Lendo o número de pessoas
N = int(input())

# Inicializando a lista para armazenar as prioridades
prioridades = []

# Lendo as prioridades
for _ in range(N):
    prioridade = int(input())
    prioridades.append(prioridade)

# Ordenando as prioridades em ordem crescente
prioridades.sort()

# Imprimindo as prioridades ordenadas
for prioridade in prioridades:
    print(prioridade)