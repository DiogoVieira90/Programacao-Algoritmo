"""
5.	Faça um algoritmo para ler um salário e atualizá-lo de acordo com a tabela abaixo
FAIXA SALARIAL	AUMENTO
Até 600,00			30%
600,01 a 1.100,00	25%
1100,01 a 2.400,00	20%
2400,01 a 3.550,00	15%
Acima de 3.550,00	10%
"""

salario = float(input("Salário do funcionário"))

if salario <= 600.00:
    aumento = salario * 30 / 100
    salarioFinal = salario + aumento
elif salario <= 1100.00:
    aumento = salario * 25 / 100
    salarioFinal = salario + aumento
elif salario <= 2400.00:
    aumento = salario * 20 / 100
    salarioFinal = salario + aumento
elif salario <= 3550.00:
    aumento = salario * 15 / 100
    salarioFinal = salario + aumento
else:
    aumento = salario * 10 / 100
    salarioFinal = salario + aumento
print(f"O novo salário é R$ {salarioFinal}")
