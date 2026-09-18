print ("Este programa irá ler o número e informar se ele é divisível por 3, 5, ambos ou nenhum deles. ")
print ("--------------------------------\n")

numero = int(input("Digite um número inteiro: "))

if numero % 3 == 0 and numero % 5 == 0:
    print("Divisível por 3 e 5")

elif numero % 3 == 0:
    print("Divisível apenas por 3")

elif numero % 5 == 0:
    print("Divisível apenas por 5")

else:
    print("Não divisível por 3 nem 5")
