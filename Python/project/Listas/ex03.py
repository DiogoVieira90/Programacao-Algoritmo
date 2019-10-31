# 3) - Desenvolva um programa em python que receba 15 valores informados pelo usuário armazene-os em vetor chamado num,
# e imprima uma listagem numerada contendo a seguinte mensagem "Par" ou "Ímpar" de
# acordo com os valores cadastrados no vetor.

num []

for cont in range(15):
    num.append(int(input(f"Informe o {cont + 1}º valor: ")))

for n in num:
    if n % 2 == 0:
        print("Par")
    else:
        print("Impar")