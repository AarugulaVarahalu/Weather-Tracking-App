# Generated by Django 4.2.11 on 2024-04-24 07:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0005_delete_historicalweather'),
    ]

    operations = [
        migrations.CreateModel(
            name='HistoricalWeather',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('temperature', models.FloatField()),
                ('description', models.CharField(max_length=100)),
                ('icon', models.CharField(max_length=10)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='content.city')),
            ],
        ),
    ]