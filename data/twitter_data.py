import json

# open the json file
tweetFile = open("tweets.json", "r")

# get the data
tweetData = json.load(tweetFile)

# close the file
tweetFile.close()

# print location of first tweet's author
print(tweetData[0]["user"]["location"])

# print text for the first tweet
print(tweetData[0]["text"])

for tweetNum in range(len(tweetData)):
    print(tweetData[tweetNum]["text"])

for tweet in tweetData:
    print(tweet["text"])
