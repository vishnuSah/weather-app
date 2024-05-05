from django.shortcuts import render, HttpResponse
from rest_framework.decorators import api_view
import requests
import json
from config import give_my_key

api_key = give_my_key()
# print(api_key)
# Create your views here.

@api_view(['GET','POST'])
def home(request):
    try:
        if request.method == 'POST':
            f = request.POST
            city_name = f['city']
            print(city_name)

            API_KEY = api_key
            city = city_name
            URL = f'http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={city}&aqi=no'
            source = requests.get(URL).content
            data = json.loads(source)
            # print(type(data))
            # print(data)
            country = data['location']['country']
            city = data['location']['name']
            date_time = data['location']['localtime']
            temperature = data['current']['temp_c']
            day_condition = data['current']['condition']['text']
            print(country,city,date_time,temperature,day_condition)

            context = {
            'country':country,
            'city':city,
            'date_time':date_time,
            'temperature':temperature,
            'day_condition':day_condition
            }
            
            return render(request, 'home.html', context)
        
        return render(request, 'home.html')

        
    
    except Exception as e:
        print(e)

    
