# Leitura do tamanho da população da cidade
P = int(input())

# Inicialização das variáveis para armazenar a quantidade de melões roubados e goblins resgatados
meloes_roubados = 0
goblins_resgatados = 0

# Loop para processar os ataques dos goblins
while True:
    # Leitura dos dados do ataque
    F, M, G = map(int, input().split())

    # Verificação se é o ataque final (0 0 0)
    if F == 0 and M == 0 and G == 0:
        break

    # Verificação se a horda foi bloqueada
    if F <= P:
        print(f"Meloes roubados: {meloes_roubados}")
        print(f"Goblins resgatados: {goblins_resgatados} \n---")
    else:
        meloes_roubados += M
        goblins_resgatados += G
        print(f"Meloes roubados: {meloes_roubados}")
        print(f"Goblins resgatados: {goblins_resgatados} \n---")
