import heapq

def main():
    N = int(input().strip())  # Número de sementes desejadas no GFM
    gfm = []  # Heap vazia para armazenar as sementes
    
    while len(gfm) < N:
        a = int(input().strip())  # Valor da semente ou 0
        
        if a == 0:
            # Remove a maior semente (o maior valor negativo)
            maior_semente = -heapq.heappop(gfm)
            print(maior_semente)
        else:
            # Adiciona a semente na heap (invertendo o sinal)
            heapq.heappush(gfm, -a)