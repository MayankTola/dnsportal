from django import forms
from .models import *


class site_form(forms.ModelForm):

    class Meta:
        model = site_details
        fields = "__all__"
        widgets = {
            'management_ip': forms.TextInput(attrs={'class': "form-control"}),
            'location': forms.TextInput(attrs={'class': "form-control"}),
            'site_address': forms.TextInput(attrs={'class': "form-control"}),
            'spoc_name1': forms.TextInput(attrs={'class': "form-control"}),
            'spoc_contact1': forms.TextInput(attrs={'class': "form-control"}),
            'spoc_name2': forms.TextInput(attrs={'class': "form-control"}),
            'spoc_contact2': forms.TextInput(attrs={'class': "form-control"}),
        }


class virtual_form(forms.Form):
    class Meta:
        model = virtual_server
        fields = "__all__"
        widgets = {
              'management_ip': forms.TextInput(attrs={'class': "form-control"}),
              'virtual_ip': forms.TextInput(attrs={'class': "form-control"}),
              'description': forms.TextInput(attrs={'class': "form-control"}),

        }
