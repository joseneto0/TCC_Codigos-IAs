n = int(input())
moedas = list(map(int, input().split()))
centro = n // 2
total = 0

for i in range(n):
    if moedas[i] > 0:
        distancia = abs(i - centro)
        total += distancia * moedas[i]

print(total)