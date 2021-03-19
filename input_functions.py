def city_input():
    """function that creates and returns a list of the api_key and city_name that came from the user input"""
    api_key = '4d349fc5726852568f381fb6e06dc0f2'
    api_city = []
    api_city.append(api_key)
    print("Please insert the name of your City:")
    city_name = input()
    api_city.append(city_name)
    return api_city


def time_input():
    x = input(f'How often do you want the wallpaper do be changed(minutes)?:\n')
    x = float(x)
    x = x * 60
    return x