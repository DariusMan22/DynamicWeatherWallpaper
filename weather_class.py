import platform
import image_handling
import random
import wallpaper_handling

class Weather:
    """ class that handles weather variables needed """

    def __init__(self, city_name, current_weather, description, temperature):
        self.city_name = city_name
        self.current_weather = current_weather
        self.temperature = temperature
        self.description = description

    def connvertKtoC(self):
        """comverts kelvin to celsius"""

        Ctemperature = self.temperature - 272.15
        return Ctemperature

    def change_linux(self):
        """checks the description,weather and temperature in order to pick the right image"""
        
        wallpaper_handling.for_linux(self.current_weather,self.description)

    def change_windows(self):
        """checks the description,weather and temperature in order to pick the right image"""
        
        wallpaper_handling.for_windows(self.current_weather, self.description)

    def change_wallpaper(self):
        """changes wallpaper based on the weather given, also checks for the operating system"""

        if platform.uname()[0] == "Linux":
            if platform.uname()[3].find("Ubuntu") != -1:
                self.change_linux()
            else:
                print("Not supported for the moment")
        elif platform.uname()[0] == "Windows":
            if platform.uname()[2] == '10':
                self.change_windows()
            else:
                 print("Not supported for the moment")
