import requests


token = "DwfRsoxSUaDxV-jFatXz9EWMZ_3i_UsH-FF4yWeW"

request = requests.get(
    'https://api-sandbox.coingate.com/v2/orders',
    headers={'Authorization': f'Token {token}'}
).json()

orders = request['orders']

import ipdb
ipdb.set_trace()