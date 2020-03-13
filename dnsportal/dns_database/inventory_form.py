from django import forms


class site_form(forms.Form):

    management_ip = forms.GenericIPAddressField(required=True, widget=forms.TextInput(attrs={"class": "form-control"}))
    location = forms.CharField(required=True, widget=forms.TextInput(attrs={"class": "form-control"}))
    site_address = forms.CharField(required=True, widget=forms.TextInput(attrs={"class": "form-control"}))
    spoc_name1 = forms.CharField(required=True, widget=forms.TextInput(attrs={"class": "form-control"}))
    spoc_contact1 = forms.CharField(required=True, widget=forms.TextInput(attrs={"class": "form-control"}))
    spoc_name2 = forms.CharField(required=True, widget=forms.TextInput(attrs={"class": "form-control"}))
    spoc_contact2 = forms.CharField(required=True, widget=forms.TextInput(attrs={"class": "form-control"}))

class virtual_form(forms.Form):

    management_ip = forms.GenericIPAddressField(required=True, widget=forms.TextInput(attrs={"class": "form-control"}))




