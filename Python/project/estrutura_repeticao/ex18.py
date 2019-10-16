# 18) - Faça um algoritmo que calcule o valor da conta de luz de 30 pessoas.
# Sabe-se que o cálculo da conta de luz segue a tabela abaixo:
#
# Tipo de Cliente		Valor do KW/h
# 1 (Residência)		R$ 0,60
# 2 (Comércio)		    R$ 0,48
# 3 (Indústria)		    R$ 1,29

for vezes in range(30):
    cliente = input("Tipo de cliente:\n(R)esidência\n(C)omércio\n(I)ndústria\n")

    if cliente.upper() == 'R':
        valor = 0.60 * 24 *30
        print(f"\nValor da conta R$ {valor}")
    elif cliente.upper() == 'C':
        valor = 0.48 * 24 *30
        print(f"\nValor da conta R$ {valor}")
    else:
        valor = 1.29 * 24 *30
        print(f"\nValor da conta R$ {valor}")