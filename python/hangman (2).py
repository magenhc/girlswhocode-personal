# Some useful variables
maxfails = 7
guesses = []

while(True):
	'''
	The input() function prints out the argument, then prompts the user to type (i.e. input)
	something on the keyboard. Note that if the user enters a number, the return value
	of input() is still a string.
	'''
	word = input("Type a word for someone to guess: ")

	'''
	"\n" is a special character called "newline". You can use it to format your output. Note that
	the print() function always prints on a new line, so writing print("\n") will actually results in
	two empty lines. To print only one new line, simply write print("") or print().

	You can also write "\n" at the end of your input() prompt so that the user input
	will appear on a new line.
	'''
	print("\n")

	'''
	The "." operator is called the dot operator. Certain special functions, such as isalpha(), uses this operator
	for passing its first argument (i.e. instead of writing "isalpha(word)", you write "word.isalpha()". Functions
	that are called in this manner are known as "methods".
	'''

	#Checks if only letters are present
	if(word.isalpha() == False):
		print("That's not a word!\n")
		continue

	# Converts the word to lowercase
	word = word.lower()
	break

while(maxfails > 0):
	'''
	Note that the function join() is also a method. Its first argument is "", the empty character.

	join() accepts two arguments. The first argument is a string with which you want to join items in
	the second argument. The second argument is an "iterable object". For now, this means either a list
	or a string. join() will take each character in a string, or each element in a list, and connect them
	into a larger string. Between each character or each element, join() will insert the string provided
	in your first argument. For example,

		a = "*".join("magen")
		print(a)

	would give the following output:

		m*a*g*e*n

	Similarly,

		a = "xx".join(['a', 'b', 'c']) #note the second argument is a list
		print(a)

	will produce:

		axxbxxc

	The expression [c if c in guesses else "_" for c in word], seen below, is simply
	a complicated (but compact) way of saying: construct a list from each character (denoted c)
	in the string variable word, and replace the character with "_" if it is also found in the list
	variable guesses.

	The effect would be: for the original word provided, make the characters you have already guessed
	correctly visible, but mask all the unguessed characters with "_".

	'''
	guessed_word = "".join([c if c in guesses else "_" for c in word])

	print(" ".join(guessed_word))

	# Check for winning condition
	if (guessed_word == word):
		print("Congratulations, you won!")
		exit(0)

	'''
	Remember you cannot use + with variables or expression of different types.
	"Guesses remaining: " is a string type expression, while maxfails is an integer.
	In order to concatenate the two variables, it is thus neccesary to convert maxfails
	into a string, using the function str().

	'''
	print("Guesses remaining: " + str(maxfails))

	while(True):
		guess = input("Guess a letter: ").lower()

		# Check if single letter
		if (len(guess) != 1 or guess.isalpha() == False):
			print("Please only enter a single letter!\n")
			continue

		# Check if already guessed
		if guess in guesses:
			print("You have already guessed this letter!\n")
			continue

		# Character entered is valid
		break

	# Incorrect guess
	if guess not in word:
		print("Wrong guess!\n")
		maxfails -= 1
		continue

	# Correct guess
	print("Correct guess!\n")

	'''
	Again, notice that append() is a method.
	guesses.append(guess) means add the variable guess to the end of your
	guesses list.

	'''
	guesses.append(guess)

print("Sorry, you lost!")
