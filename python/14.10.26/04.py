Mokilo = float(input("quantos kilos de morangos foram comprados? "))
Makilo = float(input("quantos kilos de maçãs foram comprados? "))
Mopreco = 2.5 * Mokilo
Mapreco = 1.8 * Makilo
if (Mokilo > 5):
    Mopreco = Mokilo * 2.2
if (Makilo > 5):
    Mapreco = Makilo * 1.5
precoT = Mopreco + Mapreco
if (Mokilo + Makilo > 8 or Mapreco + Mopreco > 25):
    precoT = precoT * 0.9
print(f"preço total: {precoT}")