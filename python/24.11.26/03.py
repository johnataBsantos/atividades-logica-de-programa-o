def calculo(numero):
    if(numero % 2 == 0):
        return "true"
    else:
        return "false"
numero = int(input("escreva um número\n:"))
print(calculo(numero))