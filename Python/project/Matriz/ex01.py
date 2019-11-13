# 1) - Criar um algoritmo que leia os elementos de uma matriz inteira de 5 X 5 e imprima a matriz
# (em forma de matriz).

mat = []
dados = []

for linha in range(6):
    for coluna in range(6):
        dados.append(int(input(f"Informe o valor para o elemento [{linha}][{coluna}] : ")))
    mat.append(dados)
    dados = []

for linha in range(6):
    for coluna in range(6):
        print(mat[linha][coluna], end=" ")
    print()