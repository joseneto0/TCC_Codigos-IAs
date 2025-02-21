# Leitura da quantidade de humanos disponíveis
P = int(input())

# Variáveis para acumular melões roubados e goblins resgatados
meloes_roubados = 0
goblins_resgatados = 0

# Processamento dos ataques
while True:
    F, M, G = map(int, input().split())
    
    # Se o ataque for o final (0 0 0), parar o processamento
    if F == 0 and M == 0 and G == 0:
        break
    
    # Verificar se o ataque é bem-sucedido
    if F > P:  # O ataque tem sucesso apenas se F > P
        meloes_roubados += M
        goblins_resgatados += G
    
    # Imprimir o status atual após o ataque
    print(f"Meloes roubados: {meloes_roubados}")
    print(f"Goblins resgatados: {goblins_resgatados}")
    print("---")