# Leitura do número de sementes que cabem no GFM
N = int(input())

# Inicialização da lista para armazenar as sementes
sementes = []

# Loop para processar as linhas da entrada
while len(sementes) < N:
    # Leitura do valor da semente
    a = int(input())

    # Verificação se é um ninja
    if a == 0:
        # Impressão do valor da semente mais valiosa
        print(max(sementes))

        # Remoção da semente mais valiosa
        sementes.remove(max(sementes))
    else:
        # Adição da semente ao GFM
        sementes.append(a)
