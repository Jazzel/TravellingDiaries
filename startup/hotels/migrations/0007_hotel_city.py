# Generated by Django 2.2.5 on 2020-03-08 13:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cities_light', '0008_city_timezone'),
        ('hotels', '0006_hotel_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotel',
            name='city',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='cities_light.City'),
        ),
    ]
