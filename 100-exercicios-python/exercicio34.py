print ("Este programa irá ler o número do mês e informar quantos dias ele tem")
print ("--------------------------------\n")

mes = int(input("Digite o número do mês: "))
ano = int(input("Digite o ano: "))

if mes < 1 or mes > 12:
    print("Mês inválido")

elif mes == 2:
    if (ano % 400 == 0) or (ano % 4 == 0 and ano % 100 != 0):
        print("O mês possui 29 dias")
    else:
        print("O mês possui 28 dias")

elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
    print("O mês possui 30 dias")

else:
    print("O mês possui 31 dias")