import requests
from datetime import datetime

MY_LAT = 50.241200
MY_LNG = 14.311790

# Connect to API Endpoint URL

response = requests.get(url="http://api.open-notify.org/iss-now.json")

# Request module for various Error responses

response.raise_for_status()

def is_iss_overhead():

    # Reading position of ISS

    data = response.json()
    longitude = data['iss_position']['longitude']
    lattitude = data['iss_position']['latitude']

    # Compare positions
    if MY_LAT-5 <= lattitude <= MY_LAT-5 and MY_LNG <= longitude <= MY_LAT:
        return True
    
def is_night():

    # Getting Data from Sunrise and Sunset web

    parameters = {
        "lat": MY_LAT,
        "lng": MY_LNG,
        "formatted" : 0
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour

    if time_now >= sunset or time <= sunrise:
        return True
    
if is_iss_overhead() and is_night():
    pass 
    # sent email