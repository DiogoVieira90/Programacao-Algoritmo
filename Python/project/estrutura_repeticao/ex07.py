# 7) - 6.	Faça um algoritmo que receba o preço de custo e o preço de venda de 40 produtos. Mostre
# como resultado se houve lucro, prejuízo ou empate para cada produto. Informe média de preço de
# custo e do preço de venda.

mediaCompra = float(0)
mediaVenda = float(0)

for produto in range(1, 41):
    valorCompra = float(input("Informe o preço de custo do produto: "))
    valorVenda = float(input("Informe o preço de vencda do produto: "))
    if valorCompra > valorVenda:
        print("Prejuízo.")
    elif valorCompra < valorVenda:
        print("Lucro.")
    else:
        print("Não houve lucro nem prejuízo.")
    mediaCompra = mediaCompra + valorCompra
    mediaVenda = mediaVenda + valorVenda

mediaCompra = mediaCompra / 40
mediaVenda = mediaVenda / 40

print(f"\nO valor da média de compra é de R$ {mediaCompra}\nO valor da média de venda é de R$ {mediaVenda}")