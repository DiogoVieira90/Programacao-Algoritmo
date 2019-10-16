# 19) - Desenvolva um algoritmo que leia 10 valores e ao final exiba a quantidade de valores múltiplo de 5.

mult = 0

for vezes in range(10):
    numero = int(input("Digite um valor: "))
    rest = numero % 5

    if rest == 0:
        mult = mult + 1

print(f"{mult} desses valores são múltiplos de 5.")
