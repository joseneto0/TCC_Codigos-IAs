def contar_armadilhas(sensores):
    armadilhas = 0
    i = 0
    n = len(sensores)
    
    while i < n:
        if sensores[i] == 1:
            armadilhas += 1
            while i < n and sensores[i] == 1:
                i += 1
        else:
            i += 1
    
    return armadilhas

# Exemplo de uso
N = int(input())
sensores = [int(input()) for _ in range(N)]
print(contar_armadilhas(sensores))