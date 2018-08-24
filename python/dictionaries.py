'''A dictionary is a python data structure that matches KEYs with VALUES.
You can look up a value using its key.
Keys must be unique, but values can be the same.
Example is the English Dictionary. Key = the word
value = the definition '''

# Declare a dictionary with known values
# before the colon is the key : after the colon is the value

spanish_english = {
    'hola' : 'hello',
    'gato' : 'cat',
    'mujer' : 'woman'
}
# references which key you are looking for -> hola
first_value = spanish_english['hola']

bikes = [] # empty list
users = {} # empty Dictionary, stores names of people and their ages
users['Lila'] = 20
# if print users: users = {'Lila' : 20}


'''1. Declare a dictionary that holds pairs of names and ages of your friends and family members
2. Print your dictionary
3. Experiment to answer the question: What kind of VALUES can dictionaries hold?'''

family_friends = {
    'Ryan' : 10,
    'Yixian' : 25,
    'Thomas' : 9,
    'Tyler' : 7,
    'Frank' : 21,
    'Sally' : 28
}

family_friends2 = {}
family_friends2['cat'] = 16

dictTest = {}
dictTest['Lila'] = ['ellie']
dictTest['Lila'].append("callie")
dictTest['Olivia'] = [16]
dictTest['Olivia'].append("wiggles")
dictTest['Olivia'].append(3)

print(dictTest)
