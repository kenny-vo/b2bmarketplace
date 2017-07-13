""" Models below """

from datetime import datetime
from django.db import models
from django.contrib.auth.models import User
from djmoney.models.fields import MoneyField

class Listing(models.Model):
    """ Listing Model """

    user = models.ForeignKey(User)
    topic = models.CharField(verbose_name='Topic', max_length=100)
    description = models.CharField(verbose_name='Description', max_length=500)
    budget = MoneyField(verbose_name='Budget',
                        max_digits=10,
                        decimal_places=2,
                        default_currency='USD')
    location = models.CharField(verbose_name='Location', max_length=50)
    requirement1 = models.CharField(verbose_name='Requirements(1)', max_length=50)
    requirement2 = models.CharField(verbose_name='Requirements(2)', max_length=50)
    requirement3 = models.CharField(verbose_name='Requirements(3)', max_length=50)
    date = models.DateField(verbose_name='Date Posted', default=datetime.now, blank=True)
    date_required = models.DateField(verbose_name='Date Required')

    def __str__(self):
        return self.topic
        return self.description
        return self.budget
        return self.location
        return self.requirement1
        return self.requirement2
        return self.requirement3
        return self.date
        return self.date_required
