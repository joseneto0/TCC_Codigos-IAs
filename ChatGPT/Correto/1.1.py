# Leitura dos dados de entrada
pe_meloes = int(input())  # Número de pés de melão
meloes_colhidos = int(input())  # Número de melões colhidos
meloes_por_pe = int(input())  # Número de melões que cada pé deveria produzir

# Calculando o total esperado de melões
total_esperado = pe_meloes * meloes_por_pe

# Comparando o total esperado com o total colhido
if meloes_colhidos < total_esperado:
    print("SIM")
else:
    print("NAO")