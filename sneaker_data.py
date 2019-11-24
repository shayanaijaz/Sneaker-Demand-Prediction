# Get the sneaker data from thesneakerdatabase api

import requests
def get_sneaker_data(query):
    brand = query.args.get('brand')
    gender = query.args.get('gender')
    year = query.args.get('year')
    title = query.args.get('title')
    colorway = query.args.get('colorway')

    parameters = {'brand': brand, 'gender': gender, 'year': year, 'title': title, 'colorway':colorway}

    sneaker_data = requests.get('http://www.thesneakerdatabase.com/api/getData', params=parameters)

    print(sneaker_data.url)

    new_data = sneaker_data.json()
    print(new_data['data'])