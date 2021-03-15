import API_functions
import weather_class
from loop_timing_functions import setInterval
from wallpaper_handling import change_wallpaper 

def main(api_city):
    weather_param = []
    weather_param = API_functions.openweathermap_get(api_city)
    weather_object = weather_class.Weather(weather_param[0],weather_param[1],weather_param[2],weather_param[3])
    change_wallpaper()

if __name__ == "__main__":
    api_key = '4d349fc5726852568f381fb6e06dc0f2'
    api_city = []
    api_city.append(api_key)
    print("Please insert the name of your City:")
    city_name = input()
    api_city.append(city_name)
    main(api_city)
    setInterval(10, main, api_city)
        
    