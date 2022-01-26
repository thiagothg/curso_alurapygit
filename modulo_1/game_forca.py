import random

def jogar():
    print_welcome()

    secret_word = read_file_words()
    words_guessed = init_words_guessed(secret_word)

    enforcou = False
    player_guess = False
    erros = 0

    print(words_guessed)
    while not enforcou and not player_guess:
        print('*********** jogando... *****************')

        guess = ask_letter()

        if guess in secret_word:
            mark_words_finded(secret_word, guess, words_guessed)

            print(words_guessed)
        else:
            erros += 1
            draw_forca(erros)

        if erros == len(secret_word):
            break
        if "_" not in words_guessed:
            break

        letras_faltando = str(words_guessed.count('_'))
        print('Ainda faltam acertar {} letras'.format(letras_faltando))
        print('Possui {} tentativas'.format(len(words_guessed) - erros))
        print(words_guessed)

    if "_" not in words_guessed:
        print_winner_player()
    else:
        print_lose_player(secret_word)

    print('fim de jogo')

def print_winner_player():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

def print_lose_player(word):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(word))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")

def ask_letter():
    return input('What a letter? ').strip().upper()

def mark_words_finded(word, guess, words_guessed):
    index = 0
    for letter in word:
        if guess == letter:
            words_guessed[index] = letter

            print('Find letter {} in posotion {}'.format(letter, index))
        index = index + 1

def print_welcome():
    print('*******************************')
    print('*******************************')
    print('************* Welcome Guess Forca ******************')
    print('*******************************')

def read_file_words():
    palavras = []
    with open('palavras.txt', 'r') as arquivo:
        for linha in arquivo:
            palavras.append(linha.strip().upper())

    return palavras[random.randrange(0, len(palavras))]

def init_words_guessed(word):
    return ['_' for letter in word]

def draw_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

if(__name__ == '__main__'):
    jogar()