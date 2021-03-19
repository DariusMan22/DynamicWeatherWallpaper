import API_functions
import weather_class
import loop_timing_functions
import input_functions
import time



def main():
    api_city = input_functions.city_input()
    x = input_functions.time_input()
    while True:
        API_functions.weather_object_get(api_city).change_wallpaper()
        time.sleep(x)

if __name__ == "__main__":
    main()