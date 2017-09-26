from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.db.models import Q
from django.urls import reverse
from django.views.generic import ListView
from django.views.generic.edit import FormView
from .models import Message
from .forms import NewMessageForm

class MessagesView(LoginRequiredMixin, ListView):
    template_name = "messaging/index.html"
    context_object_name = 'latest_conversations_list'

    def get_queryset(self):
        """
        Return a list of last messages sent/received for each unique user.
        """
        return Message.objects.all() # temporary

class NewMessageView(FormView):
    form_class = NewMessageForm
    template_name = 'messaging/new_message.html'

    def get_success_url(self):
        return reverse('messaging:messages')

    def get_initial(self):
        initial = super(NewMessageView, self).get_initial()
        initial['username'] = self.kwargs.get('username')
        return initial

    def form_valid(self, form):
        username = form.cleaned_data['username']
        message = form.cleaned_data['message']
        user = User.objects.get(username=username)
        if user is None:
            form.add_error(username, "User does not exist")
            super(NewMessageView, self).form_invalid(form)
        form.save(self.request.user)
        return super(NewMessageView, self).form_valid(form)