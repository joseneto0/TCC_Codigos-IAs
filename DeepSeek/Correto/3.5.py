def simular_gfm():
    N = int(input())  # Capacidade do GFM
    gfm = []  # Lista para armazenar as sementes

    while len(gfm) < N:
        a = int(input())
        if a == 0:
            # Remove a semente mais valiosa
            semente_removida = max(gfm)
            gfm.remove(semente_removida)
            print(semente_removida)
        else:
            # Adiciona a semente ao GFM
            gfm.append(a)

# Chama a função para simular o GFM
simular_gfm()