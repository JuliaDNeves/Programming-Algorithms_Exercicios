print ("Este programa irá calcular o valor do ingresso de acordo com a idade ou se é estudante")
print ("--------------------------------\n")

idade = int(input("Idade: "))
estudante = input("Estudante (sim/nao): ")

valor = 30.00

if idade < 12 or estudante == "sim" or idade >= 60:
    valor = valor / 2

print(f"\nValor do ingresso: R$ {valor}")