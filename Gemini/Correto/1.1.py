def verificar_producao(pes, colhidos, esperado_por_pe):
  """Verifica se a produção de melões está abaixo do esperado.

  Args:
    pes: Número de pés de melão.
    colhidos: Número de melões colhidos.
    esperado_por_pe: Número esperado de melões por pé.

  Returns:
    "SIM" se a produção real for menor que a esperada, "NAO" caso contrário.
  """

  esperado_total = pes * esperado_por_pe
  return "SIM" if colhidos < esperado_total else "NAO"

# Lendo os dados de entrada
pes = int(input())
colhidos = int(input())
esperado_por_pe = int(input())

# Chamando a função e imprimindo o resultado
resultado = verificar_producao(pes, colhidos, esperado_por_pe)
print(resultado)