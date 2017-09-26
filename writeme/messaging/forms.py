from django import forms
from django.contrib.auth.models import User
from django.db.models import Q

from .models import Message, Conversation

class NewMessageForm(forms.Form):
    username = forms.CharField(max_length=150)
    message = forms.CharField(widget=forms.Textarea)

    def save(self, user):
        user1 = user
        user2 = User.objects.get(username=self.username)

        """
        Check if conversation between user1 and user2 already exists.
        If not, create new conversation.
        """
        try:
            conversation = Conversation.objects.get(
                (Q(user1=user1) & Q(user2=user2)) |
                (Q(user1=user2) & Q(user2=user1))
            )
        except Conversation.DoesNotExist:
            conversation = Conversation(
                user1=user1,
                user2=user2
            )
            conversation.save()

        """
        Create new message between user1 and user2.
        """
        new_message = Message(
            conversation=conversation,
            sender=user1,
            message=self.message
        )
        new_message.save()