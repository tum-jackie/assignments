import requests
from twilio.rest import Client
import credentials

Parameters = {
    "lat": -0.421150,
    "lon": 36.949410,
    "appid": credentials.weather_key,
}
  
response = requests.get(url = "https://api.openweathermap.org/data/2.5/weather", params=Parameters)
response.raise_for_status()
data = response.json()
weather = data["weather"][0]["main"]
if weather == "Clouds":
    client = Client(credentials.account_sid, credentials.auth_token)
    message = client.messages \
                .create(
                     body="bring an umbrella.",
                     from_='+1 620 445 0284',
                     to='+254 720241562'
                 ) 
    

print(message.status)