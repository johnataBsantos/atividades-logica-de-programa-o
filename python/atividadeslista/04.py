soma = 0
i=0
listasem = ["seg","ter","qua","qui","sex","sab","dom"]
lista = []
for x in range (1,8):
    y = int(input(f"qual é a temperatura de {listasem[i]}: "))
    lista.append(y)
    i+=1
i=0
menor = lista[0]
maior = lista[0]
for x in range (1,8):
    if(lista[i] < menor):
        menor = lista[i]
    if(lista[i] > maior):
        maior = lista[i]
    soma = soma + y
    i+=1
media = soma/7
print(f"a maior temperatura foi {maior}")
print(f"a menor temperatura foi {menor}")
print(f"e a media das temperaturas foi {media}")