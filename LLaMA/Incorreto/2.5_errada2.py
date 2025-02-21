# Inicialização da posição atual e do número de melões
posicao_atual = 0
num_meloes = 0

# Loop para processar as fotos
while True:
    # Leitura da foto
    foto = input()

    # Verificação se o goblin não está olhando para nenhum esconderijo
    if 'X' not in foto:
        # Impressão da vitória
        print(f"Vitória com {num_meloes} melões!")
        break

    # Verificação se o goblin está olhando para o esconderijo atual
    if foto[posicao_atual] == 'X':
        # Impressão da ação de silêncio
        print("Silêncio...")
    else:
        # Verificação se é possível mudar de esconderijo
        if posicao_atual > 0 and foto[posicao_atual - 1] != 'X':
            # Impressão da ação de mudança de esconderijo
            print(f"Correndo pro esconderijo {posicao_atual - 1}!")
            posicao_atual -= 1
        elif posicao_atual < len(foto) - 1 and foto[posicao_atual + 1] != 'X':
            # Impressão da ação de mudança de esconderijo
            print(f"Correndo pro esconderijo {posicao_atual + 1}!")
            posicao_atual += 1
        else:
            # Impressão da ação de tiro de melão
            print("Tiro de Melão!!!")
            num_meloes += 1
            # Contagem adicional para o último tiro
            if 'X' not in foto.replace('O', 'X', 1):
                num_meloes += 1