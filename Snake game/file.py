import requests
import os
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient

# OpenWeatherMap API
OWM_ENDPOINT = "https://api.openweathermap.org/data/2.5/onecall"

API_KEY = os.environ.get("c82b8f9ca711e23b4e51fac78d04f3e7")

# Twilio API
ACCOUNT_SID = os.environ.get("AC8101c025d883201aa978a019ce84eb66")
AUTH_TOKEN = os.environ.get("603e022844d7a641b84d0cf7a82d8e3a")
FROM_PHONE_NUMBER = "+12524771488"  # Replace with your Twilio phone number
TO_PHONE_NUMBER = "9675329115"  # Replace with the recipient's phone number

# Weather parameters
LATITUDE = 28.669155
LONGITUDE = 77.453758
EXCLUDE = "current,minutely,daily"

weather_params = {
    "lat": LATITUDE,
    "lon": LONGITUDE,
    "appid": API_KEY,
    "exclude": EXCLUDE
}

try:
    # Make the request to OpenWeatherMap API
    response = requests.get(OWM_ENDPOINT, params=weather_params)
    response.raise_for_status()

    # Parse the response JSON
    weather_data = response.json()
    weather_slice = weather_data["hourly"][:12]

    will_rain = any(int(hour_data["weather"][0]["id"]) < 700 for hour_data in weather_slice)

    if will_rain:
        # Twilio setup with proxy client
        proxy_client = TwilioHttpClient()
        proxy_client.session.proxies = {'https': os.environ.get('https_proxy', '')}

        client = Client(ACCOUNT_SID, AUTH_TOKEN, http_client=proxy_client)

        # Send SMS notification
        message = client.messages.create(
            body="It's going to rain today. Remember to bring an ☔️",
            from_=FROM_PHONE_NUMBER,
            to=TO_PHONE_NUMBER
        )

        print(f"SMS sent successfully. Status: {message.status}")

except requests.exceptions.RequestException as e:
    print(f"Error making OpenWeatherMap API request: {e}")

except Exception as e:
    print(f"An unexpected error occurred: {e}")
