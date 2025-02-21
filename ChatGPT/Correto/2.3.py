def listar_nomes_unicos(n, nomes):
    vistos = set()  # Conjunto para controlar os nomes já impressos
    for nome in nomes:
        if nome not in vistos:
            print(nome)
            vistos.add(nome)

# Leitura da entrada
n = int(input())  # Número de habitantes
nomes = [input().strip() for _ in range(n)]  # Lista com os nomes

# Chamada da função para imprimir os nomes sem repetição
listar_nomes_unicos(n, nomes)