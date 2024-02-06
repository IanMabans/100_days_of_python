import requests
from datetime import datetime

#
# response = requests.get(url='http://api.open-notify.org/iss-now.json')
# data = response.json()
#
# longitude = data['iss_position']['longitude']
# latitude = data['iss_position']['latitude']
# iss_position = (longitude, latitude)
# print(iss_position)
my_lat = '-1.2832533'
my_long = '36.8172449'

parameters = {
    'lat': my_lat,
    'lng': my_long,
}
response = requests.get(url='https://api.sunrise-sunset.org/json', params=parameters)
response.raise_for_status()
data = response.json()
sunrise = data['results']['sunrise']
sunset = data['results']['sunset']
print(sunrise.split('T'))
time_now = datetime.now()
print(time_now)
