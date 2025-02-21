# Leitura do tamanho da matriz
N = int(input())

# Inicialização da matriz
matriz = []

# Leitura da matriz
for _ in range(N):
    linha = list(map(int, input().split()))
    matriz.append(linha)

# Inicialização da contagem de símbolos
contagem = {'+': 0, 'o': 0, '-': 0}

# Processamento da matriz
for i in range(N):
    for j in range(N):
        if matriz[i][j] <= 100:
            print('+', end='')
            contagem['+'] += 1
        elif matriz[i][j] <= 110:
            print('o', end='')
            contagem['o'] += 1
        else:
            print('-', end='')
            contagem['-'] += 1
    print()

print()

# Impressão da contagem de símbolos
for simbolo, quantidade in contagem.items():
    print(f"{simbolo}: {quantidade}")