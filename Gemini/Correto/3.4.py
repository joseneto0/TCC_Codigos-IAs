fila = []

while True:
    pessoa = input()
    if pessoa == "FIM":
        break
    elif pessoa == "PROXIMO":
        if fila:
            proximo = fila.pop(0)
            print(f"PROXIMO: {proximo}")
        else:
            print("A fila está vazia!")  # Caso especial para fila vazia
    else:
        fila.append(pessoa)
        print(f"FILA: {' '.join(fila)}")