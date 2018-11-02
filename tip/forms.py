from django import forms
from .models import MakeTip
from django.forms import Textarea, TextInput, ImageField


class MakePostForm(forms.ModelForm):

    class Meta:
        model = MakeTip
        fields = ['title', 'post_pic', 'info']

        widgets = {
            'info': Textarea(attrs={'class': 'form-control'}),
            'title': TextInput(attrs={'class': 'form-control'})
        }
