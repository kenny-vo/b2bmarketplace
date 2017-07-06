from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

class Listing(models.Model):
    user = models.ForeignKey(User)
    topic = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    budget = models.DecimalField(max_digits=10, decimal_places=2)
    location = models.CharField(max_length=50)
    requirement1 = models.CharField(max_length=50)
    requirement2 = models.CharField(max_length=50)
    requirement3 = models.CharField(max_length=50)
    date = models.DateField(default=datetime.now, blank=True)

    def __str__(self):
        return self.topic
        return self.description
        return self.budget
        return self.location
        return self.requirement1
        return self.requirement2
        return self.requirement3
        return self.date
