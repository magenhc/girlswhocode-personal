#imports the ability to get a random number (we will learn more about this later!)
from random import *

for i in range (3):
#Generates a random integer.
    i = randint(1, 100)
# For Testing: print(aRandomNumber)

    guess = input("Guess a number between 1 and 100 (inclusive): ")
    if not guess.isnumeric():
        # checks if a string is only digits 0 to 9
            print("That's not a positive whole number, try again!")
else:
            guess = int(guess) # converts a string to an integer


            if guess < i:
                print("Too low, guess again.")

            if guess > i:
                print("Too high, guess again.")

            if guess == i:
                print("You guessed correctly.")
