# Lendo a entrada
pe_de_melao = int(input())
melões_colhidos = int(input())
melões_por_pe = int(input())

# Calculando o total esperado de melões
total_esperado = pe_de_melao * melões_por_pe

# Comparando o total colhido com o total esperado
if melões_colhidos < total_esperado:
    print("SIM")
else:
    print("NAO")