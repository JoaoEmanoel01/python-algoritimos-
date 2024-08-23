produtos = []
while True:
    nome = input("Qual é o produto: ")
    produtos.append(nome)
    resp = input("Tem mais alguma produto: [S|N]? ")
    if resp.upper() == "N":
        break
print(produtos)


