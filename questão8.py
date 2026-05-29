numero = input("Digite um número inteiro: ")
algarismo = input("Digite um dígito de 0 a 9: ")

quantidade = 0

for caractere in numero:
    
    if caractere == algarismo:
        quantidade += 1

print("O dígito aparece", quantidade, "vez(es).")