list = []
def vogais (palavra):
    i=0
    y=0
    t=0
    for x in palavra:
        list.append(x)
    for x in list:
        if(list[i]=="a" or list[i]=="e" or list[i]=="i" or list[i]=="o" or list[i]=="u"):
            y+=1
        if(list[i]=="A" or list[i]=="E" or list[i]=="I" or list[i]=="O" or list[i]=="U"):
            t+=1
        i+=1
    print(f"a sua palavra tem \n{y} vogais minusculas e \n{t} vogais maiusculas")
palavra = input("qual palavra voce escolhe?: ")
vogais(palavra)