from django import forms
from .models import Message, Conversation
from django.contrib.auth.models import User

class NewMessageForm(forms.Form):
    username = forms.CharField(max_length=150)
    message = forms.CharField(widget=forms.Textarea)

    def save(self, user):
        conversation = Conversation(
            user1=user,
            user2=User.objects.get(username=self.username),
        )

        if len(conversation) == 0:
            conversation.save()

        new_message = Message(
            conversation=conversation,
            message=self.message
        )
        new_message.save()