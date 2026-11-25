i=0
lista = []
for x in range(1,6):
    x = str(input(f"me fala o {i+1} itens da lista: "))
    lista.append(x)
    i+=1
print(f"o primeiro item da sua lista é: {lista[0]}")
print(f"e o ultimo item da sua lista é: {lista[-1]}")