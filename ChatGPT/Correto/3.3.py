# Dicionário para armazenar as contagens das sementes
semente_contagem = {}

# Loop para ler as sementes até encontrar "FIM"
while True:
    semente = input().strip()  # Lê a semente e remove espaços desnecessários
    if semente == "FIM":  # Se for "FIM", saímos do loop
        break
    if semente in semente_contagem:
        semente_contagem[semente] += 1  # Incrementa a contagem
    else:
        semente_contagem[semente] = 1  # Primeira vez que vemos essa semente
    
    # Imprime o tipo de semente e sua quantidade até o momento
    print(f"{semente} {semente_contagem[semente]}")