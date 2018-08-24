'''
what is your name?
what is your age?
what is your favourite season?

'''
import json

survey = ['What is your name?','What is your age?', 'What is your birth month?','What is your favourite season?']

keys = ["name", "age", "birth month", "season"]

done = "no"


while done == "no":
    answers = {}

    for question in range(len(survey)):
        response = input(survey[question] + ":  ")
        response = response.lower()
        answers[keys[question]] = response

    new_user = input("Welcome! Are you a new user?(yes/no):  ")
    new_user = new_user.lower()
    new_file = open("banana.txt", "a")
    if new_user == "yes":
        print(answers)
        json.dump(answers, new_file)
    elif new_user == "no":
        print(answers)
        print("Try again later.")
        done = "yes"
        print("exiting")
        json.dump(answers, new_file)
    else:
        print("Invalid response.")
        json.dump(answers, new_file)
    # dictionaryName[key] = value

#print the context of the Dictionary
