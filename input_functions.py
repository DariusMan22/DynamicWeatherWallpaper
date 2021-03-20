

def city_input():
    """function that creates and returns city_name that came from the user input"""

    print("Please insert the name of your City:")
    city_name = input()
    return city_name


def time_input():
    """asks for time input and converts it to minutes"""
    x = input(f'How often do you want the wallpaper do be changed(minutes)?:\n')
    x = float(x)
    x = x * 60
    return x
