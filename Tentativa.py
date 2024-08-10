senha = 123456
tentativa = 3

for i in range(3):
    ds = float(input("Digite a senha: "))
    
    if ds == senha:
        print("sucesso!")
        exit()
    else:
        trs = tentativa - (i+1)
        if trs > 0:
            print(f"Senha incorreta, você ainda tem {trs} chances")
        else:
            print("Conta bloqueada")
            exit()
