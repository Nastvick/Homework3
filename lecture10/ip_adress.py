import requests

response = requests.get('https://httpbin.org/ip').json()
print(f'My IP adress is {response}')
