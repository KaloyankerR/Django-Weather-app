import requests
from django.shortcuts import render

# Create your views here.
def index(request):
    city = 'Sofia'
    api_key = 'b15f9fd26448fd72a810d6c7bfe7bb74'
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&appid=b15f9fd26448fd72a810d6c7bfe7bb74&units=standard'

    r = requests.get(url.format(city)).json()

    weather_data = {
        'city': city,
        'temperature': r['main']['temp'],
        'description': r['weather'][0]['description'],
        'icon': r['weather'][0]['icon']
    }

    print(weather_data)

    return render(request, 'base/index.html')
