from django.views.generic import ListView
from django.contrib.auth.models import User

class HomeView(ListView):
    template_name = "home.html"
    context_object_name = 'user_list'

    def get_queryset(self):
        """
        Return all registered users' First Name and Last Name.
        """
        return User.objects.all().exclude(is_superuser=True)
