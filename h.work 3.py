import random


def Viselitsa(Word):
    print('VREMYA IGRAT VISELITSA')


dictionary = ['random', 'bolya', 'konya', 'home', 'moloko', 'sultan']
secret = random.choice(dictionary)
guesses = 'II'
hp = 5

while hp > 0:
    missed = 0
    for letter in secret:
        if letter in guesses:
            print(letter, end=' ')

        else:
            print('_', end=' ')
            missed = missed + 1

    print()

    if missed == 0:
        print('\nYou win!')
        break

    guess = input('\nguess a letter: ')
    guesses += guess

    if guess not in secret:
        hp = hp - 1
        print('\nNope.')
        print('\n', hp, 'more HP')
        if hp < 5: print('\n  |  ')
        if hp < 4: print('  O  ')
        if hp < 3: print(' /|\ ')
        if hp < 2: print('  |  ')
        if hp < 1: print(' / \ ')
        if hp == 0:
            print('\n\nThe answer is', secret)

yesOrNo = ' yes'
while yesOrNo == ' yes':

    yesOrNo = input('Do you want play again? (yes or no)')
    if yesOrNo != "no":
        continue
    elif yesOrNo == "yes":
        break