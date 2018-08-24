'''
In this project, you will visualize the feelings and language used in a set of
Tweets. This starter code loads the appropriate libraries and the Twitter data you'll
need!
'''

import json
from textblob import TextBlob
import matplotlib.pyplot as plt



#Get the JSON data
tweetFile = open("tweets.json", "r")
tweetData = json.load(tweetFile)
tweetFile.close()

# Continue your program below!

# Textblob sample:
tb = TextBlob("You are a brilliant computer scientist.")
print(tb.polarity)
print(tb.subjectivity)

polarity = []
subjectivity = []

for tweet in range(len(tweetData)):
    tweetb = TextBlob(tweetData[tweet]["text"])
    polarity.append(tweetb.polarity)
    subjectivity.append(tweetb.subjectivity)

print("This is the polarity of all the tweets")
print(polarity)
print("")
print("This is the subjectivity of all the tweets")
print(subjectivity)
print("")

averagePolarity = sum(polarity) / len(polarity)
averageSubjectvity = sum(subjectivity) / len(subjectivity)
print("This is the average polarity: " + str(averagePolarity))
print("This is the average subjectivity: " + str(averageSubjectvity))
# -----

import matplotlib.pyplot as plt

plt.hist(polarity)
plt.xlabel('Polarity')
plt.ylabel('Frequency')
plt.title('Polarity of All Tweets')
plt.show()

plt.hist(subjectivity)
plt.xlabel('Subjectivity')
plt.ylabel('Frequency')
plt.title('Subjectivity of All Tweets')
plt.show()

x = polarity
y = subjectivity
plt.scatter(x,y)
plt.title('The Subjectivity of All Tweets Plotted\nAgainst the Polarity of All Tweets')
plt.show()

from wordcloud import WordCloud
