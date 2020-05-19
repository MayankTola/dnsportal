from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import *
from .models import *


# Create your views here.


@login_required()
def upload_schedule(request):
    form = schedule_form  # form called from forms.py
    if request.method == "POST":
        form = schedule_form(request.POST or None, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("/schedule/upload")
        else:
            print(form.errors)
    return render(request, "schedule.html", {"form": form})

@login_required()
def view_schedule(request):
    form = schedule_form  # form called from forms.py
    if request.method == "POST":
        form = schedule_form(request.POST or None, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("/schedule/upload")
        else:
            print(form.errors)
    return render(request, "schedule.html", {"form": form})