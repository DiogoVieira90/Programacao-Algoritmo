# 8) Faça um algoritmo que receba o nome a idade e o sexo de dez funcionário. Para cada funcionário
# mostre o nome e o salário líquido:

# 	SEXO	IDADE	SALÁRIO LÍQUIDO
# 	M		>= 30	R$ 100,00
# 	M		< 30	R$ 50,00
# 	F		>= 30	R$ 200,00
# 	F		< 30	R$ 80,00

for funcionario in range(1, 11):
    nome = input("Informe o nome do(a) funcionário(a): ")
    idade = int(input("Informe a idade do(a) funcionário(a): "))
    sexo = input("Informe o sexo do(a) funcionário(a): ")

    if sexo.upper() == 'M':
        if idade >= 30:
            salario = 100.0
        else:
            salario = 50.0
    elif idade >= 30:
        salario = 200.0
    else:
        salario = 80.0

    print(f"\nFuncionário {nome}\nSalário R$ {salario}")