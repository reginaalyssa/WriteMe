import datetime
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        del self.fields['password2']

        for fieldname in ['username', 'password1']:
            self.fields[fieldname].help_text = None

    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female')
    )

    first_name = forms.CharField(max_length=70)
    last_name = forms.CharField(max_length=70)
    gender = forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.RadioSelect(), initial=GENDER_CHOICES[0][0])
    birthdate = forms.DateField(initial=datetime.date(1900, 1, 1))

    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'gender',
            'birthdate',
            'password1',
        )