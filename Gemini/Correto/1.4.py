def contar_armadilhas(sequencia):
  """Conta o número mínimo de armadilhas para cobrir sequências de sensores ativados.

  Args:
    sequencia: Lista com os valores de ativação dos sensores.

  Returns:
    Número mínimo de armadilhas.
  """

  armadilhas = 0
  ativado = False
  for valor in sequencia:
    if valor == 1 and not ativado:
      armadilhas += 1
      ativado = True
    elif valor == 0:
      ativado = False
  return armadilhas

# Lendo a entrada
num_sensores = int(input())
sequencia = [int(input()) for _ in range(num_sensores)]

# Chamando a função e imprimindo o resultado
resultado = contar_armadilhas(sequencia)
print(resultado)