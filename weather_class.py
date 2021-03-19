import platform
import os
import platform
import image_handling
import get_part_of_day
import random

class Weather:
    """ class that handles weather variables needed """

    def __init__(self, city_name, current_weather, description, temperature):
        self.city_name = city_name
        self.current_weather = current_weather
        self.temperature = temperature
        self.description = description

    def connvertKtoC(self):
        """comverts kelvin to celcius"""

        Ctemperature = self.temperature - 272.15
        return Ctemperature

    def change_Linux(self):
        """checks the description,weather and temperature in order to pick the right wallpaper"""
        image_handling.search_and_dw(f'{self.current_weather} {self.description} {get_part_of_day.get_moment()} {self.city_name} wallpaper {random.randint(1,100)}')
        tempath = os.path.abspath('temp_wallpaper/000001.jpg')
        path = os.path.abspath('Wallpapers/000001.jpg')
        os.replace(tempath,path)
        os.system(f"gsettings set org.gnome.desktop.background picture-uri file://{path}")

    def change_wallpaper(self):
        """changes wallpaper based on the weather given"""
        
        if platform.uname()[0] == "Linux":
            if platform.uname()[3].find("Ubuntu") != -1:
                self.change_Linux()
            else:
                print("Not supported for the moment")
        else:
            print("Not supported for the moment")