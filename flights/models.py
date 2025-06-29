


from django.db import models
from django.contrib.auth.models import User

import json
import math

class Flights(models.Model):
    origin = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    departure_date = models.DateField()
    landing_date = models.DateField()
    departure_time = models.TimeField()
    arrival_time = models.TimeField()
    total_no_of_seats = models.IntegerField()
    price = models.IntegerField()
    seats_available = models.JSONField(null=True,blank=True)  

    def save(self, *args, **kwargs):
          # Only populate if empty (first time)
        if not self.seats_available: 
            self.seats_available = self.generate_seats()
        super().save(*args, **kwargs)

    def generate_seats(self):
        seat_letters = ['A', 'B', 'C', 'D', 'E']
        total_seats = self.total_no_of_seats
        rows = math.ceil(total_seats / len(seat_letters))
        seats = []
        count = 0
        for row in range(1, rows + 1):
            for letter in seat_letters:
                if count < total_seats:
                    seats.append(f"{row}{letter}")
                    count += 1
                else:
                    break
        return seats

  
# models.py
class Booking(models.Model):
    flight = models.ForeignKey(Flights, on_delete=models.CASCADE)
    seat_number = models.CharField(max_length=5)
    user_name = models.CharField(max_length=100)  # or use auth.User
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True) 

    booked_at = models.DateTimeField(auto_now_add=True)
    meal_choice = models.CharField(max_length=50, choices=[
        ('Veg', 'Vegetarian'),
        ('Non-Veg', 'Non-Vegetarian'),
        ('Jain', 'Jain Meal'),
        ('No Meal', 'No Meal')
    ])
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        # Remove seat from flight.seats_available
        if self.seat_number in self.flight.seats_available:
            self.flight.seats_available.remove(self.seat_number)
            self.flight.save()
