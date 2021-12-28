import requests
import numpy as np
import pandas as pd
import random
import json
from pprint import pprint

finalList=[]
# coordinates = [(-30.676220 , 152.749980),(-30.241739 , 155.818985),(-32.193218, 151.700562),(-33.416665, 150.7833302),(-33.700001 , 150.300003),(-34.5,150.9),(-36.499998,148.333332),(-34.91119, 138.70735),(-35.775243 , 137.214242),(-43.1622541, 146.1999743),(33.5083153,-85.7872486),(39.6030447, -122.8297321),(36.1111101,-81.8201438),(38.6054001,-120.466501),(34.3168052,-118.0079471),(47.283719,-113.0892777),(-3.4653052,-62.2246353),(-1.8286872,-64.5377078),(-2.7123835,-72.3267565),(-7.4071854,-52.2063277),(-7.4015584,-54.3811576),(-15.2319444,-67.6526537),(-15.0092192,-64.8401539)]
# lat,lon = -15.286851,133.2752936

# input_df = pd.read_csv("apiInput.csv")
# for index, row in input_df.iterrows():
#     lat=row['latitude']
#     lon=row['longitude']
#     url='http://api.openweathermap.org/data/2.5/weather?lat={}&lon={}&appid=09d6ff7d84e1ad00519ed579350511e1&units=metric'.format(lat,lon)
#     print(url)
#     res = requests.get(url)

#     data = res.json()
#     print(data)

#     ffmc=0.0
#     temp = data['main']['temp']
#     humidity=data['main']['humidity']
#     wind = data['wind']['speed']
#     rain=0.0
#     if "rain" in data:
#         rain=data['rain']['1h']

#     inputList = [ffmc,temp,humidity,wind,rain]
#     print('Temperature : {} degree celcius'.format(temp))
#     print('Humidity : {} '.format(humidity))
#     print('Wind Speed : {} m/s'.format(wind))
#     print('Rain : {} '.format(rain))
#     print("---------------------------")
    
#     # Feed the 'inputList' to the model. The prediction done by the model is stored in 'prediction'.
#     prediction = random.randint(0, 100) * 100000     # assigned random values for now.
#     # Append the tuple into 'finalList'
#     finalList.append((lat,lon,prediction))

# print(finalList)

# #convert data to CSV for heatmap 

# column_names = ['latitude', 'longitude', 'prediction']
# data = np.array(finalList)
# my_df = pd.DataFrame(data, columns=column_names)
# my_df.to_csv('predictions.csv')


# Future Forecast Predictions

futurePredicList=[]
cooridnates=[(-3.4653052,-62.2246353, 'Amazon Forest'),(-34.91119 , 138.70735 , 'Adelaide Hills' ),(34.3168052,-118.0079471, 'Angeles National Forest'),(-32.193218, 151.700562,'Hunter Region')]
for lat, lon,name in cooridnates:
    # url='http://api.openweathermap.org/data/2.5/forecast/daily?lat={}&lon={}&cnt=4&appid=09d6ff7d84e1ad00519ed579350511e1&units=metric'.format(lat,lon)
    url='https://api.openweathermap.org/data/2.5/forecast/daily?lat={}&lon={}&cnt=4&appid=3bcfcde9b7438aa7696f020ed75f5673&units=metric'.format(lat,lon)
    # print(url)
    res = requests.get(url)
    data = res.json()

    data=data['list']
    # print(data)
    length=len(data)
    for l in range(length):
        ffmc=0.0
        temp = data[l]['temp']['max'] - data[l]['temp']['min']
        humidity=data[l]['humidity']
        wind = data[l]['speed']
        rain=0.0
        if "rain" in data[l]:
            rain=data[l]['rain']

        paramList = [ffmc,temp,humidity,wind,rain]
        print('Temperature : {} degree celcius'.format(temp))
        print('Humidity : {} '.format(humidity))
        print('Wind Speed : {} m/s'.format(wind))
        print('Rain : {} '.format(rain))
        print("---------------------------")
    
        # Feed the 'inputList' to the model. The prediction done by the model is stored in 'prediction'.
        prediction = random.randint(0, 100)     # assigned random values for now.
        # Append the tuple into 'finalList'
        futurePredicList.append((lat,lon,name,l+1,prediction))
    
# #convert data to CSV for heatmap 

column_names = ['latitude', 'longitude','name','day', 'prediction']
data = np.array(futurePredicList)
my_df = pd.DataFrame(data, columns=column_names)
my_df.to_csv('graphData.csv')
