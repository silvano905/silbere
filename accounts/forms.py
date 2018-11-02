from django import forms
from .models import Profile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import Textarea, TextInput, IntegerField


class UserFormRegistration(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')


class UserFormProfile(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('gender', 'description', 'profile_pic')

        widgets = {
            'description': TextInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['description'].label = "Descripción"
        self.fields['profile_pic'].label = "Foto de perfil"


# -------------------------to update---------------------------------------

class UserFormProfileUpdate(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['description', 'profile_pic']

        widgets = {
            'description': Textarea(attrs={'class': 'form-control'}),
        }


class UserFormCreationFormUpdate(forms.ModelForm):
    User._meta.get_field('email')._unique = True
    User._meta.get_field('username')._unique = True

    class Meta:
        model = User
        fields = ('username',)

        widgets = {
            'username': TextInput(attrs={'class': 'form-control'})
        }