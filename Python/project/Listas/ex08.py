# 8) - Desenvolva um programa em python que receba 10 valores numéricos e guarde-os em uma lista.
# Verifique se os valores cadastrados são pares ou ímpares e cadastre os valores pares em uma nova
# lista e os ímpares em outra lista. No final exibir o conteúdo das três listas.

valor = []
valorpar = []
valorimpar = []

for cont in range(10):
    valor.append(int(input("Informe o valor: ")))

for x in valor:
    if x % 2 == 0:
        valorpar.append(x)
    else:
        valorimpar.append(x)

print(valor)
print(valorpar)
print(valorimpar)
