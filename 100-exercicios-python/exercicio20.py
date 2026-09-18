print ("Este programa irá ler três números colocá-los na ordem crescente")
print ("--------------------------------\n")

a = int(input("Primeiro valor: "))
b = int(input("Segundo valor: "))
c = int(input("Terceiro valor: "))

if a <= b and b <= c:
    print(f"Ordem crescente: {a}, {b}, {c}")

elif a <= c and c <= b:
    print(f"Ordem crescente: {a}, {c}, {b}")

elif b <= a and a <= c:
    print(f"Ordem crescente: {b}, {a}, {c}")

elif b <= c and c <= a:
    print(f"Ordem crescente: {b}, {c}, {a}")

elif c <= a and a <= b:
    print(f"Ordem crescente: {c}, {a}, {b}")

else:
    print(f"Ordem crescente: {c}, {b}, {a}")
