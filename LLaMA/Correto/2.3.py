# Leitura do número de habitantes
N = int(input())

# Inicialização de uma lista para armazenar os nomes únicos
nomes_unicos = []

# Loop para processar os nomes
for _ in range(N):
    # Leitura do nome
    nome = input()

    # Verificação se o nome já está na lista
    if nome not in nomes_unicos:
        # Adiciona o nome à lista
        nomes_unicos.append(nome)

# Impressão da lista de nomes únicos
for nome in nomes_unicos:
    print(nome)
