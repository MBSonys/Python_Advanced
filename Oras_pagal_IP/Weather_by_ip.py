import requests
from password import pss, pss_2
import csv

ip_list = ['122.35.203.161',
           '174.217.10.111',
           '187.121.176.91',
           '176.114.85.116',
           '174.59.204.133',
           '54.209.112.174',
           '109.185.143.49',
           '176.114.253.216',
           '210.171.87.76',
           '24.169.250.142'
           ]
def getting_data(locations):
    ip = []
    country = []
    city = []
    map = []
    for location in locations:
        r = requests.get(f"https://api.freegeoip.app/json/{location}?apikey={pss}")
        info = r.json()
        ip.append(info["ip"])
        country.append(info["country_name"])
        city.append(info["city"])
        map.append([info["latitude"], info["longitude"]])
    return ip, country, city, map

data = getting_data(ip_list)

def getting_weather(data):
    weather = []
    for i in range(0,10):
        payload = {'lat': data[3][i][0], 'lon': data[3][i][1], 'units': 'metric', 'appid': pss_2}
        r = requests.get('http://api.openweathermap.org/data/2.5/weather/', params=payload)
        gather = r.json()
        weather.append([gather["main"]["temp"], gather["weather"][0]["description"]])
    return weather


data_2 = getting_weather(data)

with open('ip_data.csv', 'a') as f:
    writer = csv.writer(f, delimiter=',')
    writer.writerow(['IP', 'Country', 'City', 'Temp', 'Weather'])
    for i in range(0,10):
        writer.writerow((data[0][i], data[1][i], data[2][i], data_2[i][0], data_2[i][1]))
