# DynamicWeatherWallpaper
->For now this project only supports Linux ubuntu distribution and Windows10 64bit.

->You will need an API key from openweathermap.org to use this code. You can generate the key for free.

->the key needs to be inserted in the config.ini file as such: api_key = 24234234asfsdf2321342 (just paste the key that you got from the weather site)

->you need to wait a couple of minutes for the key to be activated after you generate it

->Run the code and insert your city and how often do you want the code to change the wallpaper and check the weather update in witch case the theme for the wallpapers will change

  This is a Pyhton program that extracts data about weather based on the chosen city by the user through the openweathermap.org API and changes the wallpaper of the user dynamically according to the results.
The wallpapers are extracted using a web crawler. The code is made to run continously and will periodically check if your weather parameters changed or your hour interval changed and will update the wallpaper accordingly to the new keyword generated.

