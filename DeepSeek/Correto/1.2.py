def main():
  # Digite seu código aqui
  # Leitura dos dados
  N, E = map(int, input().split())  # Número de produtores e total esperado
  total_colhido = 0
  
  # Leitura da quantidade de melões colhidos por cada produtor
  for _ in range(N):
      total_colhido += int(input())
  
  # Comparação e impressão do resultado
  if total_colhido >= E:
      print("NADA PREOCUPANTE")
  elif total_colhido >= E - 5:
      print("POUCO PREOCUPANTE")
  else:
      print("MUITO PREOCUPANTE")
  pass

if __name__ == "__main__":
  main()