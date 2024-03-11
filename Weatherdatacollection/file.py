import requests

url=('https://api.openweathermap.org/data/2.5/weather?&appid=663a379d2056a0004f5a1d2ea2d6da83')
response=requests.get(url)
weatherdata=response.json()

print("JSOn response",weatherdata)

high=weatherdata['list'][0]['temp']['max']
print("max",max)