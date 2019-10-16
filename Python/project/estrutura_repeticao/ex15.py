# 15) - Desenvolva um algoritmo que receba um valor como limite inicial e outro valor como limite final.
#       Ao final exibir quantos valores no intervalo informados são pares e ímpares.

valorMin = int(input("Digite o valor mínimo: "))
valorMax = int(input("Digite o valor máximo: "))
pares = 0
impares = 0

for numero in range(valorMin, valorMax + 1):
    resto = numero % 2
    if resto == 0:
        pares = pares + 1
    else:
        impares = impares + 1

print(f"{pares} números Pares\n{impares} números impares.")