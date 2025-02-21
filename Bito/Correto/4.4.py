# Lendo as dimensões do mapa
L, C = map(int, input().split())

# Inicializando o mapa e listas para marcar linhas e colunas
mapa = []
linhas_com_deposito = [False] * L
colunas_com_deposito = [False] * C

# Lendo o mapa e identificando depósitos
for i in range(L):
    linha = list(map(int, input().split()))
    mapa.append(linha)
    for j in range(C):
        if linha[j] == 1:
            linhas_com_deposito[i] = True
            colunas_com_deposito[j] = True

# Contando o número total de frascos de essência
total_fracos = sum(linhas_com_deposito) + sum(colunas_com_deposito)

# Imprimindo o total de frascos necessários
print(total_fracos)

# Imprimindo o mapa com marcações de linha
for i in range(L):
    linha_str = ' '.join(map(str, mapa[i])) + ' ' + ('M' if linhas_com_deposito[i] else '-')
    print(linha_str)

# Imprimindo as marcações de coluna
colunas_str = ' '.join('M' if colunas_com_deposito[j] else '-' for j in range(C))
print(colunas_str)