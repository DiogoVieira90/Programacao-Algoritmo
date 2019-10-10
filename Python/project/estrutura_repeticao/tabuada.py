#Desenvolva uma tabuada, usuario vair informar o valor da tabuada.

numero = int(input("Digite o valor: "))
vezes = numero

for contador in range(0, 11, 1):
    print(f"{numero} X {contador} = {numero * contador}")
