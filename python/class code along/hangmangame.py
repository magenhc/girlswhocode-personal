word = input("Type a word for someone to guess: ")

# Converts the word to lowercase
word = word.lower()

# Checks if only letters are present
if(word.isalpha() == False):
	print("That's not a word!")

# Some useful variables
guesses = []
tries = 7

guess = input("Guess a letter: ")
if guess in word:
    print("Correct!")
else:
    print("Incorrect!")

done = False

display = []

for letter in word:
    display.append("_")

while not done:
    guess = input("Guess a letter: ")
    if guess in word:
        print("Correct!")
        print (display)
    else:
        print("Incorrect!")
        tries -= 1
    if tries == 0:
        print("Sorry, you've run out of tries!")
        break
