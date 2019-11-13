# 9) - Desenvolva um programa em python que leia 10 valores numéricos informados pelo usuário e armazene-os em
# um vetor A, leia mais 10 valores numéricos informado pelo usuário armazene-os em outro vetor B, Gere um
# vetor C, que receberá a soma dos elementos do vetor A e B na sua respectiva posição. Ao final
# exibir os três vetores A, B e C.

listaA = []
listaB = []
listaC = []

for cont in range(5):
    listaA.append(int(input(f"Informe o {cont + 1}° valor para a lista A: ")))

for cont in range(5):
    listaB.append(int(input(f"Informe o {cont + 1}° valor para a lista B: ")))

for cont in range(5):
    listaC.append(listaA[cont] + listaB[cont])

print(f"Lista A {listaA}")
print(f"Lista B {listaB}")
print(f"Lista C {listaC}")