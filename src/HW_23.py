import random
import requests


def get_random_website():
    websites = ["https://www.google.com", "https://www.facebook.com", "https://www.twitter.com",
                "https://www.amazon.com", "https://www.apple.com"]
    return random.choice(websites)


def get_website_info():
    website = get_random_website()
    response = requests.get(website)
    status_code = response.status_code
    website_name = website.split('//')[1]
    html_length = len(response.text)

    print(f"Website: {website_name}")
    print(f"Status Code: {status_code}")
    print(f"HTML Length: {html_length}")


def get_weather(city):
    geocoding_api_url = "https://api.open-meteo.com/v1/geocode"
    weather_api_url = "https://api.open-meteo.com/v1/forecast"

    # Get coordinates for the city
    geocoding_params = {
        "limit": 1,
        "q": city
    }
    geocoding_response = requests.get(geocoding_api_url, params=geocoding_params).json()

    if geocoding_response and isinstance(geocoding_response, list) and geocoding_response[0] and "latitude" in geocoding_response[0] and "longitude" in geocoding_response[0]:
        latitude = geocoding_response[0]["latitude"]
        longitude = geocoding_response[0]["longitude"]

        # Get weather information for the coordinates
        weather_params = {
            "latitude": latitude,
            "longitude": longitude,
            "hourly": "temperature_2m,precipitation",
            "timezone": "auto"
        }
        weather_response = requests.get(weather_api_url, params=weather_params).json()

        if weather_response and "hourly" in weather_response:
            current_weather = weather_response["hourly"][0]
            temperature = current_weather["temperature_2m"]["value"]
            precipitation = current_weather["precipitation"]["value"]

            print(f"Weather in {city}:")
            print(f"Temperature: {temperature}°C")
            print(f"Precipitation: {precipitation} mm/h")
        else:
            print("Unable to fetch weather information.")
    else:
        print("Invalid city name.")


# Завдання 1
get_website_info()

# Завдання 2
city = input("Введіть назву міста: ")
get_weather(city)
