def dinheiro(money ,custo):
    compra = money - custo
    if(compra < 0):
        diferença = custo - money
        return (f"seu dinheiro é insificiente, seu pobre, e falta :{diferença} Reais")
    else:
        return (f"seu dinheiro é suficiente, seu rico!")
a = int(input("quanto dinheiro voce tem?: "))
b = int(input("quanto dinheiro voce precisa gastar?: "))
print(dinheiro(a,b))