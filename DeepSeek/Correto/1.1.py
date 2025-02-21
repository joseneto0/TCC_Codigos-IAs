def main():
  # Digite seu código aqui
  # Leitura dos dados
  p = int(input())  # Número de pés de melão
  m = int(input())  # Número de melões colhidos
  n = int(input())  # Número de melões que cada pé deveria produzir
  
  # Cálculo do total esperado
  total_esperado = p * n
  
  # Comparação e impressão do resultado
  if m < total_esperado:
      print("SIM")
  else:
      print("NAO")
  pass

if __name__ == "__main__":
  main()