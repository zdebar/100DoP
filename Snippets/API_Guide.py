import requests

response = requests.get(url="https://api.kanye.rest")
response.raise_for_status() # Check for error
data = response.json()

print(data["quote"])

# INSTALL
    # python -m pip install requests 

# RESPONSE DATA
	# 404 doesnt exists
	# 1XX hold on
	# 2XX here yout
	# 3XX go away
	# 4XX you screwed up
    # 5XX I screwed up

# POST DATA
# response = requests.post(url=pixela_endpoint, json=user_parameters)

# DELETE DATA
# header - authentification method, method with password
# response = requests.delete(url=graph_endpoint, headers=headers)