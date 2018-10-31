from django import forms
from .models import GroupMessage


class MakeMessageGroupForm(forms.ModelForm):

    class Meta:
        model = GroupMessage
        exclude = ('user', 'member', 'created_date')
