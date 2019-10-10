# 2) - Escrever um algoritmo que leia os dados de “N” pessoas (nome, sexo, idade e saúde) e informe se está apta ou não para cumprir o serviço militar obrigatório. Informe os totais.

continuar = True

while continuar:
    nome = input("Informe o nome: ")
    sexo = input("Informe o sexo (M) ou (F): ")
    idade = input("Informe a idade: ")
    apto = input("Informe seu estado de saúde: (A)pto ou (I)napto: ")

    parar = input("Deseja continuar (S)im ou (N)ão: ")

    if sexo.upper() == 'M' and idade >= 18:
        print(f"")

    if parar.upper()  == 'N' :
        continuar = False