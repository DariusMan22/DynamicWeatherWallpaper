import requests
import json

def openweathermap_get(api_city):
    """function that return a list of city_name, current_weather, description and temperature"""

    url = f'http://api.openweathermap.org/data/2.5/weather?q={api_city[1]}&appid={api_city[0]}'
    response = requests.get(url)
    data = json.loads(response.text)    
    
    temperature = data['main']['temp']
    current_weather = data['weather'][0]['main']
    description = data['weather'][0]['description']
    weather_param = []
    weather_param = [api_city[1], current_weather, description, temperature]
    return weather_param