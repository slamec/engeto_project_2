"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie
author: Miroslav Kopecky
email: kopecky.mir@gmail.com
discord: Miro#8969
"""

import random
from tkinter.tix import Tree

lines = 50 * '-'

print('Hi there!')
print(lines)
print('I\'ve generated a random 4 digit number for you.')
print('Let\'s play a bulls and cows game.')
print(lines)

def check_number(number):
    """
    Check if the input has all of the atributes needed, no duplicates, no 0 in 
    the be beginning etc.
    """

    # check if does not start with zero
    if number.startswith('0'):
        return 'Number can\'t start with 0.'

    # check if input has a letter
    if number.isalpha():
        return 'Number can\'t be a letter.'

    # check empty string
    if number == '':
        return 'You did not insert anything.'
    
    # avoid exception error
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

# Returns list of digits of a number
def get_digits(num):
    return [int(i) for i in str(num)]
      
  
# Returns True if number has no duplicate digits otherwise False      
def no_duplicates(num):
    num_li = get_digits(num)
    if len(num_li) == len(set(num_li)):
        return True
    else:
        return False
  
  
# Generates a 4 digit number 
# with no repeated digits    
def generate_number():
    while True:
        num = random.randint(1000,9999)
        if no_duplicates(num):
            return num
        


def run_game():
    """
    Game function including random number generation and game loop. 
    Does not accept any parameters.
    """

    game_on = True
    guesses = 0 


    number_str = generate_number()

    # generate random 4 digit number and avoid zero at the beginning
    # while number[0] == 0:
    #     number = random.sample(range(10), 4)

    #     number_str = ''.join(map(str, number))
    
    print(number_str) # testing - reveal the generated number 

    # game loop 
    while game_on:

        user_number = input('Enter the guessed number: ')
        user_number_str = str(user_number)

        # count guesses
        guesses += 1

        print(lines)

        # bull index 0 cow index 1
        bulls_cows = [0, 0]

        # call the function and check if inserted number fulfills all conditions
        if check_number(user_number_str) == None:

            # compare the generated number and inserted number
            for n, i in zip(number_str, user_number_str):

                if i in number_str:

                    # if place and number same 
                    if i == n:
                        bulls_cows[0] += 1

                    else:
                        bulls_cows[1] += 1

            # only one number or place guessed
            if bulls_cows[0] <= 1 and bulls_cows[1] <= 1:
                print(f'You have {bulls_cows[0]} bull and {bulls_cows[1]} cow.')

            # more places and numbers gussed 
            elif bulls_cows[0] < 4 and bulls_cows[1] < 4:
                print(f'You have {bulls_cows[0]} bulls and {bulls_cows[1]} cows.')
            
            # correct guess
            elif bulls_cows[0] == 4 and bulls_cows[1] == 0:

                if guesses <= 1:
                    print(f'Good job, you have guessed the right number in {guesses} guess!')
                    print(lines)
                
                else:
                    print(f'Good job, you have guessed the right number in {guesses} guesses!')
                    print(lines)                   

                game_on = False

        else:
            # avoid print None
            if check_number(user_number) == None:
                pass
        
            else:
                print(check_number(user_number))
                game_on = False

# run the game
run_game()

# ask user to repeat the game
play_again = input('Do you wanna play again? (Yes/No) ').lower()
print(lines)

while play_again == 'yes':
    run_game()
    
    play_again = input('Do you wanna play again? (Yes/No) ').lower()
    print(lines)

else:
    print('Thank you and see you next time!')

