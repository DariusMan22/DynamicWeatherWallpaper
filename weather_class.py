import Kelvin_to_Celsius

class Weather:
    """ class that handles weather variables needed """

    def __init__(self, city_name, current_weather, description, temperature):
        self.city_name = city_name
        self.current_weather = current_weather
        self.temperature = Kelvin_to_Celsius.connvertKtoC(temperature)
        self.description = description
    