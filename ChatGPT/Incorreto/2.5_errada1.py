def processo_fotos(fotos):
    esconderijo_atual = 0  # Começamos no esconderijo 000
    melões = 0
    n = len(fotos[0])  # Quantidade de esconderijos
    
    for foto in fotos:
        if foto[esconderijo_atual] == 'X':
            # O goblin está olhando para o esconderijo, ficar em silêncio
            print("Silêncio...")
        else:
            # O goblin não está olhando para o esconderijo, verificar movimentos
            vizinhos = []
            
            # Verificar vizinho à esquerda (se não for o primeiro esconderijo)
            if esconderijo_atual > 0 and foto[esconderijo_atual - 1] == 'O':
                vizinhos.append(esconderijo_atual - 1)
                
            # Verificar vizinho à direita (se não for o último esconderijo)
            if esconderijo_atual < n - 1 and foto[esconderijo_atual + 1] == 'O':
                vizinhos.append(esconderijo_atual + 1)
            
            if len(vizinhos) == 1:
                # Só há um vizinho possível, então vamos para lá
                esconderijo_atual = vizinhos[0]
                print(f"Correndo pro esconderijo {esconderijo_atual}!")
            elif len(vizinhos) == 0:
                # Não há vizinho possível, então atiramos um melão
                melões += 1
                print("Tiro de Melão!!!")
            else:
                # Há dois vizinhos possíveis, não nos movemos e atiramos um melão
                melões += 1
                print("Tiro de Melão!!!")
        
        # Caso o goblin não esteja olhando para nenhum esconderijo
        if foto == 'O' * n:
            break

    print(f"Vitória com {melões} melões!")

# Leitura da entrada
fotos = []
while True:
    foto = input().strip()
    if foto == 'O' * len(foto):
        fotos.append(foto)
        break
    fotos.append(foto)

# Executar o processo
processo_fotos(fotos)