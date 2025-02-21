def organizar_problemas(N, prioridades):
    # Ordena as prioridades em ordem crescente
    prioridades_ordenadas = sorted(prioridades)
    
    # Imprime as prioridades ordenadas, uma por linha
    for prioridade in prioridades_ordenadas:
        print(prioridade)

# Leitura da entrada
N = int(input())  # Lê o número de pessoas
prioridades = [int(input()) for _ in range(N)]  # Lê as prioridades de cada pessoa

# Executa o processo
organizar_problemas(N, prioridades)