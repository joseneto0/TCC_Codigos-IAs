def batalha_de_meloes():
    esconderijo = 0
    melões = 0

    while True:
        linha = input()
        if linha == 'OOOOOOOOO':  # Condição de parada: todas as posições são 'O'
            break
        if linha[esconderijo] == 'X':
            print("Silêncio...")
        else:
            vizinhos_seguros = [i for i in range(max(0, esconderijo-1), min(len(linha), esconderijo+2)) if linha[i] == 'O']
            if len(vizinhos_seguros) == 1:
                esconderijo = vizinhos_seguros[0]
                print("Correndo pro esconderijo", esconderijo, "!")
            else:
                melões += 1
                print("Tiro de Melão!!!")

    print("Vitória com", melões, "melões!")

# Chamando a função para iniciar a batalha
batalha_de_meloes()