def main():
    # Leitura do número de pessoas
    N = int(input().strip())
    
    # Leitura das prioridades dos problemas
    prioridades = []
    for _ in range(N):
        prioridade = int(input().strip())
        prioridades.append(prioridade)
    
    # Ordenar as prioridades em ordem crescente
    prioridades.sort()
    
    # Imprimir as prioridades ordenadas
    for prioridade in prioridades:
        print(prioridade)

# Chamar a função principal
if __name__ == "__main__":
    main()