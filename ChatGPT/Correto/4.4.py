# Leitura da entrada
L, C = map(int, input().split())  # Número de linhas e colunas
mapa = [list(map(int, input().split())) for _ in range(L)]  # Matriz que representa o mapa

# Inicializando variáveis para rastrear as linhas e colunas que precisam de essência
linhas_essencia = [False] * L
colunas_essencia = [False] * C

# Verificando onde devemos colocar essência
for i in range(L):
    for j in range(C):
        if mapa[i][j] == 1:
            linhas_essencia[i] = True
            colunas_essencia[j] = True

# Contando a quantidade de frascos de essência necessários
quantidade_essencias = linhas_essencia.count(True) + colunas_essencia.count(True)

# Imprimindo a quantidade total de frascos de essência
print(quantidade_essencias)

# Imprimindo o mapa com a marcação das linhas
for i in range(L):
    linha = " ".join(map(str, mapa[i]))  # Converte a linha para uma string
    if linhas_essencia[i]:
        linha += " M"
    else:
        linha += " -"
    print(linha)

# Imprimindo as colunas com a marcação de necessidade de essência
print(" ".join("M" if colunas_essencia[j] else "-" for j in range(C)))