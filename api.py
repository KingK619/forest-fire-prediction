import requests
from pprint import pprint
print('1. Weather by City')
print('2. Weather by Coordinates')



choice= int(input('Enter your choice: '))
if(choice == 1):
    city = input('Enter your city : ')
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid=09d6ff7d84e1ad00519ed579350511e1'.format(city)
if(choice == 2):
    lat = input('Enter latitude: ')
    lon = input('Enter longitude: ')
    url='http://api.openweathermap.org/data/2.5/weather?lat={}&lon={}&appid=09d6ff7d84e1ad00519ed579350511e1'.format(lat,lon)
print(url)
res = requests.get(url)

data = res.json()
print(data)

temp = data['main']['temp']
wind_speed = data['wind']['speed']

latitude = data['coord']['lat']
longitude = data['coord']['lon']

description = data['weather'][0]['description']

print('Temperature : {} degree celcius'.format(temp))
print('Wind Speed : {} m/s'.format(wind_speed))
print('Latitude : {}'.format(latitude))
print('Longitude : {}'.format(longitude))
print('Description : {}'.format(description))