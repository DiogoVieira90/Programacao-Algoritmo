# 9) - Faça um algoritmo que receba um número (não sabemos quantos números serão
# informados pelo usuário) e mostre uma mensagem caso este número seja maior
# que 80, menor que 25 ou igual a 40.

continuar = True

while continuar == True:
    num = int(input("Digite um número: "))

    if num == 40:
        print("número 40. haha.")
    elif num < 25:
        print(f"{num} é menor que 25.")
    elif num > 80:
        print(f"{num} é maior que 80.")

    resp = input("Informar outro número? (S)im ou (N)ão? ")
    if resp.upper() == 'S':
        continuar = True
    else:
        continuar = False