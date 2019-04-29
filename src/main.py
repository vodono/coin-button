import requests

token = "DwfRsoxSUaDxV-jFatXz9EWMZ_3i_UsH-FF4yWeW"

def app(environ, start_response):
    data = b"Hello, World!\n"
    start_response("200 OK", [
        ("Content-Type", "text/plain"),
        ("Content-Length", str(len(data)))
    ])
    return iter([data])

def main():
    orders = requests.get('https://api-sandbox.coingate.com/v2/orders',
                      headers={'Authorization': f'Token {token}'})
    print(orders)

# import ipdb
# ipdb.set_trace()

if __name__ == "__main__":
    main()