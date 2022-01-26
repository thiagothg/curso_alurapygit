import game_forca
import guess

print('************* Games ******************')
print('*******************************')

print('(1) Forca (2) Guess ')
print('')

game = int(input('Choose your game: '))

if (game == 1):
    print('Forca game')
    game_forca.jogar()
else:
    print('guess game')
    guess.jogar()

