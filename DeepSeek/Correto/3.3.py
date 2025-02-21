def contar_sementes():
    sementes = []
    while True:
        linha = input().strip()
        if linha == "FIM":
            break
        sementes.append(linha)
    
    contador = {}
    for semente in sementes:
        if semente in contador:
            contador[semente] += 1
        else:
            contador[semente] = 1
        print(f"{semente} {contador[semente]}")

# Chama a função para contar as sementes
contar_sementes()