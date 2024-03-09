import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")

#Request module for various Error responses
response.raise_for_status()
data = response.json()
print(data)
longitude = data['iss_position']['longitude']
lattitude = data['iss_position']['latitude']

iss_position = (longitude, lattitude)
print(iss_position)