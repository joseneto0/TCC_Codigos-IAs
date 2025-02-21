def simular_defesa(P, ataques):
    meloes_roubados = 0
    goblins_resgatados = 0
    
    for ataque in ataques:
        F, M, G = ataque
        if F == 0 and M == 0 and G == 0:
            break
        if F > P:
            meloes_roubados += M
            goblins_resgatados += G
        print(f"Meloes roubados: {meloes_roubados}")
        print(f"Goblins resgatados: {goblins_resgatados}")
        print("---")

# Exemplo de uso
P = int(input())
ataques = []
while True:
    linha = input().strip()
    if linha == "0 0 0":
        break
    F, M, G = map(int, linha.split())
    ataques.append((F, M, G))

simular_defesa(P, ataques)