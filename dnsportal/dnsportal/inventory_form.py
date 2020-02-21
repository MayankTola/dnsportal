from django import forms


class submission_form(forms.Form):
    # query_type = forms.ChoiceField(choices=(('A','A'),('AAAA','AAAA')))
    # location = forms.ChoiceField(choices=my_locations)
    location = forms.CharField(required=True, widget=forms.TextInput(attrs={"class": "form-control"}))
    management_ip = forms.CharField(required=True, widget=forms.TextInput(attrs={"class": "form-control"}))
    site_address = forms.CharField(required=True, widget=forms.TextInput(attrs={"class": "form-control"}))
    spoc_name1 = forms.CharField(required=True, widget=forms.TextInput(attrs={"class": "form-control"}))
    spoc_name2 = forms.CharField(required=True, widget=forms.TextInput(attrs={"class": "form-control"}))
    spoc_contact1 = forms.CharField(required=True, widget=forms.TextInput(attrs={"class": "form-control"}))
    spoc_contact2 = forms.CharField(required=True, widget=forms.TextInput(attrs={"class": "form-control"}))
