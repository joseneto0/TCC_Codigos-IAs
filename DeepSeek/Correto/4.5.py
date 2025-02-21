def criar_mapa_minas(N, mapa):
    # Direções para verificar as 8 posições vizinhas
    direcoes = [(-1, -1), (-1, 0), (-1, 1),
                (0, -1),          (0, 1),
                (1, -1),  (1, 0), (1, 1)]

    # Cria o mapa de minas
    mapa_minas = [[0 for _ in range(N)] for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if mapa[i][j] == '*':
                mapa_minas[i][j] = 9
            else:
                # Conta as minas ao redor
                contagem = 0
                for di, dj in direcoes:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < N and 0 <= nj < N and mapa[ni][nj] == '*':
                        contagem += 1
                mapa_minas[i][j] = contagem

    # Imprime o mapa de minas
    for linha in mapa_minas:
        print(''.join(map(str, linha)))

# Leitura da entrada
N = int(input())
mapa = [input().strip() for _ in range(N)]

# Criação do mapa de minas
criar_mapa_minas(N, mapa)