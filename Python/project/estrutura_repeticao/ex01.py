# 1- Ler 80 números e ao final informar quantos número(s) est(á)ão no intervalo entre 10 (inclusive) e 150 (inclusive).

qtdIntervalo = 0
for contador in range(80):
    numero = int(input(f"Informe o {contador + 1}º valor: "))
    if numero >= 10 and numero <= 150:
        qtdIntervalo = qtdIntervalo + 1

print(f"Achei {qtdIntervalo} números no intervalo entre 10 e 150.")