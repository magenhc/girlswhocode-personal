from random import *

aRandomNumber = randint(1,100)

numTries = 0 # Don't need for a for loop
while True: # for numTries in range (3)
    guess = input("Guess a number between 1 and 100 (inclusive):")
    numTries + 1
    if not guess.isnumeric():
        print("That's not a positive whole number, try again.")
        continue
    else:
        guess = int(guess)

    # check number is correct
    if guess == aRandomNumber:
        print("You guessed correctly!")
        break

    #check if out of tries
    if numTries >= 3:
        print("Sorry! You guessed too many times. The number was:" + str(aRandomNumber))

    #give hints
    if(guess > aRandomNumber):
        print("Try a smaller number next time!")
    if(guess < aRandomNumber):
        print("Try a bigger number next time!")
