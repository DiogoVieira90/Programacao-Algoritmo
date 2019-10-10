# Escreva um algoritmo que leia o nome de 2 times e o número de gols marcados na partida (para cada time). Escrever o
# nome do vencedor. Caso não haja vencedor deverá ser impressa a palavra EMPATE.

time1 = input("Primeiro time: ")
time1Gol = int(input("Gols do primeiro time: "))
time2 = input("Segundo time: ")
time2Gol = int(input("Gols do segundo time: "))

if time1Gol > time2Gol:
    print(f"{time1} Venceu")
elif time1Gol < time2Gol:
    print(f"{time2} Venceu")
else:
    print("EMPATE")
