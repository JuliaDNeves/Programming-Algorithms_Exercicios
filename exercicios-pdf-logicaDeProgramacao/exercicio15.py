precoUnitario = float(input("O valor unitário do produto é: "))
qnt = int(input("Quantidade de produtos: "))

frete = float(input("Frete: "))
subtotal = precoUnitario * qnt

total = subtotal + frete

print(f"Preço Unitário: {precoUnitario}\nQuantidade: {qnt}\nFrete: {frete}\nSubtotal: {subtotal}\nValor Final: {total}")