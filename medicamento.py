nome = ""
vb = float("inf")  
tp = 0 

for med in range(5):  
    medicamento = input(f"Digite o nome do medicamento {med + 1}: ")
    preco = float(input(f"Digite o preço do medicamento {med + 1}: "))
    
    if preco < vb: 
        nome = medicamento
        vb = preco
    
    tp += preco  

media = tp / 5 

print(f"O medicamento mais barato é {nome} com o preço de R$ {vb:.2f}")
print(f"A média dos preços é R$ {media:.2f}")
