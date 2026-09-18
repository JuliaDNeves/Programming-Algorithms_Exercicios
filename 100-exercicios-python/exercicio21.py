print ("Este programa irá calcular a média e informar se o aluno foi aprovado ou reprovado")
print ("--------------------------------\n")

nota1 = float(input("Nota 1: "))
nota2 = float(input("Nota 2: "))

media = (nota1 + nota2) / 2

if media >= 7:
    print(f"Média: {media}")
    print("Situação: APROVADO")
else:
    print(f"Média: {media}")
    print("Situação: REPROVADO")

