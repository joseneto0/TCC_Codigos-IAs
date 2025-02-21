posicao = 0
meloes = 0

while True:
    foto = input()
    if all(c == 'O' for c in foto):
        break

    olhando_esquerda = foto[posicao - 1] if posicao > 0 else 'X'
    olhando_direita = foto[posicao + 1] if posicao < len(foto) - 1 else 'X'
    olhando_atual = foto[posicao]

    if olhando_atual == 'X':
        print("Silêncio...")
    elif olhando_esquerda == 'O' and olhando_direita == 'X':
        posicao -= 1
        print(f"Correndo pro esconderijo {posicao}!")
    elif olhando_esquerda == 'X' and olhando_direita == 'O':
        posicao += 1
        print(f"Correndo pro esconderijo {posicao}!")
    else:
        meloes += 1
        print("Tiro de Melão!!!")

print(f"Vitória com {meloes} melões!")