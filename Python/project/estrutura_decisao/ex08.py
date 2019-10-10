# Escrever um algoritmo que leia dois valores inteiros distintos e informe qual é o maior.

val1 = int(input("Digite o primeiro número: "))
val2 = int(input("Digite o segundo número: "))

if val1 > val2:
    print(f"O número {val1} é o maior.")
elif val1 < val2:
    print(f"O número {val2} é maior.")
else:
    print("Os números são iguais.")