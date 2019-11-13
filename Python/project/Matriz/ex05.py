# 5) - Entrar com valores para uma matriz A [3X4] gere e exiba uma matriz B que é o triplo da matriz A.

matA = []
dadosA = []
matB = []
dadosB = []

for linha in range(3):
    for coluna in range(3):
        dadosA.append(int(input(f"Informe o elemento da matriz [{linha}][{coluna}]")))
    matA.append(dadosA)
    dadosA = []

for linha in range(3):
    for coluna in range(3):
        print(matA[linha][coluna], end=" ")
    print()

for linha in range(3):
    for coluna in range(3):
        dadosB.append(matA[linha][coluna] * 3)
    matB.append(dadosB)
    dadosB = []

print()
for linha in range(3):
    for coluna in range(3):
        print(matB[linha][coluna], end=" ")
    print()