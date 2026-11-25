lista = ["cocolandia","escola","minha vida","minha casa","lixão","rolândia","simolandia","casa do joão matheus","pindamonhangaba","maracanaú","pajuçara","velha york", "nova york","brookhaven","ilha do fortnite","ceará","todas","brasil","cova do joão matheus","casa do rodolfo teófilo","flamenguinho","simolandia do MAL"]
i=0
w=0
q = str(input("digite sua cidade para buscar ela na lista\n:"))
for x in lista:
    if(q == lista[i]):
        w =1
        indice = lista.index(q)
        break
    i+=1
if(w != 0):
    print(f"sua cidade foi encontrada! índice: {indice}")
else:
    print("cidade não encontrada.")