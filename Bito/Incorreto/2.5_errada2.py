# Inicializando variáveis
melões = 0
posicao = 0  # Começando no esconderijo 0

while True:
    # Lendo a entrada (foto)
    foto = input().strip()
    
    # Verificando se a entrada é a condição de parada
    if foto == "O" * len(foto):
        break

    # Verificando a posição do goblin e tomando decisões
    if foto[posicao] == 'X':
        print("Silêncio...")
    else:
        # O goblin não está olhando para o esconderijo atual
        pode_mover_esquerda = (posicao > 0 and foto[posicao - 1] == 'O')
        pode_mover_direita = (posicao < len(foto) - 1 and foto[posicao + 1] == 'O')
        
        if pode_mover_esquerda and not pode_mover_direita:
            # Só pode mover para a esquerda
            posicao -= 1
            print(f"Correndo pro esconderijo {posicao}!")
        elif pode_mover_direita and not pode_mover_esquerda:
            # Só pode mover para a direita
            posicao += 1
            print(f"Correndo pro esconderijo {posicao}!")
        elif pode_mover_esquerda and pode_mover_direita:
            # Pode atirar um melão
            print("Tiro de Melão!!!")
            melões += 1

# Imprimindo o resultado final
print(f"Vitória com {melões} melões!")