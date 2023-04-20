import requests
from twilio.rest import Client
weather_key = "2ce180b93bd1480942b1cc598a7933b9"

auth_token= "e35964d4dc2c7a4b046eaa359b75da93" # Your Twilio API Key
account_sid = "ACbde4d801388d4a97d14753fb92a5f7ac" # Your Twilio Account SID

Parameters = {
    "lat": -0.421150,
    "lon": 36.949410,
    "appid": weather_key,
}
  
response = requests.get(url = "https://api.openweathermap.org/data/2.5/weather", params=Parameters)
response.raise_for_status()
data = response.json()
weather = data["weather"][0]["main"]
if weather == "Clouds":
    client = Client(account_sid, auth_token)
    message = client.messages \
                .create(
                     body="bring an umbrella.",
                     from_='+1 620 445 0284',
                     to='+254 720241562'
                 )

print(message.status)