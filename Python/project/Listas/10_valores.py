# Cria uma lista vazia
valores = []

for cont in range(1,5,1):
    # Ler valores e armazena na lista
    valores.append(int(input(f"Informe o {cont}º valor: ")))

# Imprimi os valores da lista
for v in valores:
    print(v)