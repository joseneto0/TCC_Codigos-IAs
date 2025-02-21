def analisar_matriz(N, matriz):
    matriz_simplificada = []
    contagem = {'+': 0, 'o': 0, '-': 0}

    for i in range(N):
        linha_simplificada = []
        for j in range(N):
            goblins = matriz[i][j]
            if goblins <= 100:
                if goblins + 10 <= 100:
                    linha_simplificada.append('+')
                    contagem['+'] += 1
                else:
                    linha_simplificada.append('o')
                    contagem['o'] += 1
            else:
                linha_simplificada.append('-')
                contagem['-'] += 1
        matriz_simplificada.append(linha_simplificada)

    # Imprime a matriz simplificada
    for linha in matriz_simplificada:
        print(''.join(linha))

    # Imprime a contagem
    print()
    for simbolo, quantidade in contagem.items():
        print(f"{simbolo}: {quantidade}")

# Leitura da entrada
N = int(input())
matriz = [list(map(int, input().split())) for _ in range(N)]

# Análise da matriz
analisar_matriz(N, matriz)