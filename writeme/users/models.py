# import datetime
# from django.db import models
# from django.contrib.auth.models import User
# from django.db.models.signals import post_save
# from django.dispatch import receiver
#
# class Profile(models.Model):
#     GENDER_CHOICES = (
#         ('M', 'Male'),
#         ('F', 'Female')
#     )
#
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     first_name = models.TextField()
#     last_name = models.TextField()
#     gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
#     birthdate = models.DateField(default=datetime.date(1900, 1, 1))
#
# # Create a Profile model automatically upon creation of User
# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)
#
# # Update Profile model automatically when User is updated/edited
# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     instance.profile.save()