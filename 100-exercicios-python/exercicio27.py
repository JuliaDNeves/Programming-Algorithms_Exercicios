print ("Este programa irá ler o peso e a altura do usuário e irá indicar a faixa do IMC")
print ("--------------------------------\n")

peso = float(input("Peso: "))
altura = float(input("Altura: "))

imc = peso / (altura * altura)

if imc < 18.5:
    classificacao = "Abaixo da faixa"

elif imc < 25:
    classificacao = "Faixa normal"

elif imc < 30:
    classificacao = "Acima da faixa"

else:
    classificacao = "Faixa elevada"

print(f"\nIMC: {imc:.2f}")
print(f"Classificação: {classificacao}")