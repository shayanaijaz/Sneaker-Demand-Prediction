
import GetOldTweets3 as got
import requests
from bs4 import BeautifulSoup
from sentiment_analysis import classify_comments


def get_twitter_data(user_input):
    sneaker_name = user_input

    twitter_accounts = ["SneakerNews", "theyeezymafia", "KicksDeals", "SneakerShouts", "J23app", "SOLELINKS",
                        "kicksonfire"]

    tweets = []
    total_favorites = 0
    total_retweets = 0
    tweets_html = []

    for account in twitter_accounts:
        print("Searching for tweets from: ", account)
        tweet_result = got.manager.TweetCriteria().setUsername(account).setQuerySearch(sneaker_name).setTopTweets(
            True).setMaxTweets(1)

        if got.manager.TweetManager.getTweets(tweet_result):
            tweet = got.manager.TweetManager.getTweets(tweet_result)[0]
            print("Retrieved most popular tweet with " + str(tweet.favorites) + " favorites and " + str(tweet.retweets) + " retweets")
            total_favorites += tweet.favorites
            total_retweets += tweet.retweets
            tweets_html.append(requests.get(tweet.permalink).text)
            tweets.append(got.manager.TweetManager.getTweets(tweet_result)[0])
        else:
            print("No tweet matching search criteria")

    avg_favorites = int(total_favorites / len(tweets))
    avg_retweets = int(total_retweets / len(tweets))
    comments = get_tweet_comments(tweets_html)

    print("Average number of favorites: ", avg_favorites)
    print("Average number of retweets: ", avg_retweets)

    polarity = classify_comments(comments)
    print("Comment polarity: ", polarity)

    return{'favorites': avg_favorites, 'retweets': avg_retweets, 'polarity': polarity}


def get_tweet_comments(tweets_html):
    comments = []
    for tweet_html in tweets_html:
        soup = BeautifulSoup(tweet_html, "html.parser")

        results = soup.findAll("p", {"class": "TweetTextSize js-tweet-text tweet-text"})

        for result in results:
            if "pic.twitter.com" not in result.get_text():
                comments.append(result.get_text().lower())

    return comments
