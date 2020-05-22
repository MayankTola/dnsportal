from django import forms
from .models import *


class roster_form(forms.ModelForm):
    class Meta:
        model = roster_details
        fields = "__all__"
