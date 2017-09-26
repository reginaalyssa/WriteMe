from django import forms
from .models import Message
from django.contrib.auth.models import User

class NewMessageForm(forms.Form):
    username = forms.CharField(max_length=170)
    message = forms.CharField(widget=forms.Textarea)

    def save(self, user):
        new_message = Message(
            user_sender=user,
            user_receiver=User.objects.get(username=self.username),
            message=self.message
        )
        new_message.save()