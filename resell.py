def get_resell_price(twitter_data, regression_data):
    favorites = twitter_data['favorites']
    retweets = twitter_data['retweets']
    polarity = twitter_data['polarity']

    intercept = regression_data['intercept']
    favorites_coef = regression_data['favorite_coef']
    retweets_coef = regression_data['retweet_coef']
    polarity_coef = regression_data['polarity_coef']

    resell_price = intercept + (favorites_coef * favorites) + (retweets_coef * retweets) + (polarity_coef * polarity)

    return resell_price
