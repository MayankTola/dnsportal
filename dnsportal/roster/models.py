from django.db import models


# Create your models here.

class roster_details(models.Model):
    file = models.FileField(blank=True, upload_to="roster")

    class Meta:
        db_table = "roster_details"
