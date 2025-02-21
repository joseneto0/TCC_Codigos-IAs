def gerenciar_gfm(capacidade, entradas):
    gfm = []
    for valor in entradas:
        if valor == 0:
            if gfm:
                print(max(gfm))
                gfm.remove(max(gfm))
        else:
            gfm.append(valor)
            if len(gfm) > capacidade:
                gfm.remove(max(gfm))

# Leitura da entrada
capacidade = int(input())
entradas = []
while True:
    valor = int(input())
    if len(entradas) == capacidade:
        break
    entradas.append(valor)

# Gerenciamento do GFM
gerenciar_gfm(capacidade, entradas)