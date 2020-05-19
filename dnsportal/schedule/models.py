from django.db import models


# Create your models here.
class schedule(models.Model):
    file = models.FileField(blank=True, upload_to="roster")
