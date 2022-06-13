"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie
author: Miroslav Kopecky
email: kopecky.mir@gmail.com
discord: Miro#8969

"""

from os import dup
import random
from re import U 

lines = 50 * '-'
number = random.randint(1111, 9999)

print('Hi there!')
print(lines)
print('I\'ve generated a random 4 digit number for you.')
print('Let\'s play a bulls and cows game.')
print(lines)

user_number = input('Enter the number: ')

print(lines)

# check if does not start with zero
if user_number.startswith('0'):
    print('Number can\'t start with 0.')

# check if user number has 4 digit
elif int(user_number) not in range(1111, 9999):
    print('Number must have 4 digits.')


duplicates = []

for digits in user_number:

    if user_number.count(digits) > 1:
        
        duplicates.append(digits)

print(duplicates)

if user_number.split() in duplicates:
    print('xxx')


