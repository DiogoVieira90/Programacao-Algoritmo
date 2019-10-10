# 6.	De acordo com a tabela abaixo, desenvolva um algoritmo que
# leia um código do produto informado pelo usuário e informe a descrição do lanche.

# CÓDIGO	DESCRIÇÃO DO PRODUTO
# 100		X-Salada com coca-cola.
# 200		Hot dog com suco de laranja
# 300		Sanduiche natural com suco de uva.
# 400		Misto Quente com fanta laranja.
# 500		Pão com manteiga com café.
# 600		Pão com manteiga na chapa com café com leite.
# 		Qualquer outro código diferente dos códigos da tabela, informar a mensagem "Código informado inválido."

codigo = int(input("Digite o código"))

if codigo == 100:
    print("X-Salada com coca-cola.")
elif codigo == 200:
    print("Hot dog com suco de laranja.")
elif codigo == 300:
    print("Sanduiche naturalcom suco de uva.")
elif codigo == 400:
    print("Misto Quente com fanta laranja.")
elif codigo == 500:
    print("Pão com manteiga com café.")
elif codigo == 600:
    print("Pão com manteiga na chapa com café com leite.")
else:
    print("Código informado inválido.")