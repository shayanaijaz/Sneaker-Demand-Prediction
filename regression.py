from pandas import DataFrame
from sklearn import linear_model
import matplotlib.pyplot as plt

Resell_Market = {
    'favorites': [571, 901, 466, 135, 167, 433, 106, 30, 96, 59, 41, 696, 323, 276, 147, 671, 93, 216, 54],
    'retweets': [65, 264, 104, 23, 25, 100, 27, 6, 12, 9, 8, 120, 64, 47, 17, 244, 34, 38, 10],
    'polarity': [16, 4, 24, 2, 1, 32, 9, 14, 11, 22, 16, 8, 26, 32, 4.25, 7, 2, 4, 1],
    'resell': [1470, 3450, 550, 350, 190, 930, 380, 380, 500, 550, 450, 990, 1340, 2300, 360, 1080, 250,
               1100, 200]}


def calculate_regression_equation():
    df = DataFrame(Resell_Market, columns=['favorites', 'retweets', 'polarity', 'resell'])

    X = df[['favorites', 'retweets', 'polarity']]
    Y = df['resell']

    regr = linear_model.LinearRegression()
    regr.fit(X, Y)

    return {'intercept': regr.intercept_, 'favorite_coef': regr.coef_[0], 'retweet_coef': regr.coef_[1],
            'polarity_coef': regr.coef_[2]}
