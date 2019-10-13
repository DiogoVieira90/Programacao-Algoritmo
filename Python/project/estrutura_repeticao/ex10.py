# 10) - Faça um algoritmo que receba “N” números e mostre positivo, negativo ou zero para cada número.

continuar = True

while continuar == True:
    num = int(input("Digite um número: "))

    if num == 0:
        print("0 ZERO.")
    elif num < 0:
        print(f"{num} é negativo.")
    elif num > 0:
        print(f"{num} é positivo.")

    resp = input("Informar outro número? (S)im ou (N)ão? ")
    if resp.upper() == 'S':
        continuar = True
    else:
        continuar = False