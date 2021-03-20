import API_functions
import weather_class
import loop_timing_functions
import input_functions
import time
import config_handling



def main():
    city = input_functions.city_input()
    key = config_handling.get_key()
    key_city = [key,city]
    x = input_functions.time_input()
    while True:
        API_functions.weather_object_get(key_city).change_wallpaper()
        time.sleep(x)

if __name__ == "__main__":
    main()