print ("Este programa irá ler um preço e calcular o valor final conforme a opção selecionada")
print ("--------------------------------\n")

preco = float(input("Preço: "))

print("\n1 - Dinheiro ou Pix (10% de desconto)")
print("2 - Débito (5% de desconto)")
print("3 - Crédito à vista (sem alteração)")
print("4 - Crédito parcelado (8% de acréscimo)")

opcao = int(input("\nSelecione uma opção: "))

if opcao == 1:
    valor_final = preco - (preco * 0.10)

elif opcao == 2:
    valor_final = preco - (preco * 0.05)

elif opcao == 3:
    valor_final = preco

elif opcao == 4:
    valor_final = preco + (preco * 0.08)

print(f"Valor final: R$ {valor_final:.2f}")