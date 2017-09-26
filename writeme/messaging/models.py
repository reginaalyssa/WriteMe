from django.db import models
from django.contrib.auth.models import User

class Message(models.Model):
    user_sender = models.ForeignKey(User, related_name='%(class)s_sender')
    user_receiver = models.ForeignKey(User, related_name='%(class)s_receiver')
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    unread_flag = models.BooleanField(default=True)