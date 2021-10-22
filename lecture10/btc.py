import requests
from secrets import TOKEN

SYMBOL = 'BTC'
parameters = {
    'symbol': SYMBOL,
}

headers = {
    'Accepts': 'current.json',
    'X-CMC_PRO_API_KEY': TOKEN,
}

response = requests.get(
    'http://api.weatherapi.com/v1/current.json',
    params=parameters,
    headers=headers,
)

response_data = response.json()

