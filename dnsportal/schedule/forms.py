from django import forms
from .models import *
from django.contrib.admin import widgets



class schedule_form(forms.ModelForm):
    class Meta:
        model = schedule
        fields = "__all__"

