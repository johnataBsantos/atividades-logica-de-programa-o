codeT = int(input("digite seu código de empregado: "))
anosT = float(input("quantos anos você tem trabalhado na empresa: "))
anosI = float(input("quantos anos você tem no total: "))
if (anosI >= 65 or anosT >= 30 or(anosI >= 60 and anosT >= 25)):
    print(f"requerer aposentadoria: {codeT}")
else:
    print(f"Não requerer. {codeT}")