import API_functions
import weather_class
import loop_timing_functions
import input_functions



def main(api_city):
    API_functions.weather_object_get(api_city).change_Linux()


if __name__ == "__main__":
    api_city = input_functions.city_input()
    x = input_functions.time_input()
    main(api_city)
    loop_timing_functions.setInterval(x, main, api_city)
