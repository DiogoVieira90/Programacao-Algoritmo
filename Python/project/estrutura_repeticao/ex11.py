# 11) Uma Companhia de Seguros possui nove categorias de seguro baseadas na idade e
# ocupação do segurado. Somente pessoas com pelo menos 17 anos e não mais de 70 anos podem
# adquirir apólices de seguro. Quanto às classes de ocupações, foram definidos três grupos
# de risco. A tabela abaixo fornece as categorias em função da faixa etária e do grupo de
# risco. Dados nome, idade e grupo de risco, determinar a categoria do pretendente à aquisição
# de tal seguro. Imprimir o nome a idade e a categoria do pretendente e caso a idade não esteja
# na faixa necessária, imprimir uma mensagem.
#
# 	GRUPO DE RISCO
# 	IDADE		BAIXO		MEDIO		ALTO
# 	17 A 20		1			2			3
# 	21 A 24		2			3			4
# 	25 A 34		3			4			5
# 	35 A 64		4			5			6
# 	65 A 70		7			8			9

continuar = True

while continuar == True:
    nome = input("Digite o nome: ")
    idade = int(input("Informe a idade: "))

    if idade >= 17 and idade <= 70:

        if idade >= 17 and idade <= 20:
            print(f"Pretendente: {nome}\nIdade: {idade}\n Categoria:  ")
