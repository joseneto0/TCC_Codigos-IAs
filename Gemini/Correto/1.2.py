def analisar_producao(produtores, esperado):
  """Analisa a produção total de melões e retorna uma classificação.

  Args:
    produtores: Lista com a quantidade de melões colhidos por cada produtor.
    esperado: Valor total esperado de melões.

  Returns:
    Uma string indicando a classificação da produção.
  """

  total_colhido = sum(produtores)
  if total_colhido >= esperado:
    return "NADA PREOCUPANTE"
  elif total_colhido >= esperado - 5:
    return "POUCO PREOCUPANTE"
  else:
    return "MUITO PREOCUPANTE"

# Lendo a entrada
num_produtores, esperado = map(int, input().split())
producoes = [int(input()) for _ in range(num_produtores)]

# Chamando a função e imprimindo o resultado
resultado = analisar_producao(producoes, esperado)
print(resultado)