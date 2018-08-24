'''
what is your name?
what is your age?
what is your favourite season?

'''
import json
answer = {}

survey = ['What is your name?','What is your age?','What is your date of birth? YY/MM/DD','What is your favourite season?']

keys = ["name", "age", "DOB", "season"]

for question in range(len(survey)):
    response = input(survey[question] + ":  ")
    response = response.lower()
    answer[keys[question]] = response
    # dictionaryName[key] = value

#print the context of the Dictionary
print(answer)
new_file = open("banana.txt", "w")

print(json.dump(answer, new_file))
