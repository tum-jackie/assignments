import json
import requests

with open("data.json", "r") as f:
    data = json.load(f)
    name = data["name"]
    email = data["email"]
    print("Name: " , name)
    print("Email: " , email)

response = requests.get("https://jsonplaceholder.typicode.com/users/1") #get command to get data from the file
response_data = response.json()
if response_data == data:
    print("Data retreived using curl and requests i the same")
else:
    print("Data retreived using curl and requests i not the same")