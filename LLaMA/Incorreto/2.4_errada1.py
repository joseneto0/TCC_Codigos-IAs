# Leitura dos versos
versos = [input().split()[-1] for _ in range(4)]

# Verificação se a última palavra de cada verso tem o mesmo número de letras
if len(set(map(len, versos))) != 1:
    print("Erro: A última palavra de cada verso não tem o mesmo número de letras.")
else:
    # Cálculo da beleza do poema
    beleza = sum((versos[0][i] == versos[2][i]) + (versos[1][i] == versos[3][i]) for i in range(len(versos[0])))

    # Impressão da beleza do poema
    print(beleza)
