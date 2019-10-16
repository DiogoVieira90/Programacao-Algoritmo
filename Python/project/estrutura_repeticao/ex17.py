# 17) - A escola “APRENDER” faz o pagamento de seus professores por hora/aula.
# Faça um algoritmo que calcule e exiba o salário do professor.
# Sabe-se que o valor da hora/aula segue a tabela abaixo:

# Professor Nível 1 R$12,00 por hora/aula
# Professor Nível 2 R$17,00 por hora/aula
# Professor Nível 3 R$25,00 por hora/aula
# A escola "APRENDER” possui 50 professores.

for vezes in range(50):
    horas = int(input("Informe a quantidade de horas:"))
    nivel = int(input("Informe o nível do(a) professor(a): "))

    if nivel == 1:
        salario = 12.0 * horas
        print(f"Salário: R$ {salario}")
    elif nivel == 2:
        salario = 17.0 * horas
        print(f"Salário: R$ {salario}")
    else:
        salario = 25.0 * horas
        print(f"Salário: R$ {salario}")
