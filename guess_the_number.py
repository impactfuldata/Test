"""
This script allows users to play the game guess_the_number
    -> Users compete against the computer to guess the number chosen by the computer
    -> Users get 10 guess to correctly identify the number
    -> If users guess incorrectly, they are provided with feedback: too high or too low
    -> A log of user choices and computer choice is created 
"""
# import modules
from supporting import GuessTheNumber

# define function
def guess_the_number() -> None:
    """
    Allows users to play the the game guess_the_number by using the GuessTheNumber class and its methods 

    Args
        NA

    Returns
        None
    """

    # initilaise the GuessTheNumber class 
    guess_the_number = GuessTheNumber()

    # computer randomly chooses a number from 0 to 100
    guess_the_number.computer_choice()

    # users makes a choice (upto 10 times) and this is compared to the computer choice 
    guess_the_number.user_guess_computer_choice_compare()


# check script is being run directly
if __name__ == "__main__": 

    guess_the_number()

