# Lendo o tamanho da matriz
N = int(input())

# Inicializando a matriz e o contador de símbolos
matriz = []
contador_plus = 0
contador_o = 0
contador_minus = 0

# Lendo a matriz e processando as células
for _ in range(N):
    linha = list(map(int, input().split()))
    nova_linha = ""
    
    for goblins in linha:
        if goblins <= 100:
            nova_linha += "+"
            contador_plus += 1
        elif 100 < goblins < 110:
            nova_linha += "o"
            contador_o += 1
        else:
            nova_linha += "-"
            contador_minus += 1
    
    matriz.append(nova_linha)

# Imprimindo a matriz simplificada
for linha in matriz:
    print(linha)

# Linha em branco
print()

# Imprimindo a contagem de símbolos
print(f"+: {contador_plus}")
print(f"o: {contador_o}")
print(f"-: {contador_minus}")