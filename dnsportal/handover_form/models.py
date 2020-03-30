from django.db import models
import datetime

func_choices = (
    ("RAVPN", "RAVPN"),
    ("DNS", "DNS"),
    ("CDC Devices", "CDC Devices"),
)
status_choices = (
    ("Active", "Active"),
    ("Closed", "Closed"),
)


# Create your models here.
class handover_details(models.Model):
    function = models.CharField(max_length=20, choices=func_choices, default='RAVPN')
    incident_ticket = models.CharField(blank=True, max_length=20)
    vendor_ticket = models.CharField(blank=True, max_length=20)
    problem_statement = models.CharField(blank=True, max_length=50)
    summary = models.CharField(blank=True, max_length=100)
    submitted_by = models.CharField(blank=True, max_length=20)
    assigned_to = models.CharField(blank=True, max_length=20)
    submitted_date = models.DateField(default=datetime.date.today)
    status = models.CharField(max_length=10, choices=status_choices, default='Active')

    class Meta:
        db_table = "handover_details"
