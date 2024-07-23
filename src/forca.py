# CTRL+I --> Copilot
import random

def mensagem():
    print("JOGO DA FORCA!")

# Escolha randomica de uma palavra apartir de uma lista
def palavra_secreta():
    palavras = []
    with open('lista.txt', 'r') as file:
        palavras = [linha.strip() for linha in file.readlines()]
    return random.choice(palavras)

def chute():
    print("Chute uma letra: ")
    letra = input()
    letra = letra.strip().lower()
    return letra

def inicializa_letras_acertadas(palavra):
    return ["_" for letra in palavra]

def adicionar_palavra(filename,palavra_add):
	with open(filename, 'a') as file:
		file.write(palavra_add + '\n')
	print("Palavra adicionada com sucesso!")

# Desenho da forca
def forca(tentativas):
    if tentativas == 6:
        print("  _______     ")
        print(" |/      |    ")
        print(" |            ")
        print(" |            ")
        print(" |            ")
        print(" |            ")
        print(" |            ")
        print("_|___         ")
    elif tentativas == 5:
        print("  _______     ")
        print(" |/      |    ")
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")
        print(" |            ")
        print("_|___         ")
    elif tentativas == 4:
        print("  _______     ")
        print(" |/      |    ")
        print(" |      (_)   ")
        print(" |       |    ")
        print(" |            ")
        print(" |            ")
        print(" |            ")
        print("_|___         ")
    elif tentativas == 3:
        print("  _______     ")
        print(" |/      |    ")
        print(" |      (_)   ")
        print(" |      /|    ")
        print(" |            ")
        print(" |            ")
        print(" |            ")
        print("_|___         ")
    elif tentativas == 2:
        print("  _______     ")
        print(" |/      |    ")
        print(" |      (_)   ")
        print(" |      /|\   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")
        print("_|___         ")
    elif tentativas == 1:
        print("  _______     ")
        print(" |/      |    ")
        print(" |      (_)   ")
        print(" |      /|\   ")
        print(" |      /     ")
        print(" |            ")
        print(" |            ")
        print("_|___         ")
    elif tentativas == 0:
        print("  _______     ")
        print(" |/      |    ")
        print(" |      (_)   ")
        print(" |      /|\   ")
        print(" |      / \   ")
        print(" |            ")
        print(" |            ")
        print("_|___         ")

if __name__ == "__main__":
    
    c = 1
    mensagem()

    while(c == 1):
        escolha = 3
        fim_de_jogo = False
        tentativas = 6
        letras_jogadas = []

        # MENU
        print("1 - Jogar")
        print("2 - Adicionar palavra ao jogo")
        print("0 - Sair")

        escolha = int(input("Escolha: "))
        if escolha > 2 or escolha < 0:
            print("Escolha inválida!")
            escolha = int(input("Escolha: "))
        
        # 1 - JOGAR
        if(escolha == 1):
            
            print("Vamos jogar!")
            palavra = palavra_secreta()
            print(palavra)
            
            forca(tentativas)
            letras_acertadas = inicializa_letras_acertadas(palavra)
            print("Palavra: ", letras_acertadas)

            while(fim_de_jogo == False):

                while(tentativas != 7):

                    if tentativas == 0:
                        print("Você perdeu! A palavra era: ", palavra)
                        fim_de_jogo = True
                        break

                    if "_" not in letras_acertadas:
                        print("Parabéns! Você acertou a palavra!")
                        fim_de_jogo = True
                        break   
                    
                    print("Tentativas restantes: ", tentativas)
                    letra = chute()
                    
                    if letra in letras_jogadas:
                        print("Letra já jogada!")

                    if letra in palavra:
                        for i in range(len(palavra)):
                            if letra == palavra[i]:
                                letras_jogadas.append(letra)
                                letras_acertadas[i] = letra
                        print("Palavra: ", letras_acertadas)
                    else:
                        letras_acertadas.append(letra)
                        tentativas -= 1

                    forca(tentativas)
	
	# 2 - Adicionar Palavra
        elif escolha == 2:
        	print("Adicionar palavra ao jogo")
        	palavra_add = input("Digite a palavra: ")
        	adicionar_palavra('lista.txt',palavra_add)
           	
        # 0 - SAIR
        elif escolha == 0:
            print("Saindo do Jogo...")
            c = 0
