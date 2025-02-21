# Inicialização da fila
fila = []

# Loop para processar as linhas da entrada
while True:
    # Leitura da linha
    linha = input()

    # Verificação se a linha é a palavra FIM
    if linha == 'FIM':
        break

    # Verificação se a linha é a palavra PROXIMO
    if linha == 'PROXIMO':
        # Impressão do próximo da fila
        print(f"PROXIMO: {fila.pop(0)}")
    else:
        # Adição da pessoa à fila
        fila.append(linha)

        # Impressão da fila
        print(f"FILA: {' '.join(fila)}")