import requests
from twilio.rest import Client
# import credentials
import os
from dotenv import load_dotenv

def load_api_keys():
    load_dotenv()

load_api_keys()

Parameters = {
    "lat": -0.421150,
    "lon": 36.949410,
    "appid": os.getenv("weather_key"),
}
  
response = requests.get(url = "https://api.openweathermap.org/data/2.5/weather", params=Parameters)
response.raise_for_status()
data = response.json()
weather = data["weather"][0]["main"]
if weather == "Clouds":
    client = Client(os.getenv("account_sid"), os.getenv("auth_token"))
    message = client.messages \
                .create(
                     body="bring an umbrella.",
                     from_='+1 620 445 0284',
                     to='+254 720241562'
                 ) 
    

print(message.status)