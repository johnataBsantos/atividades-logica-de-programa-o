lista = []
listapar = []
i=0
for x in range(1,11):
    num = int(input(f"escreva o {i+1} numero: "))
    lista.append(num)
    i+=1
i=0
for q in lista:
    if(lista[i] % 2 == 0 ):
        listapar.append(lista[i])
    i+=1
print(listapar)