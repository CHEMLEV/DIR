from django.db import models
from django.urls import reverse

class Tour (models.Model):
    title = models.CharField(max_length=100)
    destination = models.TextField(max_length=100)
    duration = models.IntegerField()
    price = models.IntegerField()
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse ("tour_details", kwargs={"pk": self.pk})

class Agent (models.Model):
    
    name_last_name = models.TextField(max_length=100)
    position = models.TextField(max_length=100)
    department = models.TextField(max_length=100)
    
    def __str__(self):
        return self.name_last_name
    
    def get_absolute_url(self):
        return reverse ("tour_details", kwargs={"pk": self.pk})




