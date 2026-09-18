print ("Este programa irá ler três valores e informar se eles formam um triângulo")
print ("--------------------------------\n")

a = float(input("Lado 1: "))
b = float(input("Lado 2: "))
c = float(input("Lado 3: "))

if a < b + c and b < a + c and c < a + b:
    print("Formam um triângulo")
else:
    print("Não formam um triângulo")