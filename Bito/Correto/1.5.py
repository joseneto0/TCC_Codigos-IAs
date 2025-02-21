# Lendo o tamanho da população
P = int(input())

# Inicializando contadores de melões roubados e goblins resgatados
melões_roubados = 0
goblins_resgatados = 0

while True:
    # Lendo os dados do ataque
    ataque = input().strip()
    F, M, G = map(int, ataque.split())

    # Condição de parada
    if F == 0 and M == 0 and G == 0:
        break

    # Verificando se a horda pode ser bloqueada
    if F > P:
        # Se a horda não for bloqueada, atualizamos os contadores
        melões_roubados += M
        goblins_resgatados += G

    # Imprimindo o resultado até o momento
    print(f"Meloes roubados: {melões_roubados}")
    print(f"Goblins resgatados: {goblins_resgatados}")
    print("---")