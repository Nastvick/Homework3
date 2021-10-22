import requests

SYMBOL = 'IP'
parameters = {
    'symbol': SYMBOL,
}

headers = {
    'Accepts': 'IPadress/json'
}
response = requests.get(
    'https://httpbin.org/ip',
    parameters = parameters,
    headers = headers,
)


print(f'Current price of {SYMBOL} is {response}')