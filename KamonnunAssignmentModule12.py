# Kamonnun Silarat - Python Assignment Module 12

# Task 1

import requests

def getRandomJoke():
    request = "https://api.chucknorris.io/jokes/random"
    response = requests.get(request)

    if response.status_code == 200:
        joke_data = response.json()
        joke_text = joke_data.get("value", "Cannot fetch Chuck Norris joke.")
        return joke_text

if __name__ == "__main__":
    chuck_norris_joke = getRandomJoke()
    print("Chuck Norris Joke (Random):")
    print(chuck_norris_joke)

# Task 2

class OpenWeatherAPI:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "http://api.openweathermap.org/data/2.5/weather"

    def getWeatherData(self, city):
        params = {'q': city, 'appid': self.api_key}
        response = requests.get(self.base_url, params=params)

        if response.status_code == 200:
            weather_data = response.json()
            description = weather_data['weather'][0]['description']
            temp_kelvin = weather_data['main']['temp']
            temp_celsius = temp_kelvin - 273
            return description, temp_celsius
        else:
            return None, None

if __name__ == "__main__":
    api_key = "86e7ef6ef622f9d57365029229e19c8e"
    city = input("Enter the name of the municipality: ")

    weather_api = OpenWeatherAPI(api_key)
    description, temperature = weather_api.getWeatherData(city)

    if description is not None and temperature is not None:
        print(f"Weather in {city}: {description}")
        print(f"Temperature: {temperature:.2f}°C")
    else:
        print("Failed to fetch the weather information.")