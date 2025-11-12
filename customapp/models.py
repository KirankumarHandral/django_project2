from django.db import models


# Create your models here.
class Flight(models.Model):
    flightid = models.CharField(max_length=10)
    flight_name = models.CharField(max_length=100)
    starting_from= models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available_seats = models.IntegerField()
    total_seats = models.IntegerField()
    flight_type = models.CharField(max_length=50, choices=[('domestic', 'Domestic'), ('international', 'International')])
    flight_supply = models.CharField(max_length=100, choices=[('airline', 'Airline'), ('charter', 'Charter')])
    flight_status = models.CharField(max_length=50, choices=[('on_time', 'On Time'), ('delayed', 'Delayed'), ('cancelled', 'Cancelled')])

