from django.db import models

# Create your models here.
class Airport(models.Model):
    code = models.CharField(max_length=3)
    city = models.CharField(max_length=64)

    """
        Beautiful and 
        more meaningful exhibition
    """
    def __str__(self):
        return f"{self.city}({self.code}) Airport"

class Flight(models.Model):
    origin = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="departures")
    destination = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="arrivals")
    duration = models.IntegerField()


    """
        Beautiful and 
        more meaningful exhibition
    """
    def __str__(self):
        return f"{self.id}: from {self.origin} to {self.destination}"
    
class Passenger(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    flights=models.ManyToManyField(Flight, blank=True, related_name="passengers")
    
    """
        Beautiful and 
        more meaningful exhibition
    """
    def __str__(self):
        return f"{self.first_name} {self.last_name}"