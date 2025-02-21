# Lendo a entrada
N = int(input())  # tamanho da matriz
matrix = [list(map(int, input().split())) for _ in range(N)]

# Inicializando as variáveis de contagem
count_plus = 0
count_o = 0
count_minus = 0

# Matriz simplificada e contagem
simplified_matrix = []

for row in matrix:
    simplified_row = []
    for value in row:
        if value > 100:
            simplified_row.append('-')
            count_minus += 1
        elif value <= 100:  # valor <= 100, sempre possível entrar
            simplified_row.append('+')
            count_plus += 1
        else:  # Se o valor estiver entre 101 e 199 (considerando K-Ôru)
            simplified_row.append('o')
            count_o += 1
    simplified_matrix.append(simplified_row)

# Imprimir a matriz simplificada
for row in simplified_matrix:
    print(''.join(row))

# Imprimir a contagem
print()
print(f'+: {count_plus}')
print(f'o: {count_o}')
print(f'-: {count_minus}')