import os
import image_handling
import get_part_of_day
import random

def for_linux(current_weather,description):
    image_handling.search_and_dw(
                f'{current_weather} {description} {get_part_of_day.get_moment()} wallpaper {random.randint(1,100)}'
                )
    image_name = image_handling.get_image_name()
    tempath = os.path.abspath(f'temp_wallpaper/{image_name}')
    path = os.path.abspath(f'Wallpapers/{image_name}')
    os.replace(tempath, path)
    os.system(f"gsettings set org.gnome.desktop.background picture-uri file://{path}")