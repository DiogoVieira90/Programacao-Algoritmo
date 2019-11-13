# 4) - Crie um algoritmo que leia os elementos de uma matriz inteira de 10 X 10 e imprima as seguintes informações:
# 	a)	A soma dos elementos onde a soma do índice da linha + o índice da coluna for par;
# 	b)	A soma dos elementos onde a soma do índice da linha + o índice da coluna for ímpar;
# 	c)	A quantidade de valores pares na matriz;
# 	d)	A quantidade de valores ímpares na matriz;

mat = []
dados = []
qtdpar = 0
qtdimpar = 0
somapar = 0
somaimpar = 0

for linha in range(3):
    for coluna in range(3):
        dados.append(int(input(f"Informe o elemento da matriz [{linha}][{coluna}]")))
    mat.append(dados)
    dados = []

for linha in range(3):
    for coluna in range(3):
        print(mat[linha][coluna], end=" ")
    print()

for linha in range(3):
    for coluna in range(3):
        if mat[linha][coluna] % 2 == 0:
            qtdpar += 1
        else:
            qtdimpar += 1
print(f"Quantidade de elementos pares: {qtdpar}")
print(f"Quantidade de elementos impares: {qtdimpar}")