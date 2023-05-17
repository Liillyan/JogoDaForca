import random
from Palavras import words

palavraCerta = random.choice(words)
print(palavraCerta)
tentativas = 0
chances = 4
letraEscolhida = []
forcaAtual = ["_"]*len(palavraCerta)

print(13*"=")
print("JOGO DA FORCA")
print(13*"=")

while tentativas < chances:
    letra = input("\nDigite uma letra: ")
    letraEscolhida.append(letra)

    if letra in palavraCerta:
        print("foooi")
        for i in

        '''for i in palavraCerta:
            forcaAtual.append[i](palavraCerta)'''
    else:
        print("Errooouuuu")
        tentativas += 1
        print(f"Você agora tem {chances-tentativas} tentativas")
        print(forcaAtual)
        for i in letraEscolhida:
            print(i, end=", ")


