import requests

api_key="f239cd0a473ba9d7487adc90e507a75e"

def get_weather_info(user_city, api_key):
  url = f"https://api.openweathermap.org/data/2.5/weather?q={user_city}&appid={api_key}"
  response = requests.get(url)
  if response.status_code == 200:
    return response.json()
  else:
    print(f"Error: {response.status_code} - City not found or other API error")
    return None

def display_weather(weather_data, user_city):
  if weather_data:
    try:
      weather = weather_data["weather"][0]["main"]
      description = weather_data["weather"][0]["description"]
      temp_kelvin = weather_data["main"]["temp"]
      temp_fahrenheit = round((temp_kelvin - 273.15) * (9/5) + 32)
      humidity = weather_data["main"]["humidity"]
      print(f"The weather in {user_city} is: {weather}")
      print(f"Description: {description}")
      print(f"The temperature in {user_city} is: {temp_fahrenheit}°F")
      print(f"The humidity in {user_city} is: {humidity}%")
    except KeyError:
      print("Error: Invalid data format from API")
  else:
    print(f"No city found for {user_city}")

while True:
  user_city = input("Enter the name or zipcode of the city : ")
  weather_data = get_weather_info(user_city, api_key)
  display_weather(weather_data, user_city)
  break
