import platform
import os
def change_wallpaper():
    """changes wallpaper based on the weather given"""

#    OS = platform.platform()
#   if OS.find('Linux'):
    
    os.system("gsettings set org.gnome.desktop.background picture-uri file:///home/dariusvm/Documents/wallpaper_weather/Wallpapers/gabriel-76bE8c9Um98-unsplash.jpg")
