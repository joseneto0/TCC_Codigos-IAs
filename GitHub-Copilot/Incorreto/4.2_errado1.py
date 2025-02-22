def simplificar_matriz(N, matriz):
    matriz_simplificada = []
    contagem = {'+': 0, 'o': 0, '-': 0}
    
    for i in range(N):
        linha_simplificada = ''
        for j in range(N):
            goblins = matriz[i][j]
            if goblins <= 90:
                linha_simplificada += '+'
                contagem['+'] += 1
            elif goblins > 110:
                linha_simplificada += '-'
                contagem['-'] += 1
            else:
                linha_simplificada += 'o'
                contagem['o'] += 1
        matriz_simplificada.append(linha_simplificada)
    
    return matriz_simplificada, contagem

# Leitura da entrada
N = int(input().strip())
matriz = [list(map(int, input().strip().split())) for _ in range(N)]

# Processar a matriz
matriz_simplificada, contagem = simplificar_matriz(N, matriz)

# Imprimir a matriz simplificada
for linha in matriz_simplificada:
    print(linha)
print()

# Imprimir a contagem dos símbolos
for simbolo in ['+', 'o', '-']:
    print(f"{simbolo}: {contagem[simbolo]}")