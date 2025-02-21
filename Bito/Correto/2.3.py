# Lendo o número de habitantes
N = int(input())

# Inicializando um conjunto para armazenar nomes únicos e uma lista para a saída
nomes_unicos = set()
saida = []

# Processando cada nome
for _ in range(N):
    nome = input().strip()
    if nome not in nomes_unicos:
        nomes_unicos.add(nome)
        saida.append(nome)

# Imprimindo a lista de nomes sem duplicatas
for nome in saida:
    print(nome)