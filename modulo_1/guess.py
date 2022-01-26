import random

def jogar():
    print('************* Guess programa ******************')

    secret_number = random.randrange(1, 101)
    total_tentativas = 0
    points = 1000
    print('Welcome ao guess game!')

    print('Whats your level?')
    print('(1) easy (2) medium (3) hard')

    nivel = int(input('enter your level: '))

    if(nivel == 1):
        total_tentativas = 20
    elif(nivel == 2):
        total_tentativas = 10
    else:
        total_tentativas = 5

    for rodada in range(1, total_tentativas + 1):
        print('try {} of {}!'.format(rodada, total_tentativas))
        number = int(input('Insert a number 1 of 100: '))

        if (number < 1 or number > 100):
            print('enter number 1 of 100')
            continue

        if number == secret_number:
            print('Guessed! Made {} points'.format(points))
            break
        else:
            if(number < secret_number):
                print('Secret number is maior')
            elif(number > secret_number):
                print('Secret number is menor')
            points_loose = abs(secret_number - number)
            points = points - points_loose

    print('fim de jogo')

if(__name__ == '__main__'):
    jogar()



