import datetime
import requests

from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    token = "DwfRsoxSUaDxV-jFatXz9EWMZ_3i_UsH-FF4yWeW"

    request = requests.get(
        'https://api-sandbox.coingate.com/v2/orders',
        headers={'Authorization': f'Token {token}'}
    ).json()

    orders = request['orders']

    for order in orders:
        order['created_at'] = datetime.datetime.strptime(order['created_at'], "%Y-%m-%dT%H:%M:%S%z")

    return render_template("index.html", orders=orders)
