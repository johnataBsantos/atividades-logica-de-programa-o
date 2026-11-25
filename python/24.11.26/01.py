hora = "bom dia"
def saudacao(nome,hora):
    if(horario >= 12 and horario <= 18):
        hora = "boa tarde"
    if(horario > 18):
        hora = "boa noite"
    print(f"{hora}, {nome}") 
nome = str(input("escreva o seu nome: "))
horario = int(input("escreva que horas é: "))
saudacao(nome,hora)
    
