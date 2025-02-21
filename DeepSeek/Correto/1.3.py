def main():
  # Digite seu código aqui
  # Leitura dos dados
  N, R = map(int, input().split())  # Número de sensores e valor de referência
  sensores = list(map(int, input().split()))  # Valores dos sensores
  
  # Comparação e impressão do resultado
  for valor in sensores:
      if valor <= R:
          print(1)
      else:
          print(0)
  pass

if __name__ == "__main__":
  main()