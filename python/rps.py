import random

def say_hello():
    # ask the user for their name and says hello
    while True:
        name = input("Hello there!\nI am RPS-bot. What is your name?\n")
        if name.isalpha() == True:
            print("Hi " + name + "! Let's play rock paper scissors.")
            print("Here are the game rules:\nlose = lose 1 point,\nwin = gain 2 points,\ntie = both gain 1 point.")
            break
        else:
            print("Please use alphabetical letters only in your name, no spaces.")
            continue

def play_game(com_pts, player_pts):
    # runs the rock paper scissors play_game
    while True:
        options = ["rock", "paper", "scissors"]
        com_choice = random.choice(options) # computer picks random word from list
        player_choice = input("What do you pick: rock, paper, or scissors?\n")
        player_choice = player_choice.lower()
        if player_choice == com_choice:
            print("It's a tie.")
            com_pts += 1
            player_pts += 1
        elif player_choice == "rock":
            if com_choice == "paper":
                print("You lost!")
                com_pts += 2
                player_pts -= 1
            elif com_choice == "scissors":
                print("You won!")
                com_pts -= 1
                player_pts += 2
        elif player_choice == "scissors":
            if com_choice == "rock":
                print("You lost!")
                com_pts += 2
                player_pts -= 1
            elif com_choice == "paper":
                print("You won!")
                com_pts -= 1
                player_pts += 2
        elif player_choice == "paper":
            if com_choice == "rock":
                print("You won!")
                com_pts -= 1
                player_pts += 2
            elif com_choice == "scissors":
                print("You lost!")
                com_pts += 2
                player_pts -= 1
        else:
            print("You did not enter a valid answer. Try again.")
            continue
        print("RPS-bot picked " + com_choice + " and you picked " + player_choice)
        print("RPS-bot now has " + str(com_pts) + " points and you have " + str(player_pts) + " points.")
        try_again(com_pts, player_pts)

def try_again(com_pts, player_pts):
    while True:
        play_again = input("Would you like to play again, yes or no?\n")
        play_again = play_again.lower()
        if play_again == "yes":
            play_game(com_pts, player_pts)
        elif play_again == "no":
            if com_pts > player_pts:
                print("Looks like RPS-bot beat you to it.")
            elif com_pts < player_pts:
                print("Congratulations, you won.")
            elif com_pts == player_pts:
                print("Wow! It's a tie.")
        else:
            print("Hmm, RPS-bot did not understand that. Please try again.")
            continue
        print("RPS-bot had " + str(com_pts) + " points and you had " + str(player_pts) + " points.")
        print("Thank you for playing!")
        exit(0)

def main():
    say_hello()
    play_game(0,0)

main()
