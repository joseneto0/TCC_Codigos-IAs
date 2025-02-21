# Inicializando uma lista para armazenar a fila
fila = []

while True:
    # Lendo a entrada
    entrada = input().strip()
    
    # Verificando se a entrada é "FIM"
    if entrada == "FIM":
        break
    
    # Se a entrada for um nome, adiciona à fila
    if entrada != "PROXIMO":
        fila.append(entrada)
        print("FILA:", " ".join(fila))
    else:
        # Se for "PROXIMO", chama a próxima pessoa da fila
        if fila:
            proximo = fila.pop(0)  # Remove a primeira pessoa da fila
            print("PROXIMO:", proximo)