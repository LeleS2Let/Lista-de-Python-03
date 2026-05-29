vendas_meses = []
soma = 0

for contador in range(1, 7):
    valor = float(input(f"Digite o valor vendido no mês {contador}: "))
    
    vendas_meses.append(valor)
    
    soma += valor

media = soma / 6

meses_acima = 0

for valor in vendas_meses:
    
    if valor > media:
        meses_acima += 1

print("Total vendido:", soma)
print("Média mensal:", media)
print("Quantidade de meses acima da média:", meses_acima)