# Escreva um algoritmo que leia 3 valores
# inteiros (considere que não serão informados valores iguais) e escrevê-los em ordem crescente.

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o terceiro número: "))

if num1 < num2 and num1 < num3:
    menor = num1
elif num1 > num2 and num1 > num3:
    maior = num1
else:
    medio = num1

if num2 < num1 and num2 < num3:
    menor = num2
elif num2 > num1 and num2 > num3:
    maior = num2
else:
    medio = num2

if num3 < num2 and num3 < num1:
    menor = num3
elif num3 > num2 and num3 > num1:
    maior = num3
else:
    medio = num3

print(f"{menor} {medio} {maior}")