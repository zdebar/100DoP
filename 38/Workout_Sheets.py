import requests
from datetime import datetime


# POST TO NUTRITIONIX 


API_ID = "fcaf44a1"
API_KEY = "01905ff757e2407c7dfbd2b006fcdc84"

headers = {
    'Content-Type': 'application/json',
    'x-app-id': API_ID, 
    "x-app-key": API_KEY
}

url_nutritionix = "https://trackapi.nutritionix.com/v2/natural/exercise"
parameters = {
    "query": "Running 4km in 20 minutes",
    "weight_kg": 91,
    "height_cm": 186,
    "age": 42
}

response = requests.post(url_nutritionix, json=parameters, headers=headers)
response.raise_for_status()
result = response.json() 
print(response.text) # valid JSON


# POST TO SHEETY

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

headers_sheety = {"Authorization": "Bearer MBc29974816768fadfgh"}

API_SHEETY_URL = "https://api.sheety.co/3454450ae1d8878aa205be89ffd5177d/workoutsTracking/workouts"

for i in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": i["user_input"].title(),
            "duration": i["duration_min"],
            "calories": i["nf_calories"]
        }
    }


sheety_response = requests.post(API_SHEETY_URL, json=sheet_inputs, headers=headers_sheety)
response.raise_for_status()
print(sheety_response.text)



