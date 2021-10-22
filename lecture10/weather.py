import requests
from secrets import TOKEN

BASE_API_URL = 'http://api.weatherapi.com/v1'

parameters_forecast_weather = {
    'key': TOKEN,
    'lang': 'uk',
    'aqi': 'yes',
    'q': 'Kiev',
    'days': 3,
    'alerts': 'yes',
}

data = requests.get(
    f'{BASE_API_URL}/forecast.json',
    params=parameters_forecast_weather,
).json()

print(f"Current temperature in Kiev is: {data['current']['temp_c']} Celsius")

for i, day_data in enumerate(data['forecast']['forecastday']):
    text_forecast = day_data['day']['condition']['text']
    print(f'{"Today" if i == 0 else f"{i} days after today"} weather forecast for in Kiev is: {text_forecast}')

response = requests.get(
    'http://api.weatherapi.com/v1/current.json',
    params=parameters,
    headers=headers,
)

response_data = response.json()

