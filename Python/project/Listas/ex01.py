# 1) - Desenvolva um programa em python que receba 10 valores
# # informados pelo usuário, armazene-os em um vetor, depois exiba os dados do vetor.

valores = []

for cont in range(1,11,1):
    valores.append(int(input(f"Informe o {cont}º valor: ")))
print(valores)