import heapq

def gerenciar_gfm(capacidad, entradas):
    gfm = []  # Usamos una lista como cola de prioridad
    for valor in entradas:
        if valor == 0:
            if gfm:
                print(-heapq.heappop(gfm))  # Extraemos el máximo (negativo)
        else:
            heapq.heappush(gfm, -valor)  # Insertamos el valor negado para obtener un max-heap
            if len(gfm) > capacidad:
                heapq.heappop(gfm)  # Eliminamos el máximo (negativo)

# Leitura da entrada
capacidade = int(input())
entradas = []
while True:
    valor = int(input())
    if len(entradas) == capacidade:
        break
    entradas.append(valor)

# Gerenciamiento del GFM
gerenciar_gfm(capacidade, entradas)