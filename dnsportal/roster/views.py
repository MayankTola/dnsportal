from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import *
from .models import *


# Create your views here.

@login_required()
def roster_upload(request):
    form = roster_form()  # form called from forms.py
    if request.method == "POST":
        form = roster_form(request.POST or None, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("/roster")
        else:
            print(form.errors)
    return render(request, "roster/roster_upload.html", {"form": form})


@login_required()
def roster_view(request):
    myimg = roster_details.objects.last()
    return render(request, "roster/roster_view.html", {"myimg": myimg})
