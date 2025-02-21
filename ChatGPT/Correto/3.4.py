# Inicializa a fila como uma lista vazia
fila = []

# Loop contínuo para processar as entradas
while True:
    # Lê a entrada e remove espaços extras
    entrada = input().strip()
    
    # Se a entrada for "FIM", encerra o loop
    if entrada == "FIM":
        break
    
    # Se a entrada for "PROXIMO", chama a pessoa da frente da fila
    if entrada == "PROXIMO":
        proximo = fila.pop(0)  # Remove o primeiro nome da fila
        print(f"PROXIMO: {proximo}")
    else:
        # Se for o nome de uma pessoa, adiciona na fila
        fila.append(entrada)
        # Imprime a fila atualizada
        print(f"FILA: {' '.join(fila)}")