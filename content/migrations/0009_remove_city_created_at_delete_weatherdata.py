# Generated by Django 4.2.11 on 2024-04-25 05:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0008_city_created_at_weatherdata'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='city',
            name='created_at',
        ),
        migrations.DeleteModel(
            name='WeatherData',
        ),
    ]
