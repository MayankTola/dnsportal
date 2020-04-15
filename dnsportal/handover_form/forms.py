from django import forms
from .models import *
from django.contrib.admin import widgets


# class DateTimeInput(forms.DateTimeInput):
#     input_type = "datetime-local"
#
#     def __init__(self, **kwargs):
#         kwargs["format"] = '%m/%d/%Y %H:%M'
#         super().__init__(**kwargs)


class HandOver_form(forms.ModelForm):
    class Meta:
        model = handover_details
        fields = "__all__"
        widgets = dict(function=forms.Select(attrs={'class': 'form-control'}),
                       incident_ticket=forms.TextInput(attrs={'class': "form-control"}),
                       vendor_ticket=forms.TextInput(attrs={'class': "form-control"}),
                       problem_statement=forms.TextInput(attrs={'class': "form-control"}),
                       summary=forms.Textarea(attrs={'class': "form-control"}),
                       submitted_by=forms.TextInput(attrs={'class': "form-control"}),
                       assigned_to=forms.TextInput(attrs={'class': "form-control"}),
                       submitted_date=forms.TextInput(attrs={'class': "form_datetime", 'id': 'date-field'}),
                       status=forms.Select(attrs={'class': 'form-control'}),
                       last_updated_by=forms.TextInput(attrs={'class': "form-control"}),
                       last_updated_date=forms.TextInput(attrs={'class': "form_datetime", 'id': 'date-field'}),
                       resolution=forms.Textarea(attrs={'class': "form-control"}))
                       # file=forms.FileField(attrs={'class': "form-control"}))
