def organizar_fila():
    # Lê o número de pessoas
    N = int(input())
    
    # Lê as prioridades e armazena em uma lista
    prioridades = [int(input()) for _ in range(N)]
    
    # Ordena as prioridades em ordem crescente
    prioridades.sort()
    
    # Imprime as prioridades ordenadas, uma por linha
    for prioridade in prioridades:
        print(prioridade)

# Chama a função para organizar a fila
organizar_fila()