print ("Este programa irá identificar se um número é positivo, negativo ou igual a zero")
print ("--------------------------------\n")

num = int(input("Digite um número: "))

if num >= 1:
    print("Este é um número positivo")
elif num == 0:
    print("Este número é zero, portanto não é nem positivo, nem negativo")
else:
    print("Este é um número negativo")