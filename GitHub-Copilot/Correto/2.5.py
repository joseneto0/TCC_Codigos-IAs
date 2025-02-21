def processar_fotos(fotos):
    esconderijo_atual = 0
    melões_atirados = 0
    ações = []

    for foto in fotos:
        if 'X' not in foto:
            # Condição de fim quando o goblin não está olhando para nenhum esconderijo
            break

        if foto[esconderijo_atual] == 'X':
            # Goblin está olhando para o esconderijo atual
            ações.append("Silêncio...")
        else:
            # Goblin não está olhando para o esconderijo atual
            mover_esquerda = (esconderijo_atual > 0 and foto[esconderijo_atual - 1] == 'O')
            mover_direita = (esconderijo_atual < len(foto) - 1 and foto[esconderijo_atual + 1] == 'O')

            if mover_esquerda and not mover_direita:
                esconderijo_atual -= 1
                ações.append(f"Correndo pro esconderijo {esconderijo_atual}!")
            elif mover_direita and not mover_esquerda:
                esconderijo_atual += 1
                ações.append(f"Correndo pro esconderijo {esconderijo_atual}!")
            else:
                melões_atirados += 1
                ações.append("Tiro de Melão!!!")

    ações.append(f"Vitória com {melões_atirados} melões!")

    return ações

# Leitura das entradas
fotos = []
while True:
    foto = input().strip()
    if foto == "" or foto == "O" * len(foto):
        break
    fotos.append(foto)

# Processar as fotos e obter as ações
ações = processar_fotos(fotos)

# Imprimir as ações
for ação in ações:
    print(ação)