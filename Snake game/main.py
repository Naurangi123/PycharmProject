#recovery H1G16G2EVB6RBPY94LZF1RQY
import requests
import os
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient
#https://api.openweathermap.org/data/2.5/weather?q=Ghaziabad,India&appid=c82b8f9ca711e23b4e51fac78d04f3e7
#https://api.openweathermap.org/data/2.5/onecall?lat=28.669155&lon=77.453758&exclude=hourly,daily&appid=c82b8f9ca711e23b4e51fac78d04f3e7
OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = os.environ.get("9363c0f491806878b754b4d483d73031")
account_sid = "AC8101c025d883201aa978a019ce84eb66"
auth_token = os.environ.get("603e022844d7a641b84d0cf7a82d8e3a")

weather_params = {
    "lat": 28.669155,
    "lon": 77.453758,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]

will_rain = False

for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    proxy_client = TwilioHttpClient()
    proxy_client.session.proxies = {'https': os.environ['https_proxy']}

    client = Client(account_sid, auth_token, http_client=proxy_client)
    message = client.messages \
        .create(
        body="It's going to rain today. Remember to bring an ☔️",
        from_="+12524771488",
        to="9675329115"
    )
    print(message.status)
