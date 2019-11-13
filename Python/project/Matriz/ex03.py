# 3) - Crie um algoritmo que leia os elementos de uma matriz inteira de 8 X 8 e imprima as seguintes informações:
# 	a)	A soma dos elementos da matriz;
# 	b)	A soma dos elementos da matriz cujo seu valor é par;
# 	c)	A soma dos elementos da matriz cujo seu valor é ímpar;

mat = []
dados = []
soma = 0
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
            somapar += mat[linha][coluna]
        else:
            somaimpar += mat[linha][coluna]

soma = somapar + somaimpar

print(f"A soma dos elementos da matriz é  {soma}")
print(f"A soma dos elementos pares da matriz é  {somapar}")
print(f"A soma dos elementos impares da matriz é  {somaimpar}")