import requests
from datetime import datetime

# API version (check the official documentation for the correct version)
api_version = 'v1'

pixela_endpoint = f'https://pixe.la/{api_version}/users'
USERNAME = 'use your own username'
TOKEN = 'use your token'  # Double-check accuracy and permissions
GRAPH_ID = 'graph1'

user_params = {
    'token': TOKEN,
    'username': USERNAME,
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes',
}

# Create user
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)  # Commented out for demo

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    'id': GRAPH_ID,
    'name': 'Walking Graph',
    'unit': 'Km',
    'type': 'float',
    'color': 'ajisai',
}

headers = {
    "X-USER-TOKEN": TOKEN,
}
# Create a new graph
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

pixel_creation_endpoint = f'{graph_endpoint}/{GRAPH_ID}'
yesterday = '20240209'
today = datetime.now()
print(today.strftime('%Y%m%d'))
pixel_data = {
    'date': today,
    'quantity': input("How many km did you cycle?"),
}
response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
print(response.text)

# update_endpoint = f'{pixel_creation_endpoint}/{yesterday}'
# new_pixel_dict = {
#     'quantity': '16.0'
# }
# # response = requests.put(url=update_endpoint, headers=headers, json=new_pixel_dict)
# # print(response.text)
#
# delete_endpoint = update_endpoint
# response = requests.delete(url=delete_endpoint,headers=headers,)
# print(response.text)