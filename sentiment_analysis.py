train = [
    ("This is a cop", "pos"),
    ("Not worth it", "neg"),
    ("These are fire", "pos"),
    ("I need these", "pos"),
    ("I like these", "pos"),
    ("Must cop", "pos"),
    ("pass", "neg"),
    ("copped", "pos"),
    ("these look trash", "neg"),
    ("these are bricks", "neg"),
    ("these look good", "pos"),
    ("those are hard", "pos"),
    ("these ain't it", "neg"),
    ("stop it already", "pos"),
    ("garbage", "neg")
]

from textblob.classifiers import NaiveBayesClassifier
from textblob import TextBlob

cl = NaiveBayesClassifier(train)

def classify_comments(comments):
    sentiments = []
    for comment in comments:
        blob = TextBlob(comment, classifier=cl)
        sentiments.append(blob.classify())

    polarity = get_sentiment_polarity(sentiments)

    return polarity
    # print(sentiments)


def get_sentiment_polarity(sentiments):
    positive_comments = sentiments.count('pos')
    negative_comments = sentiments.count('neg')

    if positive_comments == 0:
        positive_comments = 1
    if negative_comments == 0:
        negative_comments = 1

    return positive_comments / negative_comments

