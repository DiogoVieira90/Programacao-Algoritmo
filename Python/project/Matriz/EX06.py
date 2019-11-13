# 6) - Considere uma turma com 10 alunos, cada um com 4 notas. Estes dados são  armazenados em uma matriz 10 x 5,
# em que a primeira coluna armazena a matrícula do aluno e as 4 últimas armazenam as suas notas.
# Fazer um algoritmo que:
# 	a) Leia estes dados, armazenando-os;
# 	b) Imprima a média de cada aluno;
# 	c) Imprima a maior média e a matrícula do aluno que a possui;

mat = []
dados = []

for linha in range(11):
    for coluna in range(1):
        dados.append(input(f"Informe o nome do aluno: "))
        for colunax in range(4):
            dados.append(int(input(f"Informe a {colunax + 1}° nota do aluno: ")))
    mat.append(dados)
    dados = []

for linha in range(3):
    for coluna in range(3):
        print(mat[linha][coluna], end=" ")
    print()