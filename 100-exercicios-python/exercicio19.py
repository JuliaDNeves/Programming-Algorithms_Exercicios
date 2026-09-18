print ("Este programa irá ler três números e identificar qual o maior e o menor entre eles")
print ("--------------------------------\n")

primeiro = float(input("Primeiro valor: "))
segundo = float(input("Segundo valor: "))
terceiro = float(input("Terceiro valor: "))

if primeiro >= segundo and primeiro >= terceiro:
    maior = primeiro
elif segundo >= primeiro and segundo >= terceiro:
    maior = segundo
else:
    maior = terceiro

if primeiro <= segundo and primeiro <= terceiro:
    menor = primeiro
elif segundo <= primeiro and segundo <= terceiro:
    menor = segundo
else:
    menor = terceiro

print(f"\nMaior valor: {maior}")
print(f"Menor valor: {menor}")