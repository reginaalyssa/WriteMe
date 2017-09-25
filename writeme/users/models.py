from django.db import models
from django.contrib.auth.models import User

class User(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female')
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.TextField()
    last_name = models.TextField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    birthdate = models.DateField()