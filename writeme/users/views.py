from django.contrib.auth import login, authenticate
from django.views.generic.edit import FormView
from .forms import SignUpForm

class UserCreateView(FormView):
    template_name = 'users/signup.html'
    form_class = SignUpForm
    success_url = '/'

    def form_valid(self, form):
        form.save()
        username = form.cleaned_data.get('username')
        raw_password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=raw_password)
        login(self.request, user)
        return super(UserCreateView, self).form_valid(form)