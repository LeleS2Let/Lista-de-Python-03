num = int(input("Digite um número inteiro positivo: "))

for linha in range(num, 0, -1):
    
    for coluna in range(linha):
        print("*", end="")
    
    print()