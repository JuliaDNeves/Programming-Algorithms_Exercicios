print("Este programa irá ler o valor de um imóvel, o salário e o prazo de pagamento.")
print("O empréstimo será aprovado se a prestação não ultrapassar 30% do salário")
print ("--------------------------------\n")

valor = float(input("Valor do imóvel: R$ "))
salario = float(input("Salário: R$ "))
anos = int(input("Prazo: "))

prestacao = valor / (anos * 12)
limite = salario * 0.30

if prestacao <= limite:
    resultado = "APROVADO"
else:
    resultado = "REPROVADO"

print(f"\nPrestação: R$ {prestacao}")
print(f"Limite: R$ {limite}")
print(f"Resultado: {resultado}")

