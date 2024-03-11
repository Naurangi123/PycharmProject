import requests
import os
from datetime import datetime

url="https://api.openweathermap.org/data/2.5/weather?q"
location=input("enter the city name:")
user_api="663a379d2056a0004f5a1d2ea2d6da83"
complete_api_link=url+"q="+location+"&appid="+user_api


api_link=requests.get(complete_api_link)
api_data=api_link.json()
print(api_data)

if api_data['cod']=='404':
    print("Invalid City:{},Please check you City name".format(location))
else:
    temp_city=((api_data['main']['temp'])-273.15)
    weather_desc=api_data['weather'][0]['description']
    hmdt=api_data['main']['humidity']
    wind_spd=api_data['wind']['speed']
    date_time=datetime.now().strftime("%d %b %y|%I:%M:%S: %p")

    print("----------------------------------------------------------")
    print("Weather States for-{} ||{}".format(location.upper(),date_time))
    print("----------------------------------------------------------")

    print("Current tempreture is:{:.2f} deg C".format(temp_city))
    print("Current weather desc :",weather_desc)
    print("Current humidity:",hmdt,'%')
    print("Current wind speed:",wind_spd,'kmph')