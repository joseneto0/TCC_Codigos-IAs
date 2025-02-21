def contar_minas(mapa):
    n = len(mapa)
    resultado = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if mapa[i][j] == '*':
                # Marca as posições adjacentes (incluindo diagonais)
                for x in range(max(0, i - 1), min(n, i + 2)):
                    for y in range(max(0, j - 1), min(n, j + 2)):
                        if mapa[x][y] == '*':
                            resultado[x][y] += 1

    # Substitui os asteriscos por 9
    for i in range(n):
        for j in range(n):
            if mapa[i][j] == '*':
                resultado[i][j] = 9

    # Imprime o resultado
    for linha in resultado:
        print(''.join(map(str, linha)))

# Leitura da entrada
n = int(input())
mapa = []
for _ in range(n):
    linha = list(input())
    mapa.append(linha)

# Chama a função para contar as minas
contar_minas(mapa)