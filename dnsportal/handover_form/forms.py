from django import forms
from .models import *


class HandOver_form(forms.ModelForm):
    class Meta:
        model = handover_details
        fields = "__all__"
        widgets = {
            'function': forms.Select(attrs={'class': 'form-control'}),
            'incident_ticket': forms.TextInput(attrs={'class': "form-control"}),
            'vendor_ticket': forms.TextInput(attrs={'class': "form-control"}),
            'problem_statement': forms.TextInput(attrs={'class': "form-control"}),
            'summary': forms.TextInput(attrs={'class': "form-control"}),
            'submitted_by': forms.TextInput(attrs={'class': "form-control"}),
            'assigned_to': forms.TextInput(attrs={'class': "form-control"}),
            'submitted_date': forms.TextInput(attrs={'class': "form-control", 'type': 'date'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
        }
