print ("Este programa irá ler três valores e informar se eles formam um triângulo")
print ("Se formarem, identificará que tipo de triângulo irá formar")
print ("--------------------------------\n")

a = float(input("Lado 1: "))
b = float(input("Lado 2: "))
c = float(input("Lado 3: "))

if a < b + c and b < a + c and c < a + b:

    if a == b and b == c:
        print("Formam um triângulo equilátero")

    elif a == b or a == c or b == c:
        print("Formam um triângulo isóceles")

    else:
        print("Formam um triângulo escaleno")

else:
    print("Não formam um triângulo")