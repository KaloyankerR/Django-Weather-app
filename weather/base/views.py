import requests
from django.shortcuts import render
from .models import City
from .forms import CityForm


# Create your views here.
def index(request):
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&appid=b15f9fd26448fd72a810d6c7bfe7bb74&units=metric'

    if request.method == 'POST':
        form = CityForm(request.POST)
        form.save() 

    form = CityForm()
    cities = City.objects.all()
    cities_data = []

    for city in cities:
        r = requests.get(url.format(city)).json()

        weather_data = {
            'city': city.name,
            'temperature': r['main']['temp'],
            'description': r['weather'][0]['description'],
            'icon': r['weather'][0]['icon']
        }
        cities_data.append(weather_data)

    context = {'cities_data': cities_data, 'form': form}
    return render(request, 'base/index.html', context)
