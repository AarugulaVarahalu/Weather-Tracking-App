# Generated by Django 4.2.11 on 2024-04-24 06:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0002_city_historicalweather'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='historicalweather',
            name='city',
        ),
        migrations.DeleteModel(
            name='Weather',
        ),
        migrations.DeleteModel(
            name='HistoricalWeather',
        ),
    ]
