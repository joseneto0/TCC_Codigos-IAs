def marcar_essencias(mapa):
    linhas = len(mapa)
    colunas = len(mapa[0])

    # Inicializa uma matriz para marcar as linhas e colunas
    marcas_linhas = [False] * linhas
    marcas_colunas = [False] * colunas

    # Marca as linhas e colunas que possuem depósitos
    for i in range(linhas):
        for j in range(colunas):
            if mapa[i][j] == 1:
                marcas_linhas[i] = True
                marcas_colunas[j] = True

    # Conta a quantidade de marcas
    count_linhas = sum(marcas_linhas) 
    count_colunas = sum(marcas_colunas)
    count = count_linhas + count_colunas

    # Imprime o resultado
    print(count)
    for i in range(linhas):
        print(''.join(['M' if marcas_linhas[i] else '-' for _ in range(colunas)]))
    print(''.join(['M' if marca else '-' for marca in marcas_colunas]))

# Leitura da entrada
linhas, colunas = map(int, input().split())
mapa = []
for _ in range(linhas):
    linha = list(map(int, input().split()))
    mapa.append(linha)

# Chama a função para marcar as essências
marcar_essencias(mapa)