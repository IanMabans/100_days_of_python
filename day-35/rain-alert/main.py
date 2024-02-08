import requests
import os

from twilio.rest import Client

account_sid = os.environ.get('account_sid')
auth_token = os.environ.get('auth_token')


owm_endpoints = 'https://api.openweathermap.org/data/2.5/forecast'

api_key = os.environ.get('api_key')
weather_params = {
    'lat': '-1.167240',
    'lon': '36.825500',
    'appid': api_key,
    'cnt': 4,
}
# I am using Kiambu kenya coordinates

response = requests.get(owm_endpoints, params=weather_params)
response.raise_for_status()
weather_data = response.json()
# print(weather_data["list"][0]['weather'][0])
will_rain = False
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]['id']
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        from_='[api sender number]',
        to='[your phone number]',
        body='Its going to rain Ian, carry an umbrella ☔'
    )

    print(message.status)
