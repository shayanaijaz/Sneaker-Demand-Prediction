from twitter_data import get_twitter_data
from regression import calculate_regression_equation
from resell import get_resell_price


def main():
    sneaker_input = input("Enter a sneaker name: ")

    twitter_data = get_twitter_data(sneaker_input)
    regression_data = calculate_regression_equation()

    resell_perice = int(get_resell_price(twitter_data, regression_data))

    print("The predicted resale price for " + sneaker_input + " is $" + str(resell_perice))
    main()


if __name__ == '__main__':
    main()
