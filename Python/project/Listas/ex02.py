# 2) - Desenvolva um programa em python que receba 10 nomes informados pelo usuário e armazene-os em um vetor
# chamado nomes. No final exiba uma lista numerada com os nomes cadastrados no vetor.

nomes = []

for cont in range(1,11,1):
    nomes.append(input(f"Informe o {cont}º nome: "))

cont = 1
for nome in nomes:
    print(f"{cont} - {nome}")
    cont = cont + 1

