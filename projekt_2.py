"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie
author: Miroslav Kopecky
email: kopecky.mir@gmail.com
discord: Miro#8969

"""

from itertools import count
from os import dup
import random
import re 

lines = 50 * '-'

game_on = True

# needs to generate number withou 0 in the beginning
number = random.sample(range(10), 4)
number_str = ''.join(map(str, number))

quesses = 0 

print(number_str) # control needs to be deleted

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

    # check if user number has 4 digit

    if int(number) not in range(1111, 9999):
        return 'Number must have 4 digits.'

    # check for duplicates
    duplicates = []

    for digits in number:

        if number.count(digits) > 1:
        
            duplicates.append(digits)


    if not duplicates:
        pass 

    else:
        return 'Number can\'t contain duplicates.'

while game_on:

    user_number = input('Enter the number: ')
    user_number_str = str(user_number)

    quesses += 1

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
    
    print(bulls_cows)

    if bulls_cows[0] == 1 or bulls_cows[1] == 1:
        print('bull')
        
    elif bulls_cows[0] > 1 and not 3 or bulls_cows[1] > 1 and not 3:
        print('bulls')
        
    elif bulls_cows[0] == 4 and bulls_cows[1] == 0:
        print('good job')
        game_on = False
 

    else:
        # avoid print None
        if check_number(user_number) == None:
            pass
    
        else:
            print(check_number(user_number))
            game_on = False
