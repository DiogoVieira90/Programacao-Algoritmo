# criar uma lsita com valores

valores = [10,20,30,40]
print(valores[3])
print(valores[0])

valores[2] = 300
print(valores)

valores[2] = valores[1] + valores[3]
print(valores)

lista_tipos_dados_diferentes = ['Alo', 2.0, 5, [10,20]]
print(lista_tipos_dados_diferentes)

print(lista_tipos_dados_diferentes[0])
print(lista_tipos_dados_diferentes[1])
print(lista_tipos_dados_diferentes[2])
print(lista_tipos_dados_diferentes[3])
print(lista_tipos_dados_diferentes[3][0])
print(lista_tipos_dados_diferentes[3][1])

lista_vazia = []
lista_vazia.append(10)
lista_vazia.append(1000)
lista_vazia.append("Teste")
print(lista_vazia)

numeros = []
numeros.append(10)
numeros.append(20)
numeros.append(30)
print(numeros[0])

numeros[1] = 5
print(numeros)

print(numeros[3-2])

print(numeros[-1])

cavaleiros = ['guerra','fogo','agua','terra']

i = 0

while i < len(cavaleiros):
    #print(cavaleiros[i])
    i = i + 1

if 'guerra' not in cavaleiros:
    print("O cavaleiro não está na lista")

for x in cavaleiros:
    print(x)

for numero in range(20):
    if numero % 2 == 0:
        print(numero)

for fruta in ['banana','abacaxi','laranja']:
    print("eu gosto de comer " + fruta)

a = ['um','dois','três']
print(a)

del a[0]
print(a)
del a[0]
print(a)

a = ['um','dois','três']
a.pop()
print(a)
a.pop(1)
print(a)

a = ['um','dois','três']

a.remove('dois')
print(a)