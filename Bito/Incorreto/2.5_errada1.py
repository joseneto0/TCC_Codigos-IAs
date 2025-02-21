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
        if (posicao > 0 and foto[posicao - 1] == 'O') and (posicao < len(foto) - 1 and foto[posicao + 1] == 'O'):
            print("Tiro de Melão!!!")
            melões += 1
        elif (posicao > 0 and foto[posicao - 1] == 'O') and (posicao == len(foto) - 1 or foto[posicao + 1] == 'X'):
            print("Tiro de Melão!!!")
            melões += 1
        elif (posicao < len(foto) - 1 and foto[posicao + 1] == 'O') and (posicao == 0 or foto[posicao - 1] == 'X'):
            print("Tiro de Melão!!!")
            melões += 1
        elif (posicao > 0 and foto[posicao - 1] == 'O'):
            posicao -= 1
            print(f"Correndo pro esconderijo {posicao}!")
        elif (posicao < len(foto) - 1 and foto[posicao + 1] == 'O'):
            posicao += 1
            print(f"Correndo pro esconderijo {posicao}!")

# Imprimindo o resultado final
print(f"Vitória com {melões} melões!")