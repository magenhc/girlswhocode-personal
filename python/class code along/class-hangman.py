# ask user for word to guessed
while True:

    word = input("Type a word for someone to guess: ")
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

    if word.isalpha() == False:
        print("That's not a word!")
    else:
        print("Word set!")
        break

    # convert the world to lowercase
    word = word.lower()

done = False

maxfails = 7
numfails = 0
guesses = []

wordToGuess = []
for letter in word:
    wordToGuess.append("_")
print("Current word", wordToGuess)

while not done:
        print("")
        # allow to user to guess single letters
        #check that the user guess is a single letter
        letter = input("Guess a letter: ")

        if len(letter) > 1:
            print("That's not a single letter. Try again.")
        elif letter.isalpha() == False:
            print ("That's not a letter! Try again.")
        else:
            # we have a single letter guess
            # check if it's correctly
            if letter in word:
                # if it is correct, show it onscreen in the hidden word
                # idx is index
                for idx in range (0, len(wordToGuess)):
                    if(word[idx] == letter):
                        wordToGuess[idx] = letter
                print("You got a correct letter!")
                print(wordToGuess)

                done = True
                for idx in range(0, len(wordToGuess)):
                    if wordToGuess[idx] == "_":
                        done = False
                        break
                if done:
                    print("You won!")
                    break


            else: # incorrect
                # if it's not correct, decrease number of chances
                numfails += 1
                print("Chances left: ", str(maxfails - numfails))
                # and let the user know they got it wrong
                print ("Wrong guess!")
                if numfails >= maxfails:
                    print("You lose!")
                    break
            # either way, let user know/track what letters they've guessed so far
            guesses.append(letter)
            print("Guesses so far:", guesses)

# if letter is too long and is not a-z letters
# print an error message
# else
# print nothing





# ask for user to input a letters
# check to see if the letter is in the word
# if the letter is in the word, display it and show a message that the user got it right
# if the letter is not in the word, notify the user that they have one chance left
# either way, track the letters that have been guessed




# display blank letters for secret word
# allow the user to guess single letters
# display letters that the user has guessed correctly
# track wrong guesses until a max number of wrong guesses is reached
# display all letters that have been guessed
