from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.db.models import Q
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views.generic import ListView
from django.views.generic.edit import FormView
from .models import Message, Conversation
from .forms import NewMessageForm

class RecentMessagesListView(LoginRequiredMixin, ListView):
    template_name = "messaging/index.html"
    context_object_name = 'latest_conversation_messages_list'

    def get_queryset(self):
        """
        Return a list of last messages sent/received for each unique user.
        """
        # Get list of people the user had a conversation with.
        conversation_list = Conversation.objects.filter(Q(user1=self.request.user) | Q(user2=self.request.user))

        # Retrieve latest messages for each conversation.
        latest_conversation_messages_list = []
        for conversation in conversation_list:
            latest_conversation_messages_list.append(Message.objects.filter(conversation=conversation).latest('timestamp'))

        # Sort messages by timestamp, with most recent timestamp first.
            latest_conversation_messages_list.sort(key=lambda x: x.timestamp, reverse=True)
        return latest_conversation_messages_list

class NewMessageView(LoginRequiredMixin, FormView):
    form_class = NewMessageForm
    template_name = 'messaging/new_message.html'

    def get_success_url(self):
        return reverse('messaging:messages')

    def get_initial(self):
        initial = super(NewMessageView, self).get_initial()
        initial['username'] = self.kwargs.get('username')
        return initial

    def form_valid(self, form):
        form.username = form.cleaned_data['username']
        form.message = form.cleaned_data['message']
        try:
            user = User.objects.get(username=form.username)
        except:
            form.add_error('username', "User does not exist")
            return super(NewMessageView, self).form_invalid(form)

        form.save(self.request.user)
        return super(NewMessageView, self).form_valid(form)


class ConversationMessagesListView(ListView):
    template_name = "messaging/conversation.html"
    context_object_name = 'messages_list'

    def get_queryset(self):
        """
        Return a list of messages in conversation between user1 and user2.
        """
        user1 = self.request.user
        user2 = User.objects.get(username=self.kwargs.get('username'))

        # Get the conversation between user1 and user2.
        try:
            conversation = Conversation.objects.get(
                (Q(user1=user1) & Q(user2=user2)) |
                (Q(user1=user2) & Q(user2=user1))
            )
        except Conversation.DoesNotExist:
            print("Did not retrieve conversation.")
            return None

        # Retrieve all messages for the conversation, with most recent first.
        messages_list = Message.objects.filter(conversation=conversation).order_by('timestamp')
        return messages_list

    def get_context_data(self, **kwargs):
        context = super(ConversationMessagesListView, self).get_context_data(**kwargs)
        context['conversation_user'] = get_object_or_404(User, username=self.kwargs.get('username'))
        return context
