import requests
from bs4 import BeautifulSoup
import json
import time
import urllib.request
url = "https://mylocation.org/"
response = requests.get(url)
webContent = response.content
soup = BeautifulSoup(webContent, 'html.parser')
titleNames = soup.findAll("td")
city = titleNames[7].text



def get_weather(apiKey, city):
    url = "http://dataservice.accuweather.com/locations/v1/search?apikey="+apiKey+"&q="+city+"&language=en-us&details=true"
    with urllib.request.urlopen(url) as url:
        data = json.loads(url.read().decode())
    print(data)
    return (data[0]['Temperature']['Imperial']['Value'],
            data[0]['RelativeHumidity'],
            data[0]['Wind']['Direction']['Degrees'],
            data[0]['Wind']['Speed']['Imperial']['Value'],
            data[0]['UVIndex'],
            data[0]['CloudCover'],
            data[0]['Pressure']['Metric']['Value'],
            data[0]['Precip1hr']['Metric']['Value'],
            data)


apiKey = "" #YOUR API KEY
timestamp = time.time()
temperature, humidity, wind_bearing, wind_speed, uv_index, cloud_cover, pressure, precipitation, raw \
    = get_weather(apiKey, city)
