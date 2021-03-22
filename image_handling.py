import icrawler.builtin
import os
import random

def search_and_dw(keyword):
    """function that searches and downloads an image from google image based on the keyword given"""

    color =["color", "blackandwhite", "transparent", "red", "orange", "yellow", "green", "teal", "blue", "purple","pink", "white", "gray", "black", "brown"]
    date = [
            ((2016,random.randint(1,12),random.randint(1,28)),None),((2017,random.randint(1,12),random.randint(1,28)),None),
            ((2018,random.randint(1,12),random.randint(1,28)),None),((2019,random.randint(1,12),random.randint(1,28)),None),
            ((2020,random.randint(1,12),random.randint(1,28)),None),((2021,random.randint(1,12),random.randint(1,28)),None)
            ]
    filters = dict(
                    size='large',
                    date = random.choice(date),
                    color = random.choice(color)
                    )
                
    path = os.path.abspath('temp_wallpaper')
    google_crawler = icrawler.builtin.GoogleImageCrawler(storage={'root_dir': path})
    google_crawler.crawl(keyword=keyword,filters= filters, max_num=1)


def get_image_path(half_path):
    image_name = get_image_name("temp_wallpaper")
    path = os.path.abspath(f'{half_path}{image_name}')
    return path    

def get_image_name(half_path):
    """the purpose is to get the name of the image file independent on the jpg/png/gif etc extensions"""

    pathdir = os.path.abspath(half_path)
    contents = os.listdir(pathdir)
    for content in contents:
        if content.find("000001") != -1:
            return content

def swicth_image():
    path = get_image_path('Wallpapers/')
    temppath = get_image_path("temp_wallpaper/")
    os.replace(temppath, path)
