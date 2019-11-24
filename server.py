from flask import Flask, request
from sneaker_data import get_sneaker_data

app = Flask(__name__)


@app.route('/', methods=['POST'])
def receive_data():
    req_data = request

    get_sneaker_data(request)

    return 'data received'