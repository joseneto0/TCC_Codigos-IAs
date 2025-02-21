# Ler as fotos
fotos = []
while True:
    foto = input().strip()
    if not 'X' in foto:
        break
    fotos.append(foto)

# Variáveis para o jogo
posicao = 0  # posição atual do goblin
meloes = 0   # quantos melões têm

for foto in fotos:
    # Determinar a direção do goblin
    direcao = None
    for i, char in enumerate(foto):
        if char == 'X':
            direcao = i - posicao
            break

    if direcao is not None:
        # O goblin está olhando para algum esconderijo
        if direcao > 0 and posicao + direcao < len(fotos[0]):
            # Se for possível mudar de esconderijo, atirar melão
            print("Tiro de Melão!!!")
            # Mover para o esconderijo que ele está olhando
            posicao += direcao
        else:
            # Não está olhando para um esconderijo vizinho, manter silencio
            print("Silêncio...")
    else:
        # Goblin não está olhando para nenhuma posição, manter silencio
        print("Silêncio...")

print("Vitória com", meloes, "melões!")