def organizar_fila(prioridades):
    """Organiza uma fila de prioridades em ordem crescente.

    Args:
        prioridades: Uma lista de inteiros representando as prioridades.

    Returns:
        Uma nova lista com as prioridades ordenadas em ordem crescente.
    """

    prioridades.sort()
    return prioridades

# Leitura da entrada
n = int(input())
prioridades = []
for _ in range(n):
    prioridades.append(int(input()))

# Organização e impressão da fila
fila_ordenada = organizar_fila(prioridades)
for prioridade in fila_ordenada:
    print(prioridade)