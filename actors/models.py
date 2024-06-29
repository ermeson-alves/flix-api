from django.db import models
from django_countries.fields import CountryField

GENDER_CHOICES = (
    ('M', 'Male'), 
    ('F', 'Female')
)

class Actor(models.Model):
    name = models.CharField(max_length=200)
    birthday = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=100,
                              choices=GENDER_CHOICES,
                              null=True,
                              blank=True)
    nationality = CountryField()
    
    def __str__(self):
        return self.name

