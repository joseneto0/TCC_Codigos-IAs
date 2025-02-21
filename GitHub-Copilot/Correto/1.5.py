def main():
    # Leitura do valor da população da cidade
    P = int(input().strip())
    
    meloes_roubados = 0
    goblins_resgatados = 0

    while True:
        # Leitura dos valores do ataque
        F, M, G = map(int, input().strip().split())
        
        # Verificação da condição de término
        if F == 0 and M == 0 and G == 0:
            break
        
        # Verificação se a horda foi bloqueada ou não
        if F > P:
            meloes_roubados += M
            goblins_resgatados += G
        
        # Impressão dos resultados acumulados até o momento
        print(f"Meloes roubados: {meloes_roubados}")
        print(f"Goblins resgatados: {goblins_resgatados}")
        print("---")

# Chamar a função principal
if __name__ == "__main__":
    main()