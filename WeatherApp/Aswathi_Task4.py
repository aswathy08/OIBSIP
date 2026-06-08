import requests

API_KEY = "80b9f37456712a9dabf93d9fefa294f0" 
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

city = input("Enter city name: ")
url = f"{BASE_URL}?q={city}&appid={API_KEY}&units=metric"

response = requests.get(url)
data = response.json()

print(data)  # debug: see full response

if data.get("cod") != "404":
    if "main" in data:
        main = data["main"]
        weather = data["weather"][0]
        print(f"City: {city}")
        print(f"Temperature: {main['temp']}°C")
        print(f"Humidity: {main['humidity']}%")
        print(f"Condition: {weather['description'].title()}")
    else:
        print("Unexpected response:", data)
else:
    print("City not found!")

