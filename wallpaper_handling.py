import os
import image_handling
import get_part_of_day
import random
import ctypes


def for_linux(current_weather,description):
    """wallpaper change prcedure for linux ubuntu"""
    
    image_handling.search_and_dw(
                f'{current_weather} {description} {get_part_of_day.get_moment()} wallpaper {random.randint(1,100)}'
                )
    path = image_handling.get_image_path('Wallpapers/')
    image_handling.swicth_image()
    os.system(f"gsettings set org.gnome.desktop.background picture-uri file://{path}")

def for_windows(current_weather,description):
    """wallpaper change procedure fow windows 64 bits"""

    image_handling.search_and_dw(
                f'{current_weather} {description} {get_part_of_day.get_moment()} wallpaper {random.randint(1,100)}'
                )
    path = image_handling.get_image_path('Wallpapers/')
    image_handling.swicth_image()
    SPI_SETDESKWALLPAPER = 20
    ctypes.windll.user32.SystemParametersInfoW(20, 0, path, 3)



