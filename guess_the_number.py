"""
This script allows users to play the guess_the_number
    -> Users compete against the computer to guess the number chosen by the computer
    -> Users get 10 guess to correctly identify the number
    -> If users guess incorrectly, they are provided with feedback: too high or too low
"""
# import modules
from supporting import GuessTheNumber

# check script is being run directly
if __name__ == "__main__": 

    # initilaise the GuessTheNumber class 
    guess_the_number = GuessTheNumber()

    # computer randomly chooses a number from 0 to 100
    guess_the_number.computer_choice()

    print (guess_the_number.computer_number)

    # users makes a choice (upto 10 times) and this is compared to the computer choice 
    guess_the_number.user_guess_computer_choice_compare()

