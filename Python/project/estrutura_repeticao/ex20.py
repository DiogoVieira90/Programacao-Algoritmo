# 20) - Escrever um algoritmo que leia três valores inteiros e verifique se eles
# podem ser os lados de um triângulo. Se for, informar qual o tipo de triângulo
# que eles formam: equilátero, isóscele ou escaleno.
# Propriedade: o comprimento de cada
# lado de um triângulo é menor do que a soma dos comprimentos dos outros dois lados.
#
# Triângulo Equilátero: aquele que tem os comprimentos dos três lados iguais;
# Triângulo Isóscele: aquele que tem os comprimentos de dois lados iguais. Portanto, todo triângulo equilátero é também isóscele;
# Triângulo Escaleno: aquele que tem os comprimentos de seus três lados diferentes.
# Repita esse processo 5 vezes.

for vezes in range(5):
    ladoA = int(input("Informe um valor para o lado A do triângulo: "))
    ladoB = int(input("Informe um valor para o lado B do triângulo: "))
    ladoC = int(input("Informe um valor para o lado C do triângulo: "))

    if ladoA < ladoB + ladoC and ladoB < ladoA + ladoC and ladoC < ladoA + ladoB:

        if ladoA == ladoB and ladoA == ladoC:
            print("Triângulo equilátero.")
        elif ladoA == ladoB or ladoA == ladoC or ladoB == ladoC:
            print("Triângulo isóscele.")
        else:
            print("Triângulo escaleno.")

    else:
        print("NÃO É UM TRIÂNGULO!")