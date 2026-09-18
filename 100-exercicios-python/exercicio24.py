print ("Este programa irá ler um ano e informar se ele é bissexto")
print ("--------------------------------\n")

ano = int(input("Ano: "))

if ano % 400 == 0 or (ano % 4 == 0 and ano % 100 != 0):
    print("É ano bissexto")
else:
    print("Não é ano bissexto")