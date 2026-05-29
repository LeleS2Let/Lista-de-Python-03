total = 0

for produto in range(1, 8):
    quantidade = float(input("Informe o consumo em kg: "))
    
    total += quantidade
    
    if produto == 1:
        maior = quantidade
        produto_maior = produto
    
    else:
        if quantidade > maior:
            maior = quantidade
            produto_maior = produto

print("Consumo total:", total, "kg")
print("Produto com maior consumo:", produto_maior)
print("Maior consumo registrado:", maior, "kg")