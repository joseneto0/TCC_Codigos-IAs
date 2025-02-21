def main():
    # Leitura do número de habitantes
    N = int(input().strip())
    
    # Conjunto para armazenar nomes únicos
    nomes_unicos = set()
    
    # Lista para preservar a ordem dos nomes únicos
    lista_nomes_unicos = []
    
    for _ in range(N):
        nome = input().strip()
        if nome not in nomes_unicos:
            nomes_unicos.add(nome)
            lista_nomes_unicos.append(nome)
    
    # Impressão dos nomes únicos
    for nome in lista_nomes_unicos:
        print(nome)

# Chamar a função principal
if __name__ == "__main__":
    main()