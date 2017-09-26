from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.db.models import Q
from django.urls import reverse
from django.views.generic import ListView
from django.views.generic.edit import FormView
from .models import Message, Conversation
from .forms import NewMessageForm

class MessagesView(LoginRequiredMixin, ListView):
    template_name = "messaging/index.html"
    context_object_name = 'latest_conversations_list'

    def get_queryset(self):
        """
        Return a list of last messages sent/received for each unique user.
        """
        # Get list of people the user had a conversation with.
        conversation_list = Conversation.objects.filter(Q(user1=self.request.user) | Q(user2=self.request.user))

        # Retrieve latest messages for each conversation.
        message_list = []
        for conversation in conversation_list:
            message_list.append(Message.objects.filter(conversation=conversation).latest('timestamp'))

        # Sort messages by timestamp, with most recent timestamp first.
        message_list.sort(key=lambda x: x.timestamp, reverse=True)
        return message_list

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