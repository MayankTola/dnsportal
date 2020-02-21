from django.db import models


class MyModelName(models.Model):
    """A typical class defining a model, derived from the Model class."""

    # Fields
    location = models.CharField(required=True,widget=models.TextInput(attrs={"class":"form-control"}))
    management_ip = models.CharField(required=True,widget=models.TextInput(attrs={"class":"form-control"}))
    site_address = models.CharField(required=True,widget=models.TextInput(attrs={"class":"form-control"}))
    spoc_name1 = models.CharField(required=True,widget=models.TextInput(attrs={"class":"form-control"}))
    spoc_name2 = models.CharField(required=True,widget=models.TextInput(attrs={"class":"form-control"}))
    spoc_contact1 = models.CharField(required=True,widget=models.TextInput(attrs={"class":"form-control"}))
    spoc_contact2 = models.CharField(required=True,widget=models.TextInput(attrs={"class":"form-control"}))

    ...

    # Metadata
    class Meta:
        ordering = ['created_on']



    # Methods
    def get_absolute_url(self):
        """Returns the url to access a particular instance of MyModelName."""
        return reverse('model-detail-view', args=[str(self.id)])

    def __str__(self):
        """String for representing the MyModelName object (in Admin site etc.)."""
        return self.my_field_name