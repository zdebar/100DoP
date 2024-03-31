import requests

# Connect to API Endpoint URL
API_ENDPOINT = 'https://opentdb.com/api.php'
API_KEY = 'b4b50ec62db85a67245530b75ea4a533'


parameters = {
    'city name': "Prague",
    'country code': 'CZ',
    'appid': API_KEY
}


response = requests.get(API_ENDPOINT, params=parameters)
response.raise_for_status()
data = response.json()['results']

