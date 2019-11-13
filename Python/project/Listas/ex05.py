# 5) - Desenvolva um programa em python que leia 30 valores inteiros e armazene-os em um vetor. Exiba os valores do vetor
# ao contrário da ordem de leitura dos valores.

numeros = []

for cont in range (30):
    numeros.append(int(input(f"Informe o {cont + 1}° valor: ")))

for numero in numeros:
    print(numeros[-numero])