# 15) - [DESAFIO] Desenvolva um procurado em python que leia valores inteiros para um vetor
# de 20 posições e mostre-o. Em seguida, troque o primeiro elemento pelo o último, o segundo com
# o penúltimo, o terceiro com o antepenúltimo e, assim, sucessivamente. Mostre o novo vetor após todas as trocas.

lista = []

for cont in range(20):
    lista.append(int(input(f"informe o {cont + 1}° valor: ")))

print(lista)

lista.reverse()

print(lista)