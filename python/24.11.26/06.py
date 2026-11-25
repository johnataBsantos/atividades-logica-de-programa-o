i=0
listanum = []
listapares = []
def filtro(listanum):
    i=0
    for x in listanum:
        if(listanum[i] % 2 == 0):
            listapares.append(listanum[i])
        i+=1
for x in range(10):
    i=0
    listanum[i] = int(input("digite dez números:\n>"))
    i+=1
print(f"os números pares da sua lista:\n> {listapares}")