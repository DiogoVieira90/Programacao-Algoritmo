# 13.	Um determinado clube de futebol pretende classificar seus atletas em categorias e para isto ele contratou um
# programador para criar um programa que executasse esta tarefa. Para isso o clube criou uma tabela que continha a
# faixa etária do atleta e sua categoria. A tabela está demonstrada abaixo:

# IDADE 		CATEGORIA
# De 05 a 10	Infantil
# De 11 a 15	Juvenil
# De 16 a 20 	Junior
# De 21 a 25 	Profissional
# Construa um programa que solicite o nome e a idade de um atleta e imprima a sua categoria.

nome = input("Digite o nome: ")
idade = int(input("Digite a idade: "))

if idade >= 5 and idade <= 10:
    print("Categoria Infantil.")
elif idade >= 11 and idade <= 15:
    print("Categoria juvenil.")
elif idade >= 16 and idade <= 20:
    print("Categoria Junior.")
elif idade >= 21 and idade <= 25:
    print("Categoria Profissional.")