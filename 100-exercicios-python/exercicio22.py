print ("Este programa irá calcular a média e informar se o aluno foi aprovado, reprovado ou se está de recuperação")
print ("--------------------------------\n")

nota1 = float(input("Nota 1: "))
nota2 = float(input("Nota 2: "))

media = (nota1 + nota2) / 2

if media < 5:
    print(f"Média: {media}")
    print("Situação: REPROVADO")

elif media < 7:
    print(f"Média: {media}")
    print("Situação: RECUPERAÇÃO")

else:
    print(f"Média: {media}")
    print("Situação: APROVADO")