# Função para contar minas ao redor de uma posição
def contar_minas(mapa, i, j, N):
    contagem = 0
    # Verificamos as 8 direções ao redor da posição (i, j)
    for di in [-1, 0, 1]:
        for dj in [-1, 0, 1]:
            if di == 0 and dj == 0:
                continue  # Ignorar a própria posição
            ni, nj = i + di, j + dj
            if 0 <= ni < N and 0 <= nj < N and mapa[ni][nj] == '*':
                contagem += 1
    return contagem

# Lendo o tamanho do mapa
N = int(input())

# Lendo o mapa
mapa = [input().strip() for _ in range(N)]

# Criando o mapa de saída
resultado = []
for i in range(N):
    linha_resultado = ""
    for j in range(N):
        if mapa[i][j] == '*':
            linha_resultado += '9'
        else:
            contagem = contar_minas(mapa, i, j, N)
            linha_resultado += str(contagem)
    resultado.append(linha_resultado)

# Imprimindo o resultado
for linha in resultado:
    print(linha)