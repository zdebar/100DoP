import requests
from datetime import datetime

# PARAMETERS

user_parameters = {
    "token": "zdebar299748", 
    "username": "zdebar",
    "agreeTermsOfService":"yes",
    "notMinor":"yes"
}

headers = {
    "X-USER-TOKEN": "zdebar299748"
}

# today = datetime.now()
today = datetime(2024, 3, 12)



# USER CREATION

# pixela_endpoint = "https://pixe.la/v1/users"
# response = requests.post(url=pixela_endpoint, json=user_parameters)
# print(response.text)



# GRAPH CREATION

# graph_parameters = {
#     "id": "graph06",
#     "name": "Diet",
#     "unit": "score",
#     "type": "int",
#     "color": "sora"
# }

# graph_endpoint = "https://pixe.la/v1/users/zdebar/graphs"
# response = requests.post(url=graph_endpoint, json=graph_parameters, headers=headers)
# print(response.text)



# DELETE GRAPH

# graph_endpoint = "https://pixe.la/v1/users/zdebar/graphs/graph01"
# response = requests.delete(url=graph_endpoint, headers=headers)
# print(response)
# print(response.text)



# VIEW GRAPH IN BROWSER

# https://pixe.la/v1/users/zdebar/graphs/<graphid>.html



# POST TO GRAPH 1 - Weight / float / kgs

graph_update = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "91.3"
}

graph_endpoint = "https://pixe.la/v1/users/zdebar/graphs/graph01"
response = requests.post(url=graph_endpoint, json=graph_update, headers=headers)
print(response.text)

# POST TO GRAPH 2 - Sleep / Float / hours

graph_update = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "7"
}

graph_endpoint = "https://pixe.la/v1/users/zdebar/graphs/graph02"
response = requests.post(url=graph_endpoint, json=graph_update, headers=headers)
print(response.text)

# POST TO GRAPH 3 - Cardio / Float / kms

graph_update = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "0"
}

graph_endpoint = "https://pixe.la/v1/users/zdebar/graphs/graph03"
response = requests.post(url=graph_endpoint, json=graph_update, headers=headers)
print(response.text)

# POST TO GRAPH 4 - Yoga / Float / mins

graph_update = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "60"
}

graph_endpoint = "https://pixe.la/v1/users/zdebar/graphs/graph04"
response = requests.post(url=graph_endpoint, json=graph_update, headers=headers)
print(response.text)

# POST TO GRAPH 5 - Coffee/Tea / Int / amount

graph_update = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "1"
}

graph_endpoint = "https://pixe.la/v1/users/zdebar/graphs/graph05"
response = requests.post(url=graph_endpoint, json=graph_update, headers=headers)
print(response.text)

# POST TO GRAPH 6 - Diet / Int / score / 4 - 2400 cal, 5 - 2200 cal, 6 - 2000 cal, 7 - 1800 cal, 8 - 1600 cal, 9 - 1400 cal, 10 - 1200 cal

graph_update = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "10"
}

graph_endpoint = "https://pixe.la/v1/users/zdebar/graphs/graph06"
response = requests.post(url=graph_endpoint, json=graph_update, headers=headers)
print(response.text)