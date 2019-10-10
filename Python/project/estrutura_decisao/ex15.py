# Escreva um algoritmo que leia 3 valores inteiros(considere que não serão informados valores iguais)
# # e escrever o maior deles.

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o terceiro número: "))

if num1 > num2 and num1 > num3:
    print(f"{num1} é o maior número.")
elif num2 > num1 and num2 > num3:
    print(f"{num2} é o maior número.")
else:
    print(f"{num3} é o maior número.")