# Lendo a quantidade máxima de sementes que o GFM pode armazenar
N = int(input())

# Inicializando a lista para armazenar as sementes
gfm = []

while len(gfm) < N:
    a = int(input())
    
    if a == 0:
        # Remover a semente mais valiosa (maior valor)
        semente_mais_valiosa = max(gfm)
        gfm.remove(semente_mais_valiosa)
        print(semente_mais_valiosa)
    else:
        # Adicionar a semente com valor a
        gfm.append(a)

# O programa termina quando o GFM possui exatamente N sementes