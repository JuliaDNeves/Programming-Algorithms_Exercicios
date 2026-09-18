print ("Este programa irá ler o número e informar se ele está no intervalo entre 10 e 20")
print ("--------------------------------\n")


numero = float(input("Digite um número real: "))

if numero >= 10 and numero <= 20:
    print("O número está dentro do intervalo")
else:
    print("O número está fora do intervalo")