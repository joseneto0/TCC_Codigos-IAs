# Leitura dos dados
pes_de_melao = int(input())
meloes_colhidos = int(input())
meloes_por_pe = int(input())

# Cálculo do total de melões esperados
total_esperado = pes_de_melao * meloes_por_pe

# Verificação se o total de melões está abaixo do esperado
if meloes_colhidos < total_esperado:
    print("SIM")
else:
    print("NAO")
