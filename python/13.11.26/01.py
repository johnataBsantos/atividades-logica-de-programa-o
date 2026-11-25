i=1
soma=0
listames = ["janeiro","fevereiro","março","abril","maio","junho","julho","agosto","setembro","outubro","novembro","dezenmbro"]
listatemp = []
for o in listames: 
    cavalo = int(input(f"me fala a temperatura do mes:  {i}\n"))
    listatemp.append(cavalo)
    i=i+1
i=0
for u in listatemp:
    soma = soma + listatemp[i]
    i=i+1
media = soma/12
i=0
print(f"a media anual da temperatura foi de: {media}\n")
for x in listames:
    if(listatemp[i] > media):
        print(f"{listames[i]} é maior que a media com a temperatura de: {listatemp[i]}")
    else:
        print(f"{listames[i]} é menor que a media com a temperatura de: {listatemp[i]}")
    i=i+1