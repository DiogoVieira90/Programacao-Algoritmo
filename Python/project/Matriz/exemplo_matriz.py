mat = []
dados = []

for linha in range(0,3,1):
    for coluna in range(0,3,1):
        dados.append(int(input(f"Informe o elemento da matriz[{linha} , {coluna}] : ")))
    mat.append(dados)
    dados = []

for linha in range(3):
    for coluna in range(3):
        print(mat[linha][coluna], end=" ")
    print()

print("Elementos da Diagonal Principal")
for linha in range(3):
    for coluna in range(3):
        if linha == coluna:
            print(mat[linha][coluna], end="")
        else:
            print("  ", end="")
    print()