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

response = requests.get(owm_endpoints, params=weather_params)
response.raise_for_status()
weather_data = response.json()

will_rain = False

for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]['id']
    # Check if the condition code indicates rain
    if 200 <= int(condition_code) <= 531:
        will_rain = True
        break  # No need to continue checking if we've found rain

if will_rain:
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        from_='[api sender number]',
        to='[your phone number]',
        body='It\'s going to rain Ian, carry an umbrella ☔'
    )

    print(message.status)
else:
    print("No rain expected.")
