salario = float(input("Digite o sálario: "))
vendas = float(input("Total vendido: "))

comissao = vendas * 0.04
salarioTotal = salario + comissao

print(f"Seu salário de {salario}, somado à sua comissão de {comissao}, resultará em um salário de {salarioTotal}")