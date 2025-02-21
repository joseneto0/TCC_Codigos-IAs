# https://github.com/copilot/c/803a5b1d-7e09-4a4b-be07-76f893ab175d
# Leitura dos valores de entrada
pes_melao = int(input())
meloes_colhidos = int(input())
meloes_por_pe = int(input())

# Calcular o número total de melões esperados
meloes_esperados = pes_melao * meloes_por_pe

# Comparar e imprimir o resultado
if meloes_colhidos < meloes_esperados:
    print("SIM")
else:
    print("NAO")