H1 = int(input("digite a idade do homem1:"))
H2 = int(input("digite a idade do homem2:"))
M1 = int(input("digite a idade da mulher1:"))
M2 = int(input("digite a idade da mulher2:"))
if (H1 > H2):
    HmaisV = H1
    HmaisN = H2
else:
    HmaisV = H2
    HmaisN = H1
if (M1 > M2):
    MmaisV = M1
    MmaisN = M2
else:
    MmaisV = M1
    MmaisN = M2
print (f"soma do homem mais velho com mulher mais nova: {HmaisV + MmaisN}",f"\nproduto do homem mais novo com mulher mais velha: {HmaisN * MmaisV}")
