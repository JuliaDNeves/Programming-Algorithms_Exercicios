print ("Este programa irá ler a idade e informar a categoria de votação")
print ("--------------------------------\n")

idade = int(input("Digite sua idade: "))

if idade < 16:
    print("NÃO PODE VOTAR")

elif idade < 18:
    print("VOTO OPCIONAL")

elif idade < 70:
    print("VOTO OBRIGATÓRIO")

else:
    print("VOTO OPCIONAL")