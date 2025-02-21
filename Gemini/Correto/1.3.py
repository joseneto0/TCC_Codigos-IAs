def verificar_sombras(sensores, referencia):
  """Verifica se houve sombra em cada sensor.

  Args:
    sensores: Lista com os valores de cada sensor.
    referencia: Valor de referência para comparação.

  Returns:
    Uma lista com 1 (houve sombra) ou 0 (não houve sombra) para cada sensor.
  """

  resultados = []
  for valor in sensores:
    resultados.append(1 if valor <= referencia else 0)
  return resultados

# Lendo a entrada
num_sensores, referencia = map(int, input().split())
valores_sensores = list(map(int, input().split()))

# Chamando a função e imprimindo os resultados
resultados = verificar_sombras(valores_sensores, referencia)
print(*resultados)