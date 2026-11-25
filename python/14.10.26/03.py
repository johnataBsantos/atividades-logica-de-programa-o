codeU = int(input("escreva seu código de usuário: "))
if (codeU != 1234):
    print("usuário inválido!")
else:
    codeA = int(input("digite sua senha de acesso: "))
    if (codeA != 9999):
        print("senha inválida!")
    else:
        print("acesso concedido")