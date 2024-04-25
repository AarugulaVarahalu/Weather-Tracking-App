from django.urls import path
from .views import home, index, logout, register, login, add_city, delete_city
urlpatterns = [
    path('', home, name='home'),
    path('register/', register, name='register'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'), 
    path('index/', index, name='weather'),
    path('add/', add_city, name='add_city'),
    path('delete/<str:city_name>/', delete_city, name='delete_city'),
]