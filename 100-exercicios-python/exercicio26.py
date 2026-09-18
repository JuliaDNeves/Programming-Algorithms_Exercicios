print ("Este programa irá ler o salário atual e informar o novo salário de acordo com a tebela de reajuste")
print ("--------------------------------\n")

salario = float(input("Salário atual: R$ "))

if salario <= 1500:
    percentual = 15
elif salario <= 3000:
    percentual = 10
else:
    percentual = 5

aumento = salario * percentual / 100
novo_salario = salario + aumento

print(f"\nPercentual aplicado: {percentual}%")
print(f"Valor do aumento: R$ {aumento:.2f}")
print(f"Novo salário: R$ {novo_salario:.2f}")