from django.db import models
import datetime

func_choices = (
    ("RAVPN", "RAVPN"),
    ("DNS", "DNS"),
    ("Network Devices", "Network Devices"),
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
    problem_statement = models.CharField(blank=True, max_length=150)
    summary = models.TextField(blank=True, max_length=5000)
    submitted_by = models.CharField(blank=True, max_length=20)
    assigned_to = models.CharField(blank=True, max_length=20)
    submitted_date = models.DateTimeField()
    status = models.CharField(max_length=10, choices=status_choices, default='Active')
    last_updated_by = models.CharField(blank=True, max_length=20)
    last_updated_date = models.DateTimeField()
    resolution = models.TextField(blank=True, max_length=5000)

    class Meta:
        db_table = "handover_details"
