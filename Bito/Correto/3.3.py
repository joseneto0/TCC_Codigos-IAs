# Inicializando um dicionário para armazenar as contagens de sementes
contagem_sementes = {}

while True:
    # Lendo a entrada
    tipo_semente = input().strip()
    
    # Verificando se a entrada é "FIM"
    if tipo_semente == "FIM":
        break
    
    # Atualizando a contagem da semente
    if tipo_semente in contagem_sementes:
        contagem_sementes[tipo_semente] += 1
    else:
        contagem_sementes[tipo_semente] = 1
    
    # Imprimindo o tipo de semente e sua contagem atual
    print(f"{tipo_semente} {contagem_sementes[tipo_semente]}")