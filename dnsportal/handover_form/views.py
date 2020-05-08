from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from pyexpat.errors import messages

from .forms import *
from .models import *


# Create your views here.


@login_required()
def handover_form(request):
    form = HandOver_form()  # form called from forms.py
    if request.method == "POST":
        form = HandOver_form(request.POST or None, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("/handover_form")
        else:
            print(form.errors)
    return render(request, "handover_form/handover_form.html", {"form": form})


@login_required()
def handover_view(request, func):
    if func == "ravpn":
        title = "RAVPN"
    elif func == "dns":
        title = "DNS"
    else:
        title = "Network Devices"
    content = handover_details.objects.filter(function=title)
    return render(request, "handover_form/handover_view.html", {'content': content, 'title': title})


@login_required()
def handover_edit(request, id):
    content = handover_details.objects.get(id=id)
    form = HandOver_form(request.POST or None, instance=content)
    return render(request, 'handover_form/handover_update.html', {'form': form, 'content': content})


@login_required()
def handover_update(request, id):
    content = handover_details.objects.get(id=id)
    form = HandOver_form(request.POST or None, request.FILES, instance=content)
    if form.is_valid():
        func_type = form.cleaned_data['function']
        if func_type == "RAVPN":
            b = 'ravpn'
        elif func_type == "DNS":
            b = 'dns'
        else:
            b = 'network'
        form.save()
        return redirect("/handover_form/view/" + b)
    else:
        print(form.errors)
    return render(request, 'handover_form/handover_update.html', {'form': form, 'content': content})
