from django import forms
from .models import Friend


class MakeFriendForm(forms.ModelForm):

    class Meta:
        model = Friend
        exclude = ('user', 'friend')

