# 6) - Desenvolva um programa em python que leia valores inteiros e armazene-os em
# um vetor, calcule e exiba as seguinte informações:
#
#    a) - A quantidade de números pares.
#    b) - Os números pares.
#    c) - A quantidade de números ímpares.
#    d) - Os valores ímpares.
#    e) - A média dos valores pares.
#    f) - A média dos valores ímpares.
#    g) - A média da soma dos valores pares mais os valores ímpares.

numeros = []
numerospares = []
numerosimpares = []

pares = 0
impares = 0

for cont in range(6):
    numeros.append(float(input(f"Informe o {cont + 1}° valor: ")))

for numero in range(6):
    if numeros[numero] % 2 == 0:
        pares = pares + 1
        numerospares.append(numeros[numero])
    else:
        impares = impares + 1
        numerosimpares.append(numeros[numero])

mediapares = sum(numerospares) / len(numerospares)
mediaimpares = sum(numerosimpares) / len(numerosimpares)
mediatotal = ((sum(numerospares) + sum(numerosimpares))) / (len(numerosimpares) + len(numerospares))

print(f"\nExistem {pares} números pares.")
print("Os números pares são:")
for num in numerospares:
    print(num, end=' ')

print( f"\nA média dos números pares é {mediapares}")
print(f"\nExistem {impares} números impares.")
print("Os números impares são:")
for num in numerosimpares:
    print(num, end=' ')

print(f"\nA média dos números impares é {mediaimpares}")
print(f"\nA média total é {mediatotal}")
