total = 0

for contador in range(1, 6):
    valor = float(input("Digite um número: "))
    
    if contador == 1:
        maior_numero = valor
        menor_numero = valor
    
    if valor >= maior_numero:
        maior_numero = valor
    
    if valor <= menor_numero:
        menor_numero = valor
    
    total += valor

media = total / 5

print("Maior valor:", maior_numero)
print("Menor valor:", menor_numero)
print("Média dos valores:", media)