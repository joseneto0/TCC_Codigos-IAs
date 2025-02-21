# Leitura do tamanho do mapa
N = int(input())

# Inicialização do mapa
mapa = []

# Leitura do mapa
for _ in range(N):
    linha = input()
    mapa.append(linha)

# Função para contar as bombas ao redor de uma posição
def contar_bombas(i, j):
    contagem = 0
    for x in range(-1, 2):
        for y in range(-1, 2):
            if x == 0 and y == 0:
                continue
            if i + x < 0 or i + x >= N or j + y < 0 or j + y >= N:
                continue
            if mapa[i + x][j + y] == '*':
                contagem += 1
    return contagem

# Processamento do mapa
for i in range(N):
    for j in range(N):
        if mapa[i][j] == '*':
            print('9', end='')
        else:
            print(contar_bombas(i, j), end='')
    print()
