# define functions

def intro():
    while True:
        name = input("Hi, I'm Chatbot!\nWhat's your name?\n")
        if name.isalpha() == False:
            print("Please only use letters in your name.\n")
            continue
        else:
            print("Nice to meet you " + name + "!")
            feeling = input("How are you today?\n")
            print("You are feeling " + feeling + " today.")
            break

def joke():
    print("Why do functions break up?\nThey stop calling each other.")

def poem():
    print("Up until yesterday, I anticipated coding.\nAfter starting python, I realize I have been forsaken.")

def main():
    while True:
        answer = input("Do you want to hear a joke or a poem?")
        if answer.lower() == "joke": # if answer == "joke" or answer == "Joke":
            joke()
            break
        elif answer.lower() == "poem":
            poem()
            break
        else:
            print("That's not a valid answer, please try again.")
            continue

if __name__ == "__main__":
    intro()
    main()
