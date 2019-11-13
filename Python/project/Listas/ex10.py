# 10) - Desenvolva um programa em python que leia 10 valores inteiros informado
# pelo usuário. No final exibir o menor valor cadastrado no vetor.

lista = []

for cont in range(10):
    lista.append(int(input(f"Informe o {cont + 1}° valor: ")))
print(min(lista))