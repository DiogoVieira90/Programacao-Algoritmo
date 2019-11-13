# 14) - Desenvolva um programa em python que leia o nome e uma nota para um aluno, crie duas listas
# para armazenar estes valores, o usuário deverá informar um nome de aluno para a pesquisar, se o aluno
# existir na lista com os nomes do aluno, exibir o nome e a nota do aluno, caso contrário informar a mensagem "Aluno não cadastrado."

lista_aluno = []
lista_nota = []

for cont in range (3):
    lista_aluno.append(input(f"Informe o nome do {cont + 1}° aluno: "))
    lista_nota.append(float(input(f"Informe a nota do aluno {lista_aluno[cont]} : ")))

check = input("Informe o nome do aluno para pesquisar sua nota: ")

if check in lista_aluno:
    print(f"A nota do aluno {check} é {lista_nota[lista_aluno.index(check)]}")