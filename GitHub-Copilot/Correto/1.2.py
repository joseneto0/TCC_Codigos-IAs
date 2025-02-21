# Leitura dos valores de entrada
primeira_linha = input().split()
N = int(primeira_linha[0])
E = int(primeira_linha[1])

# Inicializar a soma total de melões colhidos
total_colhido = 0

# Ler a quantidade de melões colhida por cada produtor e somar
for _ in range(N):
    melões_colhidos = int(input())
    total_colhido += melões_colhidos

# Comparar o total colhido com o valor esperado e determinar o nível de preocupação
if total_colhido >= E:
    print("NADA PREOCUPANTE")
elif total_colhido >= E - 5:
    print("POUCO PREOCUPANTE")
else:
    print("MUITO PREOCUPANTE")