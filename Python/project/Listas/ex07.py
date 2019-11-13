# 7) - Desenvolva um programa em python que receba valores numéricos informado pelo usuário e
# cadastre-os em uma lista, caso a lista já contenha o valor informado, exibir a
# mensagem "Valor já cadastrado". No final exiba todos os valores cadastrados.

valor = []
checka = 0
cont = 0

while cont < 5:
    checka = int(input("Informe o valor a ser adicionado: "))
    if checka in valor:
        print("Valor já cadastrado.")
    else:
        valor.append(checka)
        cont = cont + 1

print(valor)
