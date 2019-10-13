# 5) - Escrever um algoritmo para uma empresa que decide dar um reajuste a seus 584 funcionários
# de acordo com os seguintes critérios:

# 	a) 50% para aqueles que ganham menos do que três salários mínimos;
# 	b) 20% para aqueles que ganham entre três até dez salários mínimos;
# 	c) 15% para aqueles que ganham acima de dez até vinte salários mínimos;
# 	d) 10% para os demais funcionários.

# 	Leia o nome do funcionário, seu salário e o valor do salário mínimo.
# 	Calcule o seu novo salário reajustado.
# 	Escrever o nome do funcionário, o reajuste e seu novo salário. Calcule quanto à empresa
# 	vai aumentar sua folha de pagamento.

salMin = float(998.00)
folhaPagamento = float(0)

for funcionario in range (1, 585):
    nome = input("\n Informe o nome do funcionário: ")
    salario = float(input("Informe o salário fo funcionário: "))

    if salario < salMin * 3:
        aumento = salario * 50 / 100
        novoSalario = salario + aumento
    elif salario > salMin * 3 and salario < salMin * 10:
        aumento = salario * 20 / 100
        novoSalario = salario + aumento
    elif salario > salMin * 10 and salario < salMin * 20:
        aumento = salario * 15 / 100
        novoSalario = salario + aumento
    else:
        aumento = salario * 10 / 100
        novoSalario = salario + aumento

    folhaPagamento = folhaPagamento + aumento
    print(f"\n O reajuste do(a) funcionário(a) {nome}  foi de R$ {aumento} \n e seu novo salário é R$ {novoSalario} \n o aumento "
          f"na folha de pagamento da empresa é de R$ {folhaPagamento} ")
