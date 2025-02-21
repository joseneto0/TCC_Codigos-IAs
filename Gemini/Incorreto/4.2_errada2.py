def analisar_cidade(matriz):
    linhas = len(matriz)
    colunas = len(matriz[0])
    resultado = []
    for linha in matriz:
        nova_linha = []
        for celula in linha:
            if celula <= 100:
                nova_linha.append('+')
            elif celula >= 200:
                nova_linha.append('-')
            else:  # 100 < celula < 200
                nova_linha.append('o')
        resultado.append(nova_linha)

    contagem = {'+': 0, '-': 0, 'o': 0}
    for linha in resultado:
        for caractere in linha:
            contagem[caractere] += 1

    # Imprimir a matriz simplificada
    for linha in resultado:
        print(''.join(linha))

    print()

    # Imprimir a contagem
    for caractere, quantidade in contagem.items():
        print(f"{caractere}: {quantidade}")

# Leitura da entrada
n = int(input())
matriz = []
for _ in range(n):
    linha = list(map(int, input().split()))
    matriz.append(linha)

# Analisar a cidade e imprimir o resultado
analisar_cidade(matriz)