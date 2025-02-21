def marcar_essencia_de_melao(L, C, mapa):
    linhas_com_essencia = [False] * L
    colunas_com_essencia = [False] * C

    # Verificar quais linhas e colunas precisam de essência
    for i in range(L):
        for j in range(C):
            if mapa[i][j] == 1:
                linhas_com_essencia[i] = True
                colunas_com_essencia[j] = True

    # Contar a quantidade total de frascos de essência necessários
    frascos_necessarios = sum(linhas_com_essencia) + sum(colunas_com_essencia)

    # Gerar a saída
    resultado = []
    resultado.append(str(frascos_necessarios))

    for i in range(L):
        linha_res = ' '.join(map(str, mapa[i])) + ' ' + ('M' if linhas_com_essencia[i] else '-')
        resultado.append(linha_res)

    colunas_res = ' '.join('M' if colunas_com_essencia[j] else '-' for j in range(C))
    resultado.append(colunas_res)

    return resultado

# Leitura da entrada
L, C = map(int, input().strip().split())
mapa = [list(map(int, input().strip().split())) for _ in range(L)]

# Processar o mapa
resultado = marcar_essencia_de_melao(L, C, mapa)

# Imprimir o resultado
for linha in resultado:
    print(linha)