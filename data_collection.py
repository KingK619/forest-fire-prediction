import requests
import numpy as np
import pandas as pd
import random
from pprint import pprint

finalList=[]
coordinates = [(-30.676220 , 152.749980),(-30.241739 , 155.818985),(-32.193218, 151.700562),(-33.416665, 150.7833302),(-33.700001 , 150.300003),(-34.5,150.9),(-36.499998,148.333332),(-37.3431579, 148.0222592),(-34.91119, 138.70735),(-35.775243 , 137.214242),(-43.1622541, 146.1999743)]
# lat,lon = -15.286851,133.2752936

for lat,lon in coordinates:
    url='http://api.openweathermap.org/data/2.5/weather?lat={}&lon={}&appid=09d6ff7d84e1ad00519ed579350511e1&units=metric'.format(lat,lon)
    print(url)
    res = requests.get(url)

    data = res.json()
    # print(data)

    ffmc=0.0
    temp = data['main']['temp']
    humidity=data['main']['humidity']
    wind = data['wind']['speed']
    rain=0.0
    if "rain" in data:
        rain=data['rain']['1h']

    inputList = [ffmc,temp,humidity,wind,rain]
    print('Temperature : {} degree celcius'.format(temp))
    print('Humidity : {} '.format(humidity))
    print('Wind Speed : {} m/s'.format(wind))
    print('Rain : {} '.format(rain))
    print("---------------------------")
    
    # Feed the 'inputList' to the model. The prediction done by the model is stored in 'prediction'.
    prediction = random.randint(0, 100) * 100000     # assigned random values for now.
    # Append the tuple into 'finalList'
    finalList.append((lat,lon,prediction))

print(finalList)

#convert data to CSV for heatmap 

column_names = ['latitude', 'longitude', 'prediction']
data = np.array(finalList)
my_df = pd.DataFrame(data, columns=column_names)
my_df.to_csv('predictions.csv')

