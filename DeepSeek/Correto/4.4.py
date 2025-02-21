def marcar_essencia(L, C, mapa):
    linhas_marcadas = [False] * L
    colunas_marcadas = [False] * C

    # Verifica quais linhas e colunas têm depósitos
    for i in range(L):
        for j in range(C):
            if mapa[i][j] == 1:
                linhas_marcadas[i] = True
                colunas_marcadas[j] = True

    # Conta o número de frascos necessários
    frascos = sum(linhas_marcadas) + sum(colunas_marcadas)

    # Imprime o número de frascos
    print(frascos)

    # Imprime o mapa com as marcações das linhas
    for i in range(L):
        linha = ' '.join(map(str, mapa[i]))
        if linhas_marcadas[i]:
            print(f"{linha} M")
        else:
            print(f"{linha} -")

    # Imprime as marcações das colunas
    print(' '.join(['M' if colunas_marcadas[j] else '-' for j in range(C)]))

# Leitura da entrada
L, C = map(int, input().split())
mapa = [list(map(int, input().split())) for _ in range(L)]

# Marcação das essências
marcar_essencia(L, C, mapa)