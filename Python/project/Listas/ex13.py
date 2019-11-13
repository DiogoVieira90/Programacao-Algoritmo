# 13) - Desenvolva um programa em python que leia 15 valores informado pelo usuário e
# cadastre-os em uma lista. O usuário deverá informar um valor a ser procurado no vetor, caso
# encontre este valor exiba o índice desse elemento.

lista = []
check = 0

for cont in range(5):
    lista.append(input(f"Informe o {cont + 1}° valor: "))

check = input("Digite o valor a ser encontrado: ")

if check in lista:
    print(f"O indice do elemento {check} é: {lista.index(check)}")