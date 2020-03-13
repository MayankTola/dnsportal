from django.db import models

# Create your models here.
from django.db import models


class site_details(models.Model):

    management_ip = models.GenericIPAddressField(max_length=50)
    location = models.CharField(max_length=20)
    site_address = models.CharField(max_length=50)
    spoc_name1 = models.CharField(max_length=20)
    spoc_contact1 = models.CharField(max_length=13)
    spoc_name2 = models.CharField(max_length=20)
    spoc_contact2 = models.CharField(max_length=13)

    class Meta:
        db_table = "site_details"


class vip_details(models.Model):

    management_ip = models.GenericIPAddressField(max_length=50)
    virtual_ip = models.GenericIPAddressField(max_length=50)
    description = models.CharField(max_length=20)

    class Meta:
        db_table = "vip_details"