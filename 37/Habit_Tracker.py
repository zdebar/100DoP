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
today = datetime(2024,3,9)



# USER CREATION

# pixela_endpoint = "https://pixe.la/v1/users"
# response = requests.post(url=pixela_endpoint, json=user_parameters)
# print(response.text)



# GRAPH CREATION

# graph_parameters = {
#     "id": "graph02",
#     "name": "Sleep",
#     "unit": "Hours",
#     "type": "float",
#     "color": "sora"
# }

# graph_endpoint = "https://pixe.la/v1/users/zdebar/graphs"
# response = requests.post(url=graph_endpoint, json=graph_parameters, headers=headers)
# print(response.text)



# DELETE GRAPH

graph_endpoint = "https://pixe.la/v1/users/zdebar/graphs/graph01"
response = requests.delete(url=graph_endpoint, headers=headers)
print(response)
print(response.text)



# VIEW GRAPH IN BROWSER

# https://pixe.la/v1/users/zdebar/graphs/<graphid>.html



# POST TO GRAPH

# graph_update = {
#     "date": today.strftime("%Y%m%d"),
#     "quantity": "5.5"
# }

# graph_endpoint = "https://pixe.la/v1/users/zdebar/graphs/graph02"
# response = requests.post(url=graph_endpoint, json=graph_update, headers=headers)
# print(response.text)

