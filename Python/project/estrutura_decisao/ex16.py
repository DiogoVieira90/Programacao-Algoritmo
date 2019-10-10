# Escreva um algoritmo que leia 3 valores
# inteiros (considere que não serão informados valores iguais) e escrever a soma dos 2 maiores.

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o terceiro número: "))

if num1 < num2 and num1 < num3:
    soma = num2 + num3
    print(f"a soma dos 2 maiores números é {soma}.")
elif num2 < num1 and num2 < num3:
    soma = num1 + num3
    print(f"a soma dos 2 maiores números é {soma}.")
else:
    soma = num1 + num2
    print(f"a soma dos 2 maiores números é {soma}.")