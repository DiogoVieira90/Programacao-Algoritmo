# 2) - Desenvolva um algoritmo que leia os elementos de uma matriz
# inteira de 5 X 5 e imprima a soma dos elementos da matriz.

mat = []
dados = []

for linha in range(3):
    for coluna in range(3):
        dados.append(int(input(f"Informe o elemento da matriz [{linha}][{coluna}]")))
    mat.append(dados)
    dados = []

for linha in range(3):
    for coluna in range(3):
        print(mat[linha][coluna], end=" ")
    print()

soma = 0
for linha in range(3):
    for coluna in range(3):
        soma += mat[linha][coluna]

print(f"A soma dos elementos da matriz é {soma}")