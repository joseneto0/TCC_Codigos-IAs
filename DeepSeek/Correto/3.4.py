def simular_fila():
    fila = []
    while True:
        entrada = input().strip()
        if entrada == "FIM":
            break
        if entrada == "PROXIMO":
            proximo = fila.pop(0)
            print(f"PROXIMO: {proximo}")
        else:
            fila.append(entrada)
            print(f"FILA: {' '.join(fila)}")

# Chama a função para simular a fila
simular_fila()