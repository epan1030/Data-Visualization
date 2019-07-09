'''
In this project, you will visualize the feelings and language used in a set of
Tweets. This starter code loads the appropriate libraries and the Twitter data you'll
need!
'''

import json
from textblob import TextBlob
import statistics
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from wordcloud import WordCloud


#Get the JSON data
tweetFile = open("tweets_small.json", "r")
tweetData = json.load(tweetFile)
tweetFile.close()

# Continue your program below!

# Textblob sample:
ls = [[], []]
for each in tweetData:
    tweet = each["text"]
    tb = TextBlob(tweet)
    ls[0].append(tb.polarity)
    ls[1].append(tb.subjectivity)

# Polarity Histogram
plt.title('Histogram of Twitter Data: Polarity')
plt.grid(True)
plt.xlabel("Polairty")
plt.ylabel("# of Tweets")
plt.hist(ls[0], bins=[-1, -.75, -0.5, -0.25, 0, 0.25, 0.5, 0.75, 1], facecolor = 'blue', alpha=0.5)
plt.axis([-1,2,0,100]) # x-axis range, y-axis range
plt.show()


#Subjectivity Histogram
plt.title('Histogram of Twitter Data: Subjectivity')
plt.grid(True)
plt.xlabel("Subjectivity")
plt.ylabel("# of Tweets")
plt.hist(ls[1], bins=[-1, -0.75, -0.5, -0.25, 0, 0.25, 0.5, 0.75, 1], facecolor = 'blue', alpha=0.5)
plt.axis([-0.5,2,0,100]) # x-axis range, y-axis range
plt.show()

# Word Cloud by Frequency
def word_cloud_freq(tweetData):
    combined = ""
    word_count = {}
    for each in tweetData:
        tb = each["text"]
        combined += tb
    combined = combined.lower()
    ctb = TextBlob(combined)
    word_list = ctb.words
    for each in word_list:
        if len(each) > 3 and each.isalpha() == True and each != "https":
            if each not in word_count:
                word_count[each] = 1
            else:
                word_count[each] += 1

    wc = WordCloud(background_color="white", width=900,height=500,
    relative_scaling=1).generate_from_frequencies(word_count)
    plt.imshow(wc, interpolation='bilinear')
    plt.show()
word_cloud_freq(tweetData)
# tb = TextBlob("You are a brilliant computer scientist.")
# print(tb.polarity)

print(statistics.mean(ls[1]))
print(statistics.mean(ls[0]))
