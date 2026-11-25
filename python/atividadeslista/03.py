i = 0
lista = []
for x in range(1,4):
    x = str(input(f"qual é o {i+1} convidado?: "))
    lista.append(x)
    i+=1
i=0
y = str(input("agora fale quem vai morrer: "))
for x in range (1,4):
    if(lista[i] == y):
        lista.remove(y)
    i+=1  
print(lista)

