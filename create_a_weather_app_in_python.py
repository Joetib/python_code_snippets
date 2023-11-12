# To create a weather app in Python, we can use the OpenWeatherMap API.
# Install the requests library using:
# >> pip install requests
import requests
# API key for OpenWeatherMap
api_key = "YOUR_API_KEY"
# Function to get weather information
def get_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    response = requests.get(url)
    data = response.json()
    weather = {
        "city": data["name"],
        "temperature": data["main"]["temp"],
        "description": data["weather"][0]["description"],
        "humidity": data["main"]["humidity"],
        "wind_speed": data["wind"]["speed"]
    }
    return weather
city = input("Enter city name: ")
weather_info = get_weather(city)
# Print the weather information
print(weather_info)