'''
what is your name?
what is your age?
what is your favourite season?

'''

survey = ['What is your name?','What is your age?','What is your date of birth? YY/MM/DD','What is your favourite season?']

keys = ["name", "age", "DOB", "season"]

done = "no"
while done == "no":
    answer = {}
    for question in range(len(survey)):
        response = input(survey[question] + ":  ")
        response = response.lower()
        answer[keys[question]] = response
    new_user = input("Hello! Are you a new user?(yes/no):  ")
    new_user = new_user.lower()
    if new_user == "yes":
        print(answer)
    elif new_user == "no":
        print("Try again later.")
        done = "yes"
    else:
        print("Try again.")
        print(answer)
    # dictionaryName[key] = value


#print the context of the Dictionary
