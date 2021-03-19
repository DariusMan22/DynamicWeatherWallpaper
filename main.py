import API_functions
import weather_class
import loop_timing_functions

def main(api_city):
    API_functions.weather_object_get(api_city).change_Linux()
    
    
if __name__ == "__main__":
    api_city = API_functions.input_get()
    main(api_city)
    loop_timing_functions.setInterval(10, main,api_city)
   
        
