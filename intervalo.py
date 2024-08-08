a = int(input("Digite o primeiro numero: "))
b = int(input("Digite o segundo numero: "))

if a < b:
    soma = sum(range(a, b))
    print(f"A soma dos números inteiros no intervalo [{a}, {b}] é: {soma}")
else:
    print("erro")
