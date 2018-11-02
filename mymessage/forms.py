from django import forms
from .models import MyMessage
from django.forms import Textarea


class MakeMessageForm(forms.ModelForm):
    class Meta:
        model = MyMessage
        fields = ('text', 'picture')

        widgets = {
            'text': Textarea(attrs={'class':'form-control'}),
        }
