# Generated by Django 4.2.7 on 2023-11-06 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flight_management', '0003_flight_booked_seats_flight_total_seats_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='seat_number',
            field=models.PositiveIntegerField(blank=True),
        ),
    ]
