# Função para contar as minas ao redor de uma célula
def contar_minas(mapa, i, j, N):
    count = 0
    # Vizinhanças para 8 direções possíveis (cima, baixo, esquerda, direita e 4 diagonais)
    for di in [-1, 0, 1]:
        for dj in [-1, 0, 1]:
            # Evita contar a célula central ou posições fora do mapa
            if di == 0 and dj == 0:
                continue
            ni, nj = i + di, j + dj
            # Verifica se a célula está dentro dos limites do mapa
            if 0 <= ni < N and 0 <= nj < N:
                if mapa[ni][nj] == '*':  # Se encontrar uma mina, conta
                    count += 1
    return count

# Leitura da entrada
N = int(input())  # Lê o tamanho do mapa
mapa = [input().strip() for _ in range(N)]  # Lê o mapa linha por linha

# Matriz para armazenar a saída
resultado = []

# Processamento de cada célula do mapa
for i in range(N):
    linha_resultado = ""
    for j in range(N):
        if mapa[i][j] == '*':  # Se for barril, coloca 999
            linha_resultado += "999"
        else:
            # Se não for barril, conta as minas ao redor
            minas = contar_minas(mapa, i, j, N)
            linha_resultado += str(minas)
    resultado.append(linha_resultado)

# Impressão da saída
for linha in resultado:
    print(linha)