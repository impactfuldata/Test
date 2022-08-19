"""
This script contains the classes required by the guess_the_number.py
"""
# import modules
import sys
from random import randint

# create class 
class GuessTheNumber:
    """
    This class allows:
        -> Users to be welcomed to the game
        -> Computer to randomly choose a number
        -> Users to make a choice and for this to be compared it to the computer choice 
    """

    def __init__(self) -> None:
        """
        Users are welcomed to the game and asked if they want to play the game 

        Args
            NA

        Returns
            None
        """    
        ## Users are welcomed to the game
        welcome_message = "In this game, you have to guess the number I have chosen."

        ## Users are asked if they want to play the game, until they enter a valid input: y or n 
        while True:
            want_to_play = str.lower(input("Would you like to play: y or n "))
            if want_to_play == "y":
                print("Okay got it. I will start the game")
                break
            elif want_to_play == "n":
                print("Okay got it. I will stop the game")
                sys.exit()
            else:
                print("You have entered an invalid input. Please, try again.")

    def computer_choice(self) -> int:
        """
        Computer randomly chooses a number from 0 to 100

        Args
            NA

        Returns
            self.computer_number: randomly chosen number from 0 to 100 (both included): int
        """
        ## Computer choose a number from 0 to 100
        self.computer_number = randint(0, 100)

         ## Users are informed that number chosen if from 0 to 100
        print("I have chosen a number from 0 to 100")
        return self.computer_number

    def user_guess_computer_choice_compare(self) -> None:
        """
        Users makes a choice (upto 10 times) and this is compared to the computer choice 

        Args
            NA

        Returns
            None
        """
        ## Users can make a choice upto 10 times
        user_guess_count = 1
        while user_guess_count <= 10:
        
        ## Users make their choice
            self.user_guess = int(input("What do you think the number is?: "))
        
        ## Users provided with feedback on their guess: correct 
            if self.user_guess == self.computer_number:
                print("You have guessed the number correctly.")
                break

         ## Users provided with feedback on their guess: too high    
            elif self.user_guess > self.computer_number:
                print("Your guess is too high.")
                user_guess_count += 1
        
        ## Users provided with feedback on their guess: too low
            elif self.user_guess < self.computer_number:
                print("Your guess is too low.")
                user_guess_count += 1