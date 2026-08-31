temperatura = float(input("Quantos graus faz agora? "))

chovendo = False

if temperatura > 25 and not chovendo:
    print("Sugestão: Ótimo dia para ir à praia!")
elif temperatura < 15 or chovendo:
    print("Sugestão: Que tal um filme em casa?")
else:
    print("Sugestão: O tempo está agradável.")