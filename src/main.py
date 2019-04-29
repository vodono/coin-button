import requests

token = "DwfRsoxSUaDxV-jFatXz9EWMZ_3i_UsH-FF4yWeW"

orders = requests.get('https://api-sandbox.coingate.com/v2/orders',
                      headers={'Authorization': f'Token {token}'})

print(orders)

# import ipdb
# ipdb.set_trace()
