from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .forms import *
from .models import *
from .remote_login import *


# Create your views here.

# Functions for CRUD operations.

@login_required()
def inventory_form(request):
    form = site_form()
    if request.method == "POST":
        form = site_form(request.POST or None)
        if form.is_valid():
            form.save()
        else:
            print(form.errors)
    return render(request, "database/inventory_form.html", {"form": form})


@login_required()
def inventory_view(request):
    content = site_details.objects.all()
    title = 'Site'
    return render(request, "database/inventory_view.html", {'content': content, 'title':title})


@login_required()
def inventory_edit(request, id):
    content = site_details.objects.get(id=id)
    form = site_form(request.POST or None, instance=content)
    return render(request, 'database/inventory_update.html', {'content': content, 'form': form})


@login_required()
def inventory_update(request, id):
    content = site_details.objects.get(id=id)
    form = site_form(request.POST or None, instance=content)
    if form.is_valid():
        form.save()
        return redirect("/inventory/view")
    return render(request, 'database/inventory_update.html', {'content': content})


@login_required()
def inventory_delete(request, id):
    content = site_details.objects.get(id=id)
    content.delete()
    return redirect("/inventory/view")



@login_required()
def virtual_form(request):
    form = virtual_form()
    if request.method == "POST":
        form = virtual_form(request.POST or None)
        if form.is_valid():
            form.save()
        else:
            print(form.errors)
    return render(request, "database/inventory_form.html", {"form": form})



