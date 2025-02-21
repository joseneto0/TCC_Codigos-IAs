def simular_estrategia(fotos):
    esconderijo_atual = 0
    meloes = 0

    for foto in fotos:
        if all(c == 'O' for c in foto):
            print("Vitória com", meloes, "melões!")
            break

        if foto[esconderijo_atual] == 'X':
            print("Silêncio...")
        else:
            # Verifica se pode atirar um melão
            if foto[esconderijo_atual] == 'O':
                print("Tiro de Melão!!!")
                meloes += 1
            else:
                # Verifica se pode mudar de esconderijo
                opcoes = []
                if esconderijo_atual > 0 and foto[esconderijo_atual - 1] == 'O':
                    opcoes.append(esconderijo_atual - 1)
                if esconderijo_atual < len(foto) - 1 and foto[esconderijo_atual + 1] == 'O':
                    opcoes.append(esconderijo_atual + 1)

                if len(opcoes) == 1:
                    esconderijo_atual = opcoes[0]
                    print(f"Correndo pro esconderijo {esconderijo_atual}!")
                elif len(opcoes) > 1:
                    # Escolhe a primeira opção disponível (esquerda ou direita)
                    esconderijo_atual = opcoes[0]
                    print(f"Correndo pro esconderijo {esconderijo_atual}!")
                else:
                    print("Silêncio...")

# Exemplo de uso
fotos = []
while True:
    linha = input().strip()
    if all(c == 'O' for c in linha):
        fotos.append(linha)
        break
    fotos.append(linha)

simular_estrategia(fotos)