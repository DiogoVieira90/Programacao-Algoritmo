# 16) - Dados três valores A, B e C, em que A e B são números reais e C é um caractere, pede-se
# para imprimir o resultado da operação de A por B se C for um símbolo de operador aritmético; caso
# contrário deve ser impressa uma mensagem de operador não definido. Tratar erro de divisão
# por zero. Repita esse processo cinco vezes.

for vezes in range(5):
    a = float(input("Informe um valor para A: "))
    b = float(input("Informe um valor para B: "))
    c = input("Informe o operador aritmético: ")

    if c == '+':
        print(f"{a} + {b} = {a + b}")
    elif c == '-':
        print(f"{a} - {b} = {a - b}")
    elif c == '*':
        print(f"{a} * {b} = {a * b}")
    elif c == '/':
        if b == 0:
            print(f"NÃO É POSSÍVEL DIVIDIR {a} POR ZERO!")
        else:
            print(f"{a} / {b} = {a / b}")
    else:
        print("Operador não definido.")