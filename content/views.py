import requests
from django.shortcuts import render, redirect
from .models import City, HistoricalWeather
from django.shortcuts import get_object_or_404
from django.contrib.auth import logout as auth_logout
from .models import User
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from .forms import LoginForm, RegistrationForm


def home(request):
    return render(request, 'home.html')

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            # Create user
            user = User.objects.create_user(username=username, password=password)
            # Authenticate and login the user
            auth_login(request, user)
            # Redirect to logged-in page
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})


def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('weather')
            else:
                error_message = "Invalid username or password."
                return render(request, 'login.html', {'form': form, 'error_message': error_message})
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})
from django.contrib.auth.models import User



def logout(request):
    auth_logout(request)
    return redirect('login')



def index(request):
    cities = City.objects.all()
    weather_data = []
    for city in cities:
        url = f'http://api.openweathermap.org/data/2.5/weather?q={city.name}&appid=a87788d03715dc371a152023a7cae6da&units=metric'
        response = requests.get(url).json()
        weather = {
            'city': city.name,
            'temperature': response['main']['temp'],
            'description': response['weather'][0]['description'],
            'icon': response['weather'][0]['icon']
        }
        weather_data.append(weather)
    return render(request, 'weather.html', {'weather_data': weather_data})

def add_city(request):
    if request.method == 'POST':
        city_name = request.POST['city']
        City.objects.create(name=city_name)
    return redirect('weather')

def delete_city(request, city_name):
    if request.method == 'POST':
        City.objects.filter(name=city_name).delete()
    return redirect('weather')

