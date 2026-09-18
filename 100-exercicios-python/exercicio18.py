print ("Este programa irá ler dois valores e identificar qual deles é o maior. Se ambos forem iguais, não haverá diferença entre eles")
print ("--------------------------------\n")

valor1 = float(input("Digite o primeiro valor: "))
valor2 = float(input("Digite o segundo valor: "))

if valor1>valor2:
    print(f"O maior valor é: {valor1}")
elif valor2>valor1:
    print(f"O maior valor é: {valor2}")
else: 
    print(f"Os valores são iguais, portanto existe um maior")