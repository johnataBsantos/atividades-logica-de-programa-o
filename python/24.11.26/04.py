def numeros(a,b,c):
    if (a >= b and a>= c):
        return a
    elif (b >= a and b>= c):
        return b
    else:
        return c
a = int(input("digite um numero\n:"))
b = int(input("digite um numero\n:"))
c = int(input("digite um numero\n:"))
print(numeros(a,b,c))

    