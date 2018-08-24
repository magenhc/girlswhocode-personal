import random

def say_hello():
    # ask the user for their name and says hello
    while True:
        name = input("Hello there!\nI am RPS-bot. What is your name?\n")
        if name.isalpha() == True:
            print("Hi " + name + "! Let's play rock paper scissors.")
            break
        else:
            print("Please use alphabetical letters only, no spaces.")
            continue

def com_answer_rock():
    while True:
        player_answer = input("Choose rock paper or scissors: ")
        player_answer = player_answer.lower()
        if player_answer == "rock":
            print("It's a tie!")
        elif player_answer == "paper":
            print("You won!")
        elif player_answer == "scissors":
            print("You lost!")
        else:
            print("Not a valid input.")
            continue
        print("RPS-bot picked " + com_choice + " and you picked " + player_choice)
        try_again()

def com_answer_paper():
    while True:
        player_answer = input("Choose rock paper or scissors: ")
        player_answer = player_answer.lower()
        if player_answer == "rock":
            print("You lost!")
        elif player_answer == "paper":
            print("It's a tie!")
        elif player_answer == "scissors":
            print("You won!")
        else:
            print("Not a valid input.")
            continue
        print("RPS-bot picked " + com_choice + " and you picked " + player_choice)
        try_again()

def com_answer_scissors():
    while True:
        player_answer = input("Choose rock paper or scissors: ")
        player_answer = player_answer.lower()
        if player_answer == "rock":
            print("You won!")
        elif player_answer == "paper":
            print("You lost!")
        elif player_answer == "scissors":
            print("It's a tie!")
        else:
            print("Not a valid input.")
            continue
        print("RPS-bot picked " + com_choice + " and you picked " + player_choice)
        try_again()

def try_again():
    while True:
        play_again = input("Would you like to play again, yes or no?\n")
        play_again = play_again.lower()
        if play_again == "yes":
            run_game()
        elif play_again == "no":
            print("Good game.")
        else:
            print("Hmm, RPS-bot did not understand that. Please try again.")
            continue
        exit(0)


def run_game():
    options = ["rock", "paper", "scissors"]
    com_player = random.choice(options)
    # if computer answer = rock we want to run comp answer rock function
    if com_player == "rock":
        com_answer_rock()
    elif com_player == "paper":
        com_answer_paper()
    else:
        com_answer_scissors()

def main():
    say_hello()
    run_game()

main()
