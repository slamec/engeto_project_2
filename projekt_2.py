"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie
author: Miroslav Kopecky
email: kopecky.mir@gmail.com
discord: Miro#8969

"""

from os import dup
import random
 

lines = 50 * '-'

game_on = True

number = random.sample(range(10), 4)
number_str = ''.join(map(str, number))

print(number_str) # control needs to be deleted

print('Hi there!')
print(lines)
print('I\'ve generated a random 4 digit number for you.')
print('Let\'s play a bulls and cows game.')
print(lines)

user_number = input('Enter the number: ')
user_number_str = str(user_number)

print(lines)

def check_number(number):
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


    

