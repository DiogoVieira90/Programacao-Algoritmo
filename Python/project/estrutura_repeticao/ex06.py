# 6) - A concessionária de veículos “CARANGO VELHO” está vendendo os seus veículos com desconto. Faça
# um algoritmo que calcule e exiba o valor do desconto e o valor a ser pago pelo cliente de vários carros.
# O desconto deverá ser calculado de acordo com o ano do veículo. Até 2000 - 12% e acima de 2000 - 7%. O sistema
# deverá perguntar se o usuário deseja continuar calculando desconto até que a resposta seja: “(N) Não”. Informar
# total de carros com ano até 2000 e total geral.

continuar = True
carroAntigo = 0
qtdVeiculos = 0

while continuar == True:
    valor = float(input("Digite o Valor do veículo: "))
    ano = int(input("Informe o ano do veículo: "))
    if ano <= 2000:
        desconto = valor * 12 / 100
        total = valor - desconto
        carroAntigo = carroAntigo + 1
        qtdVeiculos = qtdVeiculos + 1
    else:
        desconto = valor * 7 / 100
        total = valor - desconto
        qtdVeiculos = qtdVeiculos + 1

    print(f"O desconto é de R$ {desconto} e o total a pagar é R$ {total}")
    resp = input("Deseja consultar outro veículo? (S)im ou (N)ão? ")
    if resp.upper() == 'S':
        continuar = True
    else:
        continuar = False

print(f"O total de carros consultados foram {qtdVeiculos}. \n{carroAntigo} deles são do ano 2000 ou anterior.")