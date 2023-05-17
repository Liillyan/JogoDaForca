import random
from Palavras_Forca import words

palavraCerta = random.choice(words).upper()
print(palavraCerta)
tentativas = 0
chances = 4
letraEscolhida = []
forcaAtual = ["_"]*len(palavraCerta)

print(13*"=")
print("JOGO DA FORCA")
print(13*"=")

while tentativas < chances:
    letra = input("\nDigite uma letra: ").upper()

    while letra in letraEscolhida:
        print("Voce já tentou essa letra, digite outra")
        letra = input("\nDigite uma letra: ").upper()
    letraEscolhida.append(letra)

    if letra in palavraCerta:
         print("voce acertou uma letra!!")
         for i in range(len(palavraCerta)):
            if letra == palavraCerta[i]:
                forcaAtual[i] = letra

    else:
        print("Errooouuuu")
        tentativas += 1
    print(f"Você agora tem {chances - tentativas} tentativas")
    print(forcaAtual)

    for i in letraEscolhida:
        print(i, end=", ")

#trecho que não estou conseguindo implementar para que quando o usuario já souber a palavra consiga finalizar

'''    while letra in palavraCerta:
        finalizar = input("\nDeseja chutar? digite s para sim e n para não: ").upper()
        if finalizar == "sim":
            chute = input("Qual é a palavra? ")
            if chute == palavraCerta:
                print("Parabens, voce ganhou !!")
        else:
            letra = input("\nDigite uma letra: ").upper()'''






