# Escreva um algoritmo que leia dois valores inteiros e imprimir uma das três mensagens a seguir:
# ‘Números iguais’, caso os números sejam iguais
# ‘Primeiro é maior’, caso o primeiro seja maior que o segundo;
# ‘Segundo maior’, caso o segundo seja maior que o primeiro.

num1 = int(input("Primeiro número: "))
num2 = int(input("segundo número: "))

if num1 == num2:
    print("Número iguais.")
elif num1 > num2:
    print("primeiro número é maior.")
else:
    print("segundo número é maior.")