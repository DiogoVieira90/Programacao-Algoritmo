
continuar = True;

while continuar == True:
    #comando para ser executado várias vezes.
    resposta = input("Deseja continuar (S)im ou (N)ão : ").upper()
    if resposta == 'S':
        continuar = True
    elif resposta == 'N':
        continuar = False
    else:
        print("Respota inválida.")