import requests
from concurrent.futures import ThreadPoolExecutor

API_KEY = 'YOUR_API_KEY'


def get_weather(city):
    try:
        url = f'http: //api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}'
        response = requests.get(url)
        data = response.json()
        temperature = data['main']['temp']
        return city, temperature
    except KeyError:
        print(f"Error: Unable to fetch weather data for {city}")
        return city, None


def get_weather_threadpool(cities):
    with ThreadPoolExecutor() as executor:
        results = executor.map(get_weather, cities)
    return results


if __name__ == '__main__':
    favorite_cities = ['Kyiv', 'London', 'Paris', 'Berlin', 'Rome']
    weather_data_threadpool = get_weather_threadpool(favorite_cities)
    for city, temperature in weather_data_threadpool:
        if temperature is not None:
            print(f'Temperature in {city}: {temperature} K')
