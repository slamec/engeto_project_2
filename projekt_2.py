"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie
author: Miroslav Kopecky
email: kopecky.mir@gmail.com
discord: Miro#8969

"""

from ast import main
from asyncio import run
import random

lines = 50 * '-'

print('Hi there!')
print(lines)
print('I\'ve generated a random 4 digit number for you.')
print('Let\'s play a bulls and cows game.')
print(lines)

def check_number(number):
    """Check if the input has all of the atributes needed, no duplicates, no 0 in 
    the be beginning etc."""

    # check if does not start with zero
    if number.startswith('0'):
        return 'Number can\'t start with 0.'

    if number.isalpha():
        return 'Number can\'t be a letter.'

    if number == '':
        return 'You did not insert anything.'
    
    try:

        # check if user number has 4 digit
        if int(number) not in range(1111, 9999):
            return 'Number must have 4 digits.'
    
    except:
        return 'Wrong number format. Number has to have 4 digits.'

    # check for duplicates
    duplicates = []

    for digits in number:

        if number.count(digits) > 1:
        
            duplicates.append(digits)


    if not duplicates:
        pass 

    else:
        return 'Number can\'t contain duplicates.'

def run_game():
    game_on = True
    guesses = 0 

    number = [0]

    # avoid zero on the beginning
    while number[0] == 0:
        number = random.sample(range(10), 4)

        number_str = ''.join(map(str, number))
    
    #print(number_str) # testing needs to be deleted

    while game_on:

        user_number = input('Enter the number: ')
        user_number_str = str(user_number)

        guesses += 1

        print(lines)

        # bull index 0 cow index 1
        bulls_cows = [0, 0]

        if check_number(user_number_str) == None:

            for n, i in zip(number_str, user_number_str):

                if i in number_str:

                    if i == n:
                        bulls_cows[0] += 1
                
                    else:
                        bulls_cows[1] += 1
        
            # print(bulls_cows) # for testing purposes

            if bulls_cows[0] <= 1 and bulls_cows[1] <= 1:
                print(f'You have {bulls_cows[0]} bull and {bulls_cows[1]} cow.')

            elif bulls_cows[0] < 4 and bulls_cows[1] < 4:
                print(f'You have {bulls_cows[0]} bulls and {bulls_cows[1]} cows.')
            
            elif bulls_cows[0] == 4 and bulls_cows[1] == 0:
                print(f'Good job, you have guessed the right number in {guesses} guesses!')
                
                game_on = False

        else:
            # avoid print None
            if check_number(user_number) == None:
                pass
        
            else:
                print(check_number(user_number))
                game_on = False

run_game()

play_again = input('Do you wanna play again? Yes/No ').lower()

if play_again == 'yes':
    run_game()

else:
    print('See you next time.')