# Leitura dos versos
versos = [input().split()[-1] for _ in range(4)]

# Cálculo da beleza do poema
beleza = sum((versos[0][i] == versos[2][i]) for i in range(min(len(versos[0]), len(versos[2])))) + sum((versos[1][i] == versos[3][i]) for i in range(min(len(versos[1]), len(versos[3]))))

# Impressão da beleza do poema
print(beleza)
