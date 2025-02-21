# Leitura do número de linhas e colunas
L, C = map(int, input().split())

# Inicialização da matriz
matriz = []

# Leitura da matriz
for _ in range(L):
    linha = list(map(int, input().split()))
    matriz.append(linha)

# Inicialização das variáveis para armazenar as linhas e colunas que precisam de essência
linhas_com_essencia = []
colunas_com_essencia = []

# Processamento da matriz
for i in range(L):
    for j in range(C):
        if matriz[i][j] == 1:
            if i not in linhas_com_essencia:
                linhas_com_essencia.append(i)
            if j not in colunas_com_essencia:
                colunas_com_essencia.append(j)

# Impressão do número de frascos de essência necessários
print(len(linhas_com_essencia) + len(colunas_com_essencia))

# Impressão da matriz com as informações de essência
for i in range(L):
    for j in range(C):
        print(matriz[i][j], end=' ')
    if i in linhas_com_essencia:
        print('M')
    else:
        print('-')

# Impressão das colunas que precisam de essência
for j in range(C):
    if j in colunas_com_essencia:
        print('M', end=' ')
    else:
        print('-', end=' ')
