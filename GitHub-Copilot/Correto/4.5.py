def calcular_alertas_de_minas(N, mapa):
    # Inicializar a matriz de saída com zeros
    resultado = [[0] * N for _ in range(N)]
    
    # Direções para as células vizinhas (incluindo diagonais)
    direcoes = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    
    for i in range(N):
        for j in range(N):
            if mapa[i][j] == '*':
                resultado[i][j] = 9
                # Atualizar as células vizinhas
                for di, dj in direcoes:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < N and 0 <= nj < N and mapa[ni][nj] != '*':
                        resultado[ni][nj] += 1
    
    return resultado

# Leitura da entrada
N = int(input().strip())
mapa = [input().strip() for _ in range(N)]

# Calcular a matriz de alertas de minas
resultado = calcular_alertas_de_minas(N, mapa)

# Imprimir o resultado
for linha in resultado:
    print("".join(map(str, linha)))