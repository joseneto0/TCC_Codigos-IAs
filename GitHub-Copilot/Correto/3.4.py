def gerenciar_fila():
    from collections import deque
    
    fila = deque()
    
    while True:
        linha = input().strip()
        if linha == "FIM":
            break
        elif linha == "PROXIMO":
            proximo = fila.popleft()
            print(f"PROXIMO: {proximo}")
        else:
            fila.append(linha)
            print(f"FILA: {' '.join(fila)}")

# Chamar a função principal
if __name__ == "__main__":
    gerenciar_fila()