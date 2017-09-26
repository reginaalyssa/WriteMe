from django.db import models
from django.contrib.auth.models import User

class Conversation(models.Model):
    user1 = models.ForeignKey(User, related_name='%(class)s_1')
    user2 = models.ForeignKey(User, related_name='%(class)s_2')

class Message(models.Model):
    conversation = models.ForeignKey(Conversation)
    sender = models.ForeignKey(User)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    unread_flag = models.BooleanField(default=True)
