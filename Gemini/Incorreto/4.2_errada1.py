def analisar_cidade(matriz):
    linhas = len(matriz)
    colunas = len(matriz[0])
    resultado = [['+' if celula <= 100 else '-' if celula >= 200 else 'o' for celula in linha] for linha in matriz]

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