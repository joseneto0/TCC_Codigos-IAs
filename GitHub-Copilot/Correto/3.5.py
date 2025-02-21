def gerenciar_gfm():
    # Leitura da capacidade do GFM
    N = int(input().strip())
    gfm = []
    
    while len(gfm) < N:
        a = int(input().strip())
        if a == 0:
            # Remover a semente com o maior valor
            max_val = max(gfm)
            gfm.remove(max_val)
            print(max_val)
        else:
            # Adicionar a semente ao GFM
            gfm.append(a)

# Chamar a função principal
if __name__ == "__main__":
    gerenciar_gfm()