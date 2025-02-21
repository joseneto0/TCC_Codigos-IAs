def contar_sementes():
    sementes = {}
    
    while True:
        semente = input().strip()
        if semente == "FIM":
            break
        if semente not in sementes:
            sementes[semente] = 0
        sementes[semente] += 1
        print(f"{semente} {sementes[semente]}")

# Chamar a função principal
if __name__ == "__main__":
    contar_sementes()