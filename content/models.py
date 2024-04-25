from django.db import models

class City(models.Model):
    name = models.CharField(max_length=100)
    

    def __str__(self):
        return self.name

class HistoricalWeather(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    date = models.DateField()
    temperature = models.FloatField()
    description = models.CharField(max_length=100)
    icon = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.city.name} - {self.date}"
    


class User(models.Model):
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=50)